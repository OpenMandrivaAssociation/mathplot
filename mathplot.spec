%define	Summary	Interactive function grapher

Summary:	%{Summary}
Name:		mathplot
Version:	0.8.5
Release:	%mkrel 4
License:	GPL
Group:		Sciences/Mathematics
Url:		http://merd.net/pixel/mathplot.html
Source0:	http://merd.net/pixel/%{name}-%{version}.src.tar.bz2
Requires:	tk tcl
BuildRequires:	ocaml >= 3.00 ocamltk XFree86-devel ImageMagick ncurses-devel
BuildRequires:	findlib ocaml-simple_gettext tk tk-devel tcl tcl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
mathplot is a GUI frontend  for  interactive  graphing  of
functions.   mathplot2ps  is  a  batch program to generate
PostScript output.

You can have both equations (y=f(x)  or  f(x,y)=g(x))  and
inequations.  For inequations, mathplot hatches the inter-
section. For example, with y>0, y<x and x<2 it hatches the
solution which is a triangle.
You  can name a point, anywhere or on a function.  You can
ask for the tangent of a function.
As it uses a symbolic library,  you  can  enter  functions
like "x+1/y=2".
Can  find  root (zeros), extrema (even symbolically, some-
times) and intersection of 2 functions.
mathplot exports in PostScript so that you can print  eas-
ily, and with the reference mark (O, i, j).
You  can  save  and  load files. mathplot2ps can transform
these files into PostScript.
It's written in OCaml using the Tk  toolkit  for  the  GUI
frontend

%prep
%setup -q -n %{name}

%build
CFLAGS="%{optflags}" make prefix=/usr

%install
rm -rf %{buildroot}
%makeinstall_std prefix=/usr

%find_lang %{name}

rm -rf %{buildroot}%{_docdir}

install -d %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert icons/mathplot-icon.gif $RPM_BUILD_ROOT%{_miconsdir}/mathplot.png
convert icons/mathplot-icon-large.gif $RPM_BUILD_ROOT%{_iconsdir}/mathplot.png
convert icons/mathplot-icon-mini.gif $RPM_BUILD_ROOT%{_liconsdir}/mathplot.png

install -d %{buildroot}%{_menudir}
install -d %{buildroot}%{_menudir}
cat <<EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}):\
needs="x11"\
section="More Applications/Sciences/Mathematics"\
title="Mathplot"\
longtitle="%{Summary}"\
command="%{name}"\
icon="%{name}.png" \
xdg="true"
EOF


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Mathplot
Comment=%{Summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Science;Math;X-MandrivaLinux-MoreApplications-Sciences-Mathematics;
EOF


%clean
rm -rf %{buildroot}

%post 
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-, root, root)
%doc CHANGES README docs/TODO docs/BUGS
%{_bindir}/*
%{_datadir}/%{name}*
%lang(es) %{_mandir}/es/*/*
%{_mandir}/man*/*
%{_datadir}/applications/*
%{_menudir}/*
%{_iconsdir}/%{name}*
%{_iconsdir}/*/*


