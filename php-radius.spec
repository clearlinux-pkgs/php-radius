#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-radius
Version  : 1.4.0b1
Release  : 2
URL      : https://pecl.php.net/get/radius-1.4.0b1.tgz
Source0  : https://pecl.php.net/get/radius-1.4.0b1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-radius-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
No detailed description available

%package lib
Summary: lib components for the php-radius package.
Group: Libraries

%description lib
lib components for the php-radius package.


%prep
%setup -q -n radius-1.4.0b1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20180731/radius.so
