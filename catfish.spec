Summary:	A handy file search tool
Name:		catfish
Version:	4.16.3
Release:	2
Group:		File tools
License:	GPLv2+
Url:		http://twotoasts.de/index.php/catfish
Source0:	http://archive.xfce.org/src/apps/catfish/4.16/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	python-devel
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	python3dist(python-distutils-extra)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3dist(pygobject)
Requires:	python-pyxdg
Requires:	python-dbus
Requires:	mlocate
Requires:	findutils

%description
A handy file searching tool for linux. Basically it is a
frontend for different search engines (daemons) which
provides a unified interface. The interface is intentionally
lightweight and simple, using only GTK+ 3. You can configure
it to your needs by using several command line options.

%prep
%setup -q

%build
%py_build

%install
CFLAGS="%{optflags}" %__python3 setup.py install -O1 --root %{buildroot}

desktop-file-install \
	--remove-category="Utility" \
	--add-category='System' \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

# handle docs in files section
rm -rf %{buildroot}%{_docdir}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README*
%{_bindir}/%{name}
%{_datadir}/applications/org.xfce.Catfish.desktop
%{_datadir}/metainfo/catfish.appdata.xml
%{_datadir}/%{name}/
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_mandir}/man1/%{name}.1*
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}_lib/
%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info
%{_iconsdir}/hicolor/*x*/apps/org.xfce.catfish.*
