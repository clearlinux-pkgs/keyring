#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keyring
Version  : 23.2.1
Release  : 106
URL      : https://files.pythonhosted.org/packages/cc/24/c5402ba0c6380cc058980e2b73f0597ab6875692f185054a94244b7161ab/keyring-23.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/cc/24/c5402ba0c6380cc058980e2b73f0597ab6875692f185054a94244b7161ab/keyring-23.2.1.tar.gz
Summary  : Store and access your passwords safely.
Group    : Development/Tools
License  : MIT Python-2.0
Requires: keyring-bin = %{version}-%{release}
Requires: keyring-license = %{version}-%{release}
Requires: keyring-python = %{version}-%{release}
Requires: keyring-python3 = %{version}-%{release}
Requires: importlib_metadata
Requires: jeepney
Requires: secretstorage
BuildRequires : buildreq-distutils3
BuildRequires : jeepney
BuildRequires : secretstorage
BuildRequires : setuptools-python

%description
.. image:: https://img.shields.io/pypi/v/keyring.svg
:target: `PyPI link`_
.. image:: https://img.shields.io/pypi/pyversions/keyring.svg
:target: `PyPI link`_

%package bin
Summary: bin components for the keyring package.
Group: Binaries
Requires: keyring-license = %{version}-%{release}

%description bin
bin components for the keyring package.


%package license
Summary: license components for the keyring package.
Group: Default

%description license
license components for the keyring package.


%package python
Summary: python components for the keyring package.
Group: Default
Requires: keyring-python3 = %{version}-%{release}

%description python
python components for the keyring package.


%package python3
Summary: python3 components for the keyring package.
Group: Default
Requires: python3-core
Provides: pypi(keyring)
Requires: pypi(importlib_metadata)
Requires: pypi(jeepney)
Requires: pypi(secretstorage)

%description python3
python3 components for the keyring package.


%prep
%setup -q -n keyring-23.2.1
cd %{_builddir}/keyring-23.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631546380
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py ptr || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/keyring
cp %{_builddir}/keyring-23.2.1/LICENSE %{buildroot}/usr/share/package-licenses/keyring/8e6689d37f82d5617b7f7f7232c94024d41066d1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keyring

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/keyring/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
