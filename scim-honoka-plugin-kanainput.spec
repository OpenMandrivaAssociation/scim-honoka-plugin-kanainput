%define version  0.9.1
%define release  %mkrel 4
%define src_name honoka-plugin-kanainput

%define honoka_version   0.9.0

Name:       scim-honoka-plugin-kanainput
Summary:    A Hiragana input plugin for honoka
Version:    %{version}
Release:    %{release}
Group:      System/Internationalization
License:    GPL
URL:        http://nop.net-p.org/modules/pukiwiki/index.php?%5B%5Bhonoka%5D%5D
Source0:    %{src_name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: scim-honoka-devel >= %{honoka_version}
BuildRequires: automake
BuildRequires: libltdl-devel

%description
A Hiragana input plugin for honoka.


%prep
%setup -q -n %{src_name}-%{version}

%build
./bootstrap
%configure2_5x
# (tv) parallel build is broken:
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove devel files
rm -f $RPM_BUILD_ROOT/%{scim_plugins_dir}/honoka/*.{a,la}

%find_lang honoka-plugin-kanainput

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif


%files -f honoka-plugin-kanainput.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README.jp
%{scim_plugins_dir}/honoka/*.so
