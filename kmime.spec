%define major 5
%define libname %mklibname KF5Mime %{major}
%define devname %mklibname KF5Mime -d

Name: kmime
Version:	23.08.5
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for handling MIME types
URL: https://kde.org/
License: GPL
Group: System/Libraries
Requires: %{libname} = %{EVRD}
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: boost-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

%description
KDE library for handling MIME types

%package -n %{libname}
Summary: KDE library for handling MIME types
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for handling MIME types

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libkmime5

%files -f libkmime5.lang
%{_datadir}/qlogging-categories5/kmime.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_docdir}/qt5/*.{qch,tags}
