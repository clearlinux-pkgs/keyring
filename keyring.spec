#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keyring
Version  : 8.5.1
Release  : 17
URL      : https://pypi.python.org/packages/source/k/keyring/keyring-8.5.1.tar.gz
Source0  : https://pypi.python.org/packages/source/k/keyring/keyring-8.5.1.tar.gz
Summary  : Store and access your passwords safely.
Group    : Development/Tools
License  : MIT Python-2.0
Requires: keyring-bin
Requires: keyring-python
BuildRequires : fs-python
BuildRequires : hgtools-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pycrypto-python
BuildRequires : pytest-runner-python
BuildRequires : python-dev
BuildRequires : python-keyczar-python
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : setuptools_scm-python

%description
=======================================
Installing and Using Python Keyring Lib
=======================================

%package bin
Summary: bin components for the keyring package.
Group: Binaries

%description bin
bin components for the keyring package.


%package python
Summary: python components for the keyring package.
Group: Default

%description python
python components for the keyring package.


%prep
%setup -q -n keyring-8.5.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py ptr || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keyring

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
