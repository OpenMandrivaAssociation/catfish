Summary:	A handy file search tool
Name:		catfish
Version:	0.3
Release:	%mkrel 5
Group:		File tools
License:	GPLv2+
URL:		http://software.twotoasts.de/?page=%{name}
Source0:	http://software.twotoasts.de/media/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.3-fix-separator-position.patch
BuildRequires:	gettext
BuildRequires:	desktop-file-install
%py_requires -d
Requires:	pygtk2.0-libglade
Requires:	pyxdg
Requires:	dbus-python
Requires:	mlocate
Requires:	findutils
Suggests:	beagle
BuildArch:	noarch

%description
A handy file searching tool for linux. Basically it is a 
frontend for different search engines (daemons) which 
provides a unified interface. The interface is intentionally 
lightweight and simple, using only GTK+ 2. You can configure 
it to your needs by using several command line options.

%prep
%setup -q
%patch0 -p1

%build
sed -i.misc \
	-e '/svg/s|install|install -m 644|' \
	-e '/glade/s|install| install -m 644|' \
	-e 's|install |install -p |' \
	-e 's|pyc|py|' \
	-e 's|^\([ \t]*\)ln |\1: ln |' \
	-e 's|cp -rf|cp -prf|' \
	Makefile.in

sed -i.byte -e 's|pyc|py|' %{name}.in

sed -i.engine -e 's|Nautilus|nautilus|' %{name}.py

# (tpg) do not use macro here
./configure --prefix=%{_prefix}

%install
rm -rf %{buildroot}

%makeinstall_std

desktop-file-install \
	--remove-category="Utility" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

rm -rf %{buildroot}%{_datadir}/doc/

ln -sf ../pixmaps/%{name}.svg %{buildroot}%{_datadir}/%{name}/
ln -sf ../locale/ %{buildroot}%{_datadir}/%{name}/

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.svg
