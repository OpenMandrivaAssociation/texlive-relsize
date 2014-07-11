# revision 30707
# category Package
# catalog-ctan /macros/latex/contrib/relsize
# catalog-date 2013-05-27 20:07:27 +0200
# catalog-license pd
# catalog-version 4.1
Name:		texlive-relsize
Version:	4.1
Release:	7
Summary:	Set the font size relative to the current font size
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/relsize
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/relsize.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/relsize.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The basic command of the package is \relsize, whose argument is
a number of \magsteps to change size; from this are defined
commands \larger, \smaller, \textlarger, etc.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/relsize/relsize.sty
%doc %{_texmfdistdir}/doc/latex/relsize/README
%doc %{_texmfdistdir}/doc/latex/relsize/relsize-doc.pdf
%doc %{_texmfdistdir}/doc/latex/relsize/relsize-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
