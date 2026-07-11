%global tl_name relsize
%global tl_revision 78315

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.1
Release:	%{tl_revision}.1
Summary:	Set the font size relative to the current font size
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/relsize
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/relsize.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/relsize.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The basic command of the package is \relsize, whose argument is a number
of \magsteps to change size; from this are defined commands \larger,
\smaller, \textlarger, etc.

