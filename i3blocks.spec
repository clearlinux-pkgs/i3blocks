#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : i3blocks
Version  : 1.4
Release  : 4
URL      : https://github.com/vivien/i3blocks/releases/download/1.4/i3blocks-1.4.tar.gz
Source0  : https://github.com/vivien/i3blocks/releases/download/1.4/i3blocks-1.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: i3blocks-bin = %{version}-%{release}
Requires: i3blocks-libexec = %{version}-%{release}
Requires: i3blocks-license = %{version}-%{release}
Requires: i3blocks-man = %{version}-%{release}

%description
# i3blocks
[![Build Status](https://travis-ci.org/vivien/i3blocks.svg?branch=master)](https://travis-ci.org/vivien/i3blocks)
[![Join the chat at https://gitter.im/vivien/i3blocks](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/vivien/i3blocks?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

%package bin
Summary: bin components for the i3blocks package.
Group: Binaries
Requires: i3blocks-libexec = %{version}-%{release}
Requires: i3blocks-license = %{version}-%{release}

%description bin
bin components for the i3blocks package.


%package libexec
Summary: libexec components for the i3blocks package.
Group: Default
Requires: i3blocks-license = %{version}-%{release}

%description libexec
libexec components for the i3blocks package.


%package license
Summary: license components for the i3blocks package.
Group: Default

%description license
license components for the i3blocks package.


%package man
Summary: man components for the i3blocks package.
Group: Default

%description man
man components for the i3blocks package.


%prep
%setup -q -n i3blocks-1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564524680
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} PREFIX=/usr


%install
export SOURCE_DATE_EPOCH=1564524680
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/i3blocks
cp COPYING %{buildroot}/usr/share/package-licenses/i3blocks/COPYING
%make_install PREFIX=/usr

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/i3blocks

%files libexec
%defattr(-,root,root,-)
/usr/libexec/i3blocks/bandwidth
/usr/libexec/i3blocks/battery
/usr/libexec/i3blocks/cpu_usage
/usr/libexec/i3blocks/disk
/usr/libexec/i3blocks/iface
/usr/libexec/i3blocks/keyindicator
/usr/libexec/i3blocks/load_average
/usr/libexec/i3blocks/mediaplayer
/usr/libexec/i3blocks/memory
/usr/libexec/i3blocks/openvpn
/usr/libexec/i3blocks/temperature
/usr/libexec/i3blocks/volume
/usr/libexec/i3blocks/wifi

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/i3blocks/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/i3blocks.1
