#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keyring
Version  : 11.0.0
Release  : 53
URL      : https://pypi.debian.net/keyring/keyring-11.0.0.tar.gz
Source0  : https://pypi.debian.net/keyring/keyring-11.0.0.tar.gz
Summary  : Store and access your passwords safely.
Group    : Development/Tools
License  : MIT Python-2.0
Requires: keyring-bin
Requires: keyring-python3
Requires: keyring-python
Requires: secretstorage
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-python
BuildRequires : setuptools_scm
Patch1: requires.patch

%description
.. image:: https://img.shields.io/pypi/v/keyring.svg
:target: https://pypi.org/project/keyring

%package bin
Summary: bin components for the keyring package.
Group: Binaries

%description bin
bin components for the keyring package.


%package python
Summary: python components for the keyring package.
Group: Default
Requires: keyring-python3

%description python
python components for the keyring package.


%package python3
Summary: python3 components for the keyring package.
Group: Default
Requires: python3-core

%description python3
python3 components for the keyring package.


%prep
%setup -q -n keyring-11.0.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523555847
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py ptr || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keyring

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
