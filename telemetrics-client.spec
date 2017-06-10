#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : telemetrics-client
Version  : 1.12.2
Release  : 80
URL      : https://github.com/clearlinux/telemetrics-client/releases/download/v1.12.2/telemetrics-client-1.12.2.tar.gz
Source0  : https://github.com/clearlinux/telemetrics-client/releases/download/v1.12.2/telemetrics-client-1.12.2.tar.gz
Summary  : Telemetrics library
Group    : Development/Tools
License  : LGPL-2.1
Requires: telemetrics-client-bin
Requires: telemetrics-client-config
Requires: telemetrics-client-autostart
Requires: telemetrics-client-lib
Requires: telemetrics-client-data
Requires: telemetrics-client-doc
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libdw)
BuildRequires : pkgconfig(libelf)
BuildRequires : pkgconfig(libsystemd)
Patch1: memleak.patch

%description
No detailed description available

%package autostart
Summary: autostart components for the telemetrics-client package.
Group: Default

%description autostart
autostart components for the telemetrics-client package.


%package bin
Summary: bin components for the telemetrics-client package.
Group: Binaries
Requires: telemetrics-client-data
Requires: telemetrics-client-config

%description bin
bin components for the telemetrics-client package.


%package config
Summary: config components for the telemetrics-client package.
Group: Default

%description config
config components for the telemetrics-client package.


%package data
Summary: data components for the telemetrics-client package.
Group: Data

%description data
data components for the telemetrics-client package.


%package dev
Summary: dev components for the telemetrics-client package.
Group: Development
Requires: telemetrics-client-lib
Requires: telemetrics-client-bin
Requires: telemetrics-client-data
Provides: telemetrics-client-devel

%description dev
dev components for the telemetrics-client package.


%package doc
Summary: doc components for the telemetrics-client package.
Group: Documentation

%description doc
doc components for the telemetrics-client package.


%package lib
Summary: lib components for the telemetrics-client package.
Group: Libraries
Requires: telemetrics-client-data
Requires: telemetrics-client-config

%description lib
lib components for the telemetrics-client package.


%prep
%setup -q -n telemetrics-client-1.12.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1497105831
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1497105831
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../telemd.path %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/telemd.path
mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../telemd.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/telemd.socket
mkdir %{buildroot}/usr/lib/systemd/system/timers.target.wants
ln -s ../hprobe.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/hprobe.timer
ln -s ../pstore-clean.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/pstore-clean.service
ln -s ../pstore-probe.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/pstore-probe.service
ln -s ../oops-probe.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/oops-probe.service
ln -s ../klogscanner.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/klogscanner.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/klogscanner.service
/usr/lib/systemd/system/multi-user.target.wants/oops-probe.service
/usr/lib/systemd/system/multi-user.target.wants/pstore-clean.service
/usr/lib/systemd/system/multi-user.target.wants/pstore-probe.service
/usr/lib/systemd/system/multi-user.target.wants/telemd.path
/usr/lib/systemd/system/sockets.target.wants/telemd.socket
/usr/lib/systemd/system/timers.target.wants/hprobe.timer

%files bin
%defattr(-,root,root,-)
/usr/bin/crashprobe
/usr/bin/hprobe
/usr/bin/journalprobe
/usr/bin/klogscanner
/usr/bin/oopsprobe
/usr/bin/pstoreclean
/usr/bin/pstoreprobe
/usr/bin/telem-record-gen
/usr/bin/telemctl
/usr/bin/telemd

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/klogscanner.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/oops-probe.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/pstore-clean.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/pstore-probe.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/telemd.path
%exclude /usr/lib/systemd/system/sockets.target.wants/telemd.socket
%exclude /usr/lib/systemd/system/timers.target.wants/hprobe.timer
/usr/lib/sysctl.d/40-crash-probe.conf
/usr/lib/systemd/system.conf.d/40-core-ulimit.conf
/usr/lib/systemd/system/hprobe.service
/usr/lib/systemd/system/hprobe.timer
/usr/lib/systemd/system/journal-probe.service
/usr/lib/systemd/system/klogscanner.service
/usr/lib/systemd/system/oops-probe.service
/usr/lib/systemd/system/pstore-clean.service
/usr/lib/systemd/system/pstore-probe.service
/usr/lib/systemd/system/telemd.path
/usr/lib/systemd/system/telemd.service
/usr/lib/systemd/system/telemd.socket
/usr/lib/tmpfiles.d/telemetrics-dirs.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/telemetrics/telemetrics.conf

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libtelemetry.so
/usr/lib64/pkgconfig/libtelemetry.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtelemetry.so.3
/usr/lib64/libtelemetry.so.3.0.0
