#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : telemetrics-client
Version  : 2.1.1
Release  : 99
URL      : https://github.com/clearlinux/telemetrics-client/releases/download/v2.1.1/telemetrics-client-2.1.1.tar.gz
Source0  : https://github.com/clearlinux/telemetrics-client/releases/download/v2.1.1/telemetrics-client-2.1.1.tar.gz
Source1  : telemd-update-trigger.service
Summary  : Telemetrics library
Group    : Development/Tools
License  : LGPL-2.1
Requires: telemetrics-client-autostart = %{version}-%{release}
Requires: telemetrics-client-bin = %{version}-%{release}
Requires: telemetrics-client-config = %{version}-%{release}
Requires: telemetrics-client-data = %{version}-%{release}
Requires: telemetrics-client-lib = %{version}-%{release}
Requires: telemetrics-client-license = %{version}-%{release}
Requires: telemetrics-client-man = %{version}-%{release}
Requires: telemetrics-client-services = %{version}-%{release}
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libdw)
BuildRequires : pkgconfig(libelf)
BuildRequires : pkgconfig(libsystemd)

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
Requires: telemetrics-client-data = %{version}-%{release}
Requires: telemetrics-client-config = %{version}-%{release}
Requires: telemetrics-client-license = %{version}-%{release}
Requires: telemetrics-client-man = %{version}-%{release}
Requires: telemetrics-client-services = %{version}-%{release}

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
Requires: telemetrics-client-lib = %{version}-%{release}
Requires: telemetrics-client-bin = %{version}-%{release}
Requires: telemetrics-client-data = %{version}-%{release}
Provides: telemetrics-client-devel = %{version}-%{release}

%description dev
dev components for the telemetrics-client package.


%package lib
Summary: lib components for the telemetrics-client package.
Group: Libraries
Requires: telemetrics-client-data = %{version}-%{release}
Requires: telemetrics-client-license = %{version}-%{release}

%description lib
lib components for the telemetrics-client package.


%package license
Summary: license components for the telemetrics-client package.
Group: Default

%description license
license components for the telemetrics-client package.


%package man
Summary: man components for the telemetrics-client package.
Group: Default

%description man
man components for the telemetrics-client package.


%package services
Summary: services components for the telemetrics-client package.
Group: Systemd services

%description services
services components for the telemetrics-client package.


%prep
%setup -q -n telemetrics-client-2.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551226735
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1551226735
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/telemetrics-client
cp LICENSE.LGPL-2.1 %{buildroot}/usr/share/package-licenses/telemetrics-client/LICENSE.LGPL-2.1
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/telemd-update-trigger.service
## install_append content
mkdir %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../telempostd.path %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/telempostd.path
mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../telemprobd.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/telemprobd.socket
mkdir %{buildroot}/usr/lib/systemd/system/timers.target.wants
ln -s ../hprobe.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/hprobe.timer
mkdir %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants
ln -s ../telemprobd-update-trigger.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/telemprobd-update-trigger.service
ln -s ../pstore-clean.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/pstore-clean.service
ln -s ../pstore-probe.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/pstore-probe.service
ln -s ../python-probe.path %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/python-probe.path
ln -s ../klogscanner.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/klogscanner.service
ln -s ../journal-probe.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/journal-probe.service
ln -s ../bert-probe.service  %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/bert-probe.service
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/klogscanner.service %{buildroot}/usr/share/clr-service-restart/klogscanner.service
ln -s /usr/lib/systemd/system/telemd-update-trigger.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/telemd-update-trigger.service
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system.conf.d/40-core-ulimit.conf

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/bert-probe.service
/usr/lib/systemd/system/multi-user.target.wants/journal-probe.service
/usr/lib/systemd/system/multi-user.target.wants/klogscanner.service
/usr/lib/systemd/system/multi-user.target.wants/pstore-clean.service
/usr/lib/systemd/system/multi-user.target.wants/pstore-probe.service
/usr/lib/systemd/system/multi-user.target.wants/python-probe.path
/usr/lib/systemd/system/multi-user.target.wants/telempostd.path
/usr/lib/systemd/system/sockets.target.wants/telemprobd.socket
/usr/lib/systemd/system/timers.target.wants/hprobe.timer

%files bin
%defattr(-,root,root,-)
/usr/bin/bertprobe
/usr/bin/crashprobe
/usr/bin/hprobe
/usr/bin/journalprobe
/usr/bin/klogscanner
/usr/bin/pstoreclean
/usr/bin/pstoreprobe
/usr/bin/pythonprobe
/usr/bin/telem-record-gen
/usr/bin/telem_journal
/usr/bin/telemctl
/usr/bin/telempostd
/usr/bin/telemprobd

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/sysctl.d/40-crash-probe.conf
/usr/lib/tmpfiles.d/telemetrics-dirs.conf

%files data
%defattr(-,root,root,-)
/usr/share/clr-service-restart/klogscanner.service
/usr/share/defaults/telemetrics/telemetrics.conf

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libtelemetry.so
/usr/lib64/pkgconfig/libtelemetry.pc
/usr/share/man/man3/telemetry.3
/usr/share/man/man3/tm_create_record.3
/usr/share/man/man3/tm_send_record.3
/usr/share/man/man3/tm_set_config_file.3
/usr/share/man/man3/tm_set_payload.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtelemetry.so.3
/usr/lib64/libtelemetry.so.3.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/telemetrics-client/LICENSE.LGPL-2.1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/telem-record-gen.1
/usr/share/man/man1/telemctl.1
/usr/share/man/man1/telempostd.1
/usr/share/man/man1/telemprobd.1
/usr/share/man/man5/telemetrics.conf.5

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/bert-probe.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/journal-probe.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/klogscanner.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/pstore-clean.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/pstore-probe.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/python-probe.path
%exclude /usr/lib/systemd/system/multi-user.target.wants/telempostd.path
%exclude /usr/lib/systemd/system/sockets.target.wants/telemprobd.socket
%exclude /usr/lib/systemd/system/timers.target.wants/hprobe.timer
/usr/lib/systemd/system/bert-probe.service
/usr/lib/systemd/system/hprobe.service
/usr/lib/systemd/system/hprobe.timer
/usr/lib/systemd/system/journal-probe-tail.service
/usr/lib/systemd/system/journal-probe.service
/usr/lib/systemd/system/klogscanner.service
/usr/lib/systemd/system/pstore-clean.service
/usr/lib/systemd/system/pstore-probe.service
/usr/lib/systemd/system/python-probe.path
/usr/lib/systemd/system/python-probe.service
/usr/lib/systemd/system/telemd-update-trigger.service
/usr/lib/systemd/system/telempostd.path
/usr/lib/systemd/system/telempostd.service
/usr/lib/systemd/system/telemprobd-update-trigger.service
/usr/lib/systemd/system/telemprobd.service
/usr/lib/systemd/system/telemprobd.socket
/usr/lib/systemd/system/update-triggers.target.wants/telemd-update-trigger.service
/usr/lib/systemd/system/update-triggers.target.wants/telemprobd-update-trigger.service
