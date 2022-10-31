# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       gemrb

# >> macros
# << macros

Summary:    open-source implementation of Bioware’s Infinity Engine.
Version:    0.9.1
Release:    0
Group:      Applications
License:    GPLv2
URL:        https://github.com/gemrb/gemrb
Source0:    %{name}-%{version}.tar.gz
Source100:  gemrb.yaml
Source101:  gemrb-rpmlintrc
Patch0:     SDL2_cmake_fix.patch
Requires:   libsailfishapp-launcher
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-base >= 3.3
BuildRequires:  python3-libs >= 3.3
BuildRequires:  python3-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  desktop-file-utils

%description
GemRB (Game Engine Made with preRendered Background) is a portable
open-source reimplementation of the Infinity Engine that underpinned Baldur's
Gate, Icewind Dale and Planescape: Torment. It sports a cleaner design, greater
extensibility and several innovations. Would you like to create a game like
Baldur's Gate?

To try it out you either need some of the ORIGINAL game's data or you can
get a tiny sneak peek by running the included trivial game demo.

The original game data has to be installed if you want to see anything but
the included trivial demo. On non-windows systems either copy it over from
a windows install, use a compatible installer, WINE or extract it manually
from the CDs using the unshield tool.

%if "%{?vendor}" == "chum"
PackageName: GemRB Game Engine
Type: other
PackagerName: nephros
Categories:
 - Game
Custom:
  Repo: %{url}
  PackagingRepo: https://github.com/nephros/sailfishos-gemrb
Icon: %{url}/raw/master/artwork/gemrb-logo.png
Url:
  Homepage: https://gemrb.org/
  Help: https://gemrb.org/Documentation.html
  Bugtracker: %{url}/issues
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# SDL2_cmake_fix.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -B%{_builddir}/_build \
    -DSDL_BACKEND=SDL2 \
    -DOPENGL_BACKEND=OpenGL \
    -DLIB_DIR=%{_libdir} \
    -DPLUGIN_DIR=%{_datadir}/%{name}/plugins/


# >> build post
pushd %{_builddir}/_build
%make_build
popd
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
pushd %{_builddir}/_build
%make_install
popd
rm -rf %{buildroot}/%{_docdir}
rm -rf %{buildroot}/%{_mandir}
rm -rf %{buildroot}/%{_datadir}/pixmaps/%{name}.png
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/scalable/apps/%{name}.svg
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_datadir}/metainfo/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
# >> files
# << files
