#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : telemetrics-client
Version  : 2.3.5
Release  : 118
URL      : https://github.com/clearlinux/telemetrics-client/releases/download/v2.3.5/telemetrics-client-2.3.5.tar.gz
Source0  : https://github.com/clearlinux/telemetrics-client/releases/download/v2.3.5/telemetrics-client-2.3.5.tar.gz
Summary  : Telemetrics library
Group    : Development/Tools
License  : LGPL-2.1
Requires: telemetrics-client-bin = %{version}-%{release}
Requires: telemetrics-client-config = %{version}-%{release}
Requires: telemetrics-client-data = %{version}-%{release}
Requires: telemetrics-client-lib = %{version}-%{release}
Requires: telemetrics-client-license = %{version}-%{release}
Requires: telemetrics-client-man = %{version}-%{release}
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libdw)
BuildRequires : pkgconfig(libelf)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : valgrind
Patch1: 0001-Add-polkit-files.patch

%description
No detailed description available

%package bin
Summary: bin components for the telemetrics-client package.
Group: Binaries
Requires: telemetrics-client-data = %{version}-%{release}
Requires: telemetrics-client-config = %{version}-%{release}
Requires: telemetrics-client-license = %{version}-%{release}

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
Requires: telemetrics-client = %{version}-%{release}

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


%prep
%setup -q -n telemetrics-client-2.3.5
cd %{_builddir}/telemetrics-client-2.3.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650043724
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1650043724
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/telemetrics-client
cp %{_builddir}/telemetrics-client-2.3.5/LICENSE.LGPL-2.1 %{buildroot}/usr/share/package-licenses/telemetrics-client/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/lib/sysctl.d/40-crash-probe.conf
rm -f %{buildroot}*/usr/lib/systemd/system/sockets.target.wants/telemprobd.socket
rm -f %{buildroot}*/usr/lib/systemd/system/timers.target.wants/hprobe.timer
rm -f %{buildroot}*/usr/lib/systemd/system/hprobe.service
rm -f %{buildroot}*/usr/lib/systemd/system/hprobe.timer
rm -f %{buildroot}*/usr/lib/systemd/system/journal-probe-tail.service
rm -f %{buildroot}*/usr/lib/systemd/system/journal-probe.service
rm -f %{buildroot}*/usr/lib/systemd/system/klogscanner.service
rm -f %{buildroot}*/usr/lib/systemd/system/pstore-clean.service
rm -f %{buildroot}*/usr/lib/systemd/system/pstore-probe.service
rm -f %{buildroot}*/usr/lib/systemd/system/telempostd.path
rm -f %{buildroot}*/usr/lib/systemd/system/telempostd.service
rm -f %{buildroot}*/usr/lib/systemd/system/telemprobd-update-trigger.service
rm -f %{buildroot}*/usr/lib/systemd/system/telemprobd.service
rm -f %{buildroot}*/usr/lib/systemd/system/telemprobd.socket
rm -f %{buildroot}*/usr/lib/systemd/system/update-triggers.target.wants/telemprobd-update-trigger.service
## install_append content
#mkdir %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
#ln -s ../telempostd.path %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/telempostd.path
#mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
#ln -s ../telemprobd.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/telemprobd.socket
#mkdir %{buildroot}/usr/lib/systemd/system/timers.target.wants
#ln -s ../hprobe.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/hprobe.timer
#mkdir %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants
#ln -s ../telemprobd-update-trigger.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/telemprobd-update-trigger.service
#ln -s ../pstore-clean.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/pstore-clean.service
#ln -s ../pstore-probe.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/pstore-probe.service
#ln -s ../klogscanner.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/klogscanner.service
#ln -s ../journal-probe.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/journal-probe.service
#mkdir -p %{buildroot}/usr/share/clr-service-restart
#ln -sf /usr/lib/systemd/system/klogscanner.service %{buildroot}/usr/share/clr-service-restart/klogscanner.service
#mkdir -p %{buildroot}/usr/share/polkit-1/actions
#mkdir -p %{buildroot}/usr/share/polkit-1/rules.d
#install -m644 org.clearlinux.telemetry.policy %{buildroot}/usr/share/polkit-1/actions/
#install -m644 org.clearlinux.telemetry.rules %{buildroot}/usr/share/polkit-1/rules.d/
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system.conf.d/40-core-ulimit.conf

%files bin
%defattr(-,root,root,-)
/usr/bin/crashprobe
/usr/bin/hprobe
/usr/bin/journalprobe
/usr/bin/klogscanner
/usr/bin/pstoreclean
/usr/bin/pstoreprobe
/usr/bin/telem-record-gen
/usr/bin/telem_journal
/usr/bin/telemctl
/usr/bin/telempostd
/usr/bin/telemprobd

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/telemetrics-dirs.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/telemetrics/telemetrics.conf

%files dev
%defattr(-,root,root,-)
/usr/include/telemetry.h
/usr/lib64/libtelemetry.so
/usr/lib64/pkgconfig/libtelemetry.pc
/usr/share/man/man3/telemetry.3
/usr/share/man/man3/tm_create_record.3
/usr/share/man/man3/tm_send_record.3
/usr/share/man/man3/tm_set_config_file.3
/usr/share/man/man3/tm_set_payload.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtelemetry.so.4
/usr/lib64/libtelemetry.so.4.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/telemetrics-client/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/telem-record-gen.1
/usr/share/man/man1/telemctl.1
/usr/share/man/man1/telempostd.1
/usr/share/man/man1/telemprobd.1
/usr/share/man/man5/telemetrics.conf.5
