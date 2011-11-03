# revision 18787
# category Package
# catalog-ctan /macros/latex/contrib/cmsd
# catalog-date 2006-12-18 23:50:36 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-cmsd
Version:	20061218
Release:	1
Summary:	Interfaces to the CM Sans Serif Bold fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cmsd
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmsd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmsd.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Thr purpose of the package is to provide an alternative
interface to the CM Sans Serif boldface fonts. The EC (T1,
Cork) encoded versions of the 'CM Sans Serif boldface extended'
fonts differ considerably from the traditionally (OT1) encoded
ones: at large sizes, >10pt, they have thinner strokes and are
much wider. At 25pt they are hardly to be recognized as being
'boldface'. This package attempts to make these T1 fonts look
like the traditional ones did. You do not need any new fonts;
the package just changes the way LaTeX makes use of the current
ones.

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
%{_texmfdistdir}/tex/latex/cmsd/cmsd.sty
%{_texmfdistdir}/tex/latex/cmsd/t1cmsd.fd
%{_texmfdistdir}/tex/latex/cmsd/ts1cmsd.fd
%doc %{_texmfdistdir}/doc/latex/cmsd/liesmich
%doc %{_texmfdistdir}/doc/latex/cmsd/readme
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
