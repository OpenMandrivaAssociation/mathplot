Summary:	Interactive function grapher
Name:		mathplot
Version:	0.8.6
Release:	%mkrel 5
License:	GPLv3+
Group:		Sciences/Mathematics
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		https://rigaux.org/mathplot.html
Source0:	http://rigaux.org/%{name}-%{version}.src.tar.lzma
Requires:	tk
Requires:	tcl
BuildRequires:	ocaml >= 3.00
BuildRequires:	ocaml-labltk
BuildRequires:	X11-devel
BuildRequires:	imagemagick
BuildRequires:	ncurses-devel
BuildRequires:	findlib
BuildRequires:	ocaml-simple_gettext-devel
BuildRequires:	tk
BuildRequires:	tk-devel
BuildRequires:	tcl
BuildRequires:	tcl-devel

%description
mathplot is a GUI frontend for interactive graphing of functions.
mathplot2ps is a batch program to generate PostScript output.

You can have both equations (y=f(x) or f(x,y)=g(x)) and inequations.
For inequations, mathplot hatches the intersection. For example, with
y>0, y<x and x<2 it hatches the solution which is a triangle. You can
name a point, anywhere or on a function. You can ask for the tangent
of a function. As it uses a symbolic library, you can enter functions
like "x+1/y=2". Can find root (zeros), extrema (even symbolically,
sometimes) and intersection of two functions. mathplot exports in
PostScript so that you can print easily, and with the reference mark
(O, i, j). You can save and load files. mathplot2ps can transform
these files into PostScript.
It's written in OCaml using the Tk toolkit for the GUI frontend.

%prep
%setup -q -n %{name}

%build
CFLAGS="%{optflags}" make prefix=%{_prefix}

%install
rm -rf %{buildroot}
%makeinstall_std prefix=%{_prefix}

%find_lang %{name}

rm -rf %{buildroot}%{_docdir}

install -d %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert icons/mathplot-icon.gif %{buildroot}%{_iconsdir}/hicolor/32x32/apps/mathplot.png
convert icons/mathplot-icon-large.gif %{buildroot}%{_iconsdir}/hicolor/48x48/apps/mathplot.png
convert icons/mathplot-icon-mini.gif %{buildroot}%{_iconsdir}/hicolor/16x16/apps/mathplot.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Mathplot
Comment=Interactive function grapher
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Science;Math;
EOF


%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post 
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%files -f %{name}.lang
%defattr(-, root, root)
%doc CHANGES README docs/TODO docs/BUGS
%{_bindir}/*
%{_datadir}/%{name}*
%lang(es) %{_mandir}/es/*/*
%{_mandir}/man*/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*/apps/mathplot.png

