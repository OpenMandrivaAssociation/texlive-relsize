# revision 24074
# category Package
# catalog-ctan /macros/latex/contrib/relsize
# catalog-date 2011-09-23 08:29:05 +0200
# catalog-license pd
# catalog-version 4
Name:		texlive-relsize
Version:	4
Release:	1
Summary:	Set the font size relative to the current font size
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/relsize
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/relsize.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/relsize.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The basic command of the package is \relsize, whose argument is
a number of \magsteps to change size; from this are defined
commands \larger, \smaller, \textlarger, etc.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/relsize/relsize.sty
%doc %{_texmfdistdir}/doc/latex/relsize/README
%doc %{_texmfdistdir}/doc/latex/relsize/relsize-doc.pdf
%doc %{_texmfdistdir}/doc/latex/relsize/relsize-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
