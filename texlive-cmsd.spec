%global tl_name cmsd
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Interfaces to the CM Sans Serif Bold fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cmsd
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmsd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmsd.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Thr purpose of the package is to provide an alternative interface to the
CM Sans Serif boldface fonts. The EC (T1, Cork) encoded versions of the
'CM Sans Serif boldface extended' fonts differ considerably from the
traditionally (OT1) encoded ones: at large sizes, >10pt, they have
thinner strokes and are much wider. At 25pt they are hardly to be
recognized as being 'boldface'. This package attempts to make these T1
fonts look like the traditional ones did. You do not need any new fonts;
the package just changes the way LaTeX makes use of the current ones.

