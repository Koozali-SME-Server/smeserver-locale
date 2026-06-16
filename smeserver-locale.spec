# $Id: smeserver-locale.spec,v 1.19 2022/11/11 16:35:21 jpp Exp $

Summary: SME Server localisation module
%define name smeserver-locale
Name: %{name}
%define version 11.0.0
%define release 4
%define package_summary SME Server localisation module
%define group Applications/System
%define package_locales bg da de el es et fr he hu id it ja nb nl pl pt pt_BR ro ru sl sv th tr zh_CN zh_TW
Version: %{version}
Release: %{release}%{?dist}
License: GPL2.0
Group: Networking/Daemons
Source: %{name}-%{version}.tar.xz

BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
BuildRequires: perl
BuildRequires: smeserver-devtools >= 1.13.1-03
BuildRequires: gettext
AutoReqProv: no

%description
SME Server localisation module

%changelog
* Thu Aug 08 2024 Jean-Philippe Pialasse <jpp@koozali.org> 11.0.0-4.sme
- apply locale 2024-08-08.patch [SME: 12717]

* Thu Apr 04 2024 Brian Read <brianr@koozali.org> 11.0.0-3.sme
- Set license file to GPL2.0  [SME: 12577]

* Sat Mar 23 2024 Brian Read <brianr@koozali.org>11.0.0-2.sme
- Change Requires: e-smith- to Requires:smeserver-

* Sat Mar 23 2024 Brian Read <brianr@koozali.org>11.0.0-1.sme
- Update Release and Version to base version and 1st release for SME11 [SME: 12518]

* Mon Jul 10 2023 cvs2git.sh aka Brian Read <brianr@koozali.org> 2.6.0-18.sme
- Roll up patches and move to git repo [SME: 12338]

* Mon Jul 10 2023 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.

* Fri Nov 11 2022 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-17.sme
- apply local 2022-11-11.patch [SME: 12220]

* Wed Jul 20 2022 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-16.sme
- apply local 2022-07-21.patch [SME: 12117]

* Sun Jun 06 2021 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-15.sme
- apply local 2021-06-06.patch  [SME: 11593]

* Wed May 12 2021 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-14.sme
- apply local 2021-05-12.patch  [SME: 11593]

* Fri Jan 08 2021 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-13.sme
- apply local 2021-01-09.patch [SME: 11310]

* Fri Dec 06 2019 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-12.sme
- apply local 2019-12-07.patch

* Fri Dec 14 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 2.6.0-11.sme
- apply locale 2018-12-14 patch

* Sat Dec 02 2017 SME Translation Server <translations@contribs.org> 2.6.0-10.sme
- apply locale 2017-12-02 patch

* Wed Apr 26 2017 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-9.sme
- apply 2017-04-26 translation patch [SME: 10252]

* Fri Mar 03 2017 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-8.sme
- updated donate patch to correct location https://wiki.koozali.org/Donate [SME: 9595]
- applied smeserver-locale-2.6.0-locale-2017-03-03

* Sun Jul 17 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 2.6.0-6.sme
- Added translations smeserver-locale-2.6.0-locale-2016-07-17.patch

* Sun Jul 17 2016 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-5.sme
- fix wrongly converted http to https in
- URL starting with http:// or ftp://

* Wed Jun 15 2016 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-4.sme
- fix path to documentations (wiki) [SME: 9595]
- convert all koozali url to https

* Wed Jun 15 2016 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-3.sme
- change http://www.smeserver.org\donate to https://wiki.koozali.org/donate  [SME: 9595]
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.
  Mon Oct 15 2005 --> Mon Oct 10 2005 or Sat Oct 15 2005 or Mon Oct 17 2005 or ....
  Wed Oct 30 2005 --> Wed Oct 26 2005 or Sun Oct 30 2005 or Wed Nov 02 2005 or ....
  Wed Dec 15 2005 --> Wed Dec 14 2005 or Thu Dec 15 2005 or Wed Dec 21 2005 or ....
  Wed Mar 16 2006 --> Wed Mar 15 2006 or Thu Mar 16 2006 or Wed Mar 22 2006 or ....
  Thu Oct 17 2008 --> Thu Oct 16 2008 or Fri Oct 17 2008 or Thu Oct 23 2008 or ....
  Tue Nov 19 2008 --> Tue Nov 18 2008 or Wed Nov 19 2008 or Tue Nov 25 2008 or ....
  Wed Dec 25 2014 --> Wed Dec 24 2014 or Thu Dec 25 2014 or Wed Dec 31 2014 or ....


* Wed Jun 15 2016 Jean-Philippe Pialasse <tests@pialasse.com> 2.6.0-2.sme
- change contribs.org to koozali.org  [SME: 9595]

* Sat Feb 06 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 2.6.0-1.sme
- Initial release to sme10

* Thu Jul 2 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> 2.4.0-22.el6.sme
- apply locale smeserver-locale-2.4.0-locale-2015-07-12.patch [SME: 8842]

* Thu Jul 2 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> 2.4.0-21.el6.sme
- apply locale smeserver-locale-2.4.0-locale-2015-07-01.patch [SME: 8969]

* Sat Mar 14 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> 2.4.0-20.el6.sme
- apply locale 2015-03-14 patch from pootle [SME: 8872]

* Thu Dec 25 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> 2.4.0-19.el6.sme
  Wed Dec 25 2014 --> Wed Dec 24 2014 or Thu Dec 25 2014 or Wed Dec 31 2014 or ....
- apply locale 2014-12-25 patch from pootle [SME: 8743]

* Wed Jun 4 2014 Ian Wells <esmith@wellsi.com> 2.4.0-15.el6.sme
- apply locale 2014-06-04 patch from pootle [SME: 8402]

* Sun Apr 27 2014 Ian Wells <esmith@wellsi.com> 2.4.0-14.el6.sme
- apply locale 2014-04-27 patch from pootle [SME: 8295]

* Sun Mar 23 2014 Ian Wells <esmith@wellsi.com> 2.4.0-13.el6.sme
- apply locale 2014-03-23 patch from pootle [SME: 8176]

* Sat Mar 8 2014 Ian Wells <esmith@wellsi.com> 2.4.0-12.el6.sme
- apply locale 2014-03-08 patch from pootle [SME: 7893]

* Sat Mar 1 2014 Ian Wells <esmith@wellsi.com> 2.4.0-11.el6.sme
- apply locale 2014-03-01 patch from pootle [SME: 8176]

* Tue Dec 24 2013 Ian Wells <esmith@wellsi.com> 2.4.0-10.el6.sme
- Correctly apply locale 2013-12-24 patch from pootle [SME: 8029]

* Tue Dec 24 2013 Ian Wells <esmith@wellsi.com> 2.4.0-9.el6.sme
- apply locale 2013-12-24 patch from pootle [SME: 8029]

* Mon Dec 2 2013 Ian Wells <esmith@wellsi.com> 2.4.0-8.el6.sme
- apply locale 2013-12-02 patch from pootle [SME: 8029]

* Sun Nov 3 2013 Ian Wells <esmith@wellsi.com> 2.4.0-7.el6.sme
- apply locale 2013-11-03 patch from pootle [SME: 7971]

* Mon Oct 07 2013 Ian Wells <esmith@wellsi.com> 2.4.0-6.el6.sme
- apply locale 2013-10-07 patch from pootle [SME: 7878]

* Sat Sep 14 2013 Ian Wells <esmith@wellsi.com> 2.4.0-5.el6.sme
- apply locale 2013-09-14 patch from pootle [SME: 7848]

* Mon Mar 11 2013 Shad L. Lords <slords@mail.com> 2.4.0-4.el6
- Obsolete el5 version of aspell module [SME: 7273]

* Thu Jan 31 2013 Shad L. Lords <slords@mail.com> 2.4.0-2.el6
- Replace aspell dictionaries with hunspell dictionaries

* Thu Jan 31 2013 Shad L. Lords <slords@mail.com> 2.4.0-1.el6
- Roll new stream for sme9

* Tue Mar 20 2012 SME Translation Server <translations@contribs.org> 2.2.0-41.el6
- apply locale 2012-03-20 patch

* Wed Nov 23 2011 SME Translation Server <translations@contribs.org> 2.2.0-40.el6
- apply locale 2011-11-23 patch

* Tue Oct 04 2011 SME Translation Server <translations@contribs.org> 2.2.0-39.el6
- apply locale 2011-10-04 patch

* Mon Jun 20 2011 SME Translation Server <translations@contribs.org> 2.2.0-38.el6
- apply locale 2011-06-20 patch

* Wed Apr 27 2011 SME Translation Server <translations@contribs.org> 2.2.0-37.sme
- apply locale 2011-04-27 patch

* Sun Mar 06 2011 SME Translation Server <translations@contribs.org> 2.2.0-36.sme
- apply locale 2011-03-06 patch

* Fri Oct 08 2010 SME Translation Server <translations@contribs.org> 2.2.0-35.sme
- apply locale 2010-10-08 patch

* Wed Aug 18 2010 SME Translation Server <translations@contribs.org> 2.2.0-34.sme
- apply locale 2010-08-18 patch

* Tue Jul 13 2010 SME Translation Server <translations@contribs.org> 2.2.0-33.sme
- Add Chinese (Taiwan) language [SME: 6106]
- apply locale 2010-07-13 patch

* Thu Jun 24 2010 SME Translation Server <translations@contribs.org> 2.2.0-32.sme
- apply locale 2010-06-24 patch

* Tue Jun 08 2010 SME Translation Server <translations@contribs.org> 2.2.0-31.sme
- apply locale 2010-06-08 patch

* Tue May 25 2010 Shad L. Lords <slords@mail.com> - 2.2.0-30.sme
- Add Hebrew language [SME: 5971]

* Sun May 23 2010 SME Translation Server <translations@contribs.org> 2.2.0-29.sme
- apply locale 2010-05-23 patch

* Thu Apr 29 2010 SME Translation Server <translations@contribs.org> 2.2.0-28.sme
- apply locale 2010-04-29 patch

* Tue Mar 02 2010 SME Translation Server <translations@contribs.org> 2.2.0-27.sme
- apply locale 2010-03-02 patch

* Sat Feb 27 2010 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-26.sme
- Revert previous patch to resync with generated patches based on SME Server 7 [SME: 5803]
- Correct previous changelog entry
- Apply locale 2010-02-27 patch

* Thu Feb 25 2010 Filippo Carletti <filippo.carletti@gmail.com> 2.2.0-25.sme
- apply locale 2010-02-25 patch

* Tue Oct 27 2009 SME Translation Server <translations@contribs.org> 2.2.0-24.sme
- apply locale 2009-10-27 patch
- Add Thai language [SME: 5466]

* Mon Aug 24 2009 SME Translation Server <translations@contribs.org> 2.2.0-23.sme
- apply locale 2009-08-24 patch
- Add Polish language [SME: 5437]

* Wed May 27 2009 SME Translation Server <translations@contribs.org> 2.2.0-22.sme
- apply locale 2009-05-27 patch
- Add Romanian language [SME: 5268]

* Wed May 20 2009 SME Translation Server <translations@contribs.org> 2.2.0-21.sme
- apply locale 2009-05-20 patch

* Mon Apr 27 2009 SME Translation Server <translations@contribs.org> 2.2.0-20.sme
- apply locale 2009-04-27 patch
- Add Estonian language [SME: 5199]

* Tue Mar 03 2009 SME Translation Server
- re-apply locale 2009-03-03 patch

* Tue Mar  3 2009 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-18.sme
- Apply  3 Mar 2009 locale patch [SME: 5051]

* Sun Mar  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-17.sme
- Apply  1 Mar 2009 locale patch [SME: 5017]
- Added missing bug references to changelog entry [SME: 5002]

* Mon Feb 09 2009 Shad L. Lords <slords@mail.com> - 2.2.0-16.sme
- Add Chineese (China) language [SME: 5002]
- Add Norwegian (Bokmal) language [SME: 5002]
- Add Russian language [SME: 5002]

* Sat Jan 31 2009 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-15.sme
- Apply 31 Jan 2009 locale patch [SME: 4950]

* Wed Dec 31 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-14.sme
- Apply 31 Dec 2008 locale patch [SME: 4899]

* Sun Nov 30 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-13.sme
- Apply 30 Nov 2008 locale patch [SME: 4813]

* Wed Nov 19 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-12.sme
  Tue Nov 19 2008 --> Tue Nov 18 2008 or Wed Nov 19 2008 or Tue Nov 25 2008 or ....
- Apply 19 Nov 2008 locale patch [SME: 4748]

* Tue Nov 18 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-11.sme
- Apply 18 Nov 2008 locale patch [SME: 4748]

* Fri Nov  7 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-10.sme
- Apply  7 Nov 2008 locale patch [SME: 4748]

* Thu Nov  6 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-9.sme
- Apply  6 Nov 2008 locale patch [SME: 4746]

* Sun Nov 2 2008 Shad L. Lords <slords@mail.com> - 2.2.0-8.sme
- Apply 2 Nov 2008 locale patch

* Mon Oct 20 2008 Stephen Noble <support@dungog.net> - 2.2.0-7.sme
- Apply 19 Oct 2008 locale patch [SME: 4692]

* Fri Oct 17 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-6.sme
  Thu Oct 17 2008 --> Thu Oct 16 2008 or Fri Oct 17 2008 or Thu Oct 23 2008 or ....
- Apply 17 Oct 2008 locale patch

* Thu Oct 16 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-5.sme
- Apply 16 Oct 2008 locale patch

* Wed Oct 15 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-4.sme
- Apply 15 Oct 2008 locale patch

* Mon Oct 13 2008 Shad L. Lords <slords@mail.com> - 2.2.0-3.sme
- Add Japanese language [SME: 4637]

* Wed Oct 8 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 2.2.0-2.sme
- Apply Oct 8 locale patch, fixing last colored highlight from German locale [SME 4618]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Sat Oct 4 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 1.4.0-20
- Reverting all changes made Oct 4, as they should be made through Pootle
- Applying Pootle patch, fixing [SME: 4618] and [SME: 4616]

* Sat Oct 4 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 1.4.0-19
- Apply 4 Oct locale patch

* Sat Oct 4 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 1.4.0-18
- Remove colored highlights from German locale [SME: 4618]
- Fix changelog entry in previous entry for [SME: 4616]

* Sat Oct 4 2008 Jonathan Martens <smeserver-contribs@snetram.nl> - 1.4.0-17
- Remove references to the wiki from the German locale [SME: 4616]
- Fix bug referrence in previous changelog entry [SME: 4617]

* Fri Oct 3 2008 Shad L. Lords <slords@mail.com> - 1.4.0-16
- Apply locale patch to fix many translation bugs [SME: 4615]

* Tue Sep 30 2008 Stephen Noble <support@dungog.net> - 1.4.0-15
- Apply locale patch

* Sat Sep 27 2008 Stephen Noble <support@dungog.net> - 1.4.0-14
- Apply locale patch

* Sat Jul 26 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-13
- Apply Jul 26 2008 locale patch
- Add Portuguese language
- Add Turkish language

* Tue Jul 1 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-12
- Apply 1 July 2008 locale patch

* Fri Jun 27 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-11
- Apply 27 Jun 2008 locale patch

* Mon May 5 2008 Shad L. Lords <slords@mail.com> 1.4.0-10
- Update to May 5 2008 translations
- Revert Apr 23 2008 translations (bad patch)

* Wed Apr 23 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.4.0-9
- Update to Apr 23 2008 translations

* Tue Apr 1 2008 Shad L. Lords <slords@mail.com> 1.4.0-8
- Update to Apr 1 2008 translations

* Wed Mar 26 2008 Shad L. Lords <slords@mail.com> 1.4.0-7
- Update to Mar 26 2008 translations

* Tue Mar 25 2008 Shad L. Lords <slords@mail.com> 1.4.0-6
- Update to Mar 25 2008 translations

* Tue Mar 18 2008 Shad L. Lords <slords@mail.com> 1.4.0-5
- Fix packages for Brazilian portuguese
- Update to Mar 18 2008 translations

* Tue Mar 11 2008 Shad L. Lords <slords@mail.com> 1.4.0-4
- Move requires e-smith-formmagick to correct places [SME: 3858]
- Add missing aspell module requires

* Mon Mar 10 2008 Shad L. Lords <slords@mail.com> 1.4.0-3
- Fix requires to require e-smith-formmagick [SME: 3858]

* Mon Mar 10 2008 Shad L. Lords <slords@mail.com> 1.4.0-2
- Convert panels to UTF-8 [SME: 3858]

* Fri Mar 7 2008 Shad L. Lords <slords@mail.com> 1.4.0-1
- Roll new stream and considate patches

* Wed Mar 05 2008 Stephen Noble <support@dungog.net> 1.2.0-58
- fix conversions for tags with CDATA or marked fuzzy [SME: 4014]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-57
- add translations for Brazilian portuguese [SME: 63]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-56
- add translations for Slovian    [SME: 892]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-55
- add translations for Dutch      [SME: 2737]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-54
- add translations for Indonesian [SME: 3260]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-53
- add translations for Greek      [SME: 1690]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-52
- add translations for Danish     [SME: 2688]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-51
- update translations for Swedish [SME: 3934]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-50
- update translations for Spanish [SME: 3937]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-49
- update translations for Italian [SME: 3936]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-48
- update translations for French  [SME: 3935]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-47
- update translations for German  [SME: 3933]

* Sun Feb 17 2008 Stephen Noble <support@dungog.net> 1.2.0-46
- update po files, include script to recreate, in .src.rpm only [SME: 3833]

* Fri Feb 15 2008 Stephen Noble <support@dungog.net> 1.2.0-45
- rename de and it quota .po files with .tmpl [SME: 3834]

* Sat Feb 09 2008 Stephen Noble <support@dungog.net> 1.2.0-44
- Remove redundant germam lexicon reinstall [SME: 3881]

* Thu Jan 31 2008 Stephen Noble <support@dungog.net> 1.2.0-43
- Fix fr translation for smtp header in email panels. [SME: 3831]

* Sat Jan 26 2008 Gavin Weight <gweight@gmail.com> 1.2.0-42
- Update de, es, fr and sv translations for yum panel. [SME: 2090]

* Sat Jan 26 2008 Gavin Weight <gweight@gmail.com> 1.2.0-41
- Update de, fr and sv translations for smtp header in email panels. [SME: 2305]

* Sat Jan 26 2008 Gavin Weight <gweight@gmail.com> 1.2.0-40
- Update de, es, fr and sv translations for email panels. [SME: 2296]

* Mon Jan 21 2008 Filippo Carletti <filippo.carletti@gmail.com> 1.2.0-39
- Italian update for SMTP server [SME: 2305]

* Mon Jan 21 2008 Filippo Carletti <filippo.carletti@gmail.com> 1.2.0-38
- Italian translations for yum and email panels [SME: 2090] [SME: 2296]

* Sat Jan 19 2008 Stephen Noble <support@dungog.net> 1.2.0-37
- Add SSH_PORT for sv [SME: 3748]

* Sat Jan 19 2008 Stephen Noble <support@dungog.net> 1.2.0-36
- System password change made consistant [SME: 3533]

* Sat Jan 19 2008 Stephen Noble <support@dungog.net> 1.2.0-35
- Add Add Italian entries to hostentries [SME: 3207]

* Sat Jan 19 2008 Stephen Noble <support@dungog.net> 1.2.0-34
- Add yum uptodate message [SME: 3768]

* Mon Jan 14 2008 Gavin Weight <gweight@gmail.com> 1.2.0-33
- Update Spanish translation for panels. (Thanks Normando Hall) [SME: 3751]

* Sat Jan 12 2008 Gavin Weight <gweight@gmail.com> 1.2.0-32
- Add SSH_PORT spanish translation update. [SME: 3746]

* Mon Jan 7 2008 Stephen Noble <support@dungog.net> 1.2.0-31
- Add SSH_PORT for fr and de [SME: 3215]

* Fri Oct 19 2007 Gavin Weight <gweight@gmail.com> 1.2.0-30
- Adjust italian success text when changing admin pass. (Thanks Filippo) [SME: 3473]

* Thu Oct 18 2007 Gavin Weight <gweight@gmail.com> 1.2.0-29
- Add missing localization again. (Thanks Federico). [SME: 3149]

* Wed Oct 10 2007 Charlie Brady <charlie_brady@mitel.com>
- Add missing localization (Thanks Federico). [SME: 3149]

* Fri Jun 15 2007 Stephen Noble <support@dungog.net> 1.2.0-27
- Update French clamav lexicon [SME: 3012]

* Thu Jun 14 2007 Gavin Weight <gweight@gmail.com> 1.2.0-26
- Updated stand by text in bootstrap-console Translation. (Thanks Federico) [SME: 2937]

* Thu Jun 14 2007 Gavin Weight <gweight@gmail.com> 1.2.0-25
- Updated backupusb console Translation. (Thanks Federico) [SME: 2937]

* Tue Jun 12 2007 Gavin Weight <gweight@gmail.com> 1.2.0-24
- More Updated Spanish Translations. (Thanks Normando) [SME: 2287] 

* Sat May 05 2007 Gavin Weight <gweight@gmail.com> 1.2.0-23
- Updated German Translations. (Thanks Dietmar ) [SME: 711] 

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Sat Apr 07 2007 Gavin Weight <gweight@gmail.com> 1.2.0-22
- Updated German Translations/Console. (Thanks Dietmar ) [SME: 711] 

* Fri Mar 02 2007 Gavin Weight <gweight@gmail.com> 1.2.0-21
- Updated Spanish Translations. (Thanks Normando) [SME: 2501] 

* Sun Feb 11 2007 Stephen Noble <support@dungog.net> 1.2.0-20
- Updated Spanish Translations. (Thanks Normando) [SME: 2287] 

* Sun Feb 11 2007 Gavin Weight <gweight@gmail.com> 1.2.0-19
- New Swedish Translations for console. (Thanks Chrille). [SME: 911]

* Sun Feb 11 2007 Stephen Noble <support@dungog.net> 1.2.0-18
- Remove references to virtual from sv,it,fr panels [SME: 2297]

* Tue Feb 06 2007 Gavin Weight <gweight@gmail.com> 1.2.0-17
- New Swedish Translations for server-manager (Thanks Chrille). [SME: 911]

* Sat Jan 13 2007 Shad L. Lords <slords@mail.com> 1.2.0-16
- Remove references to virtual from panels [SME: 1517]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Fri Jun 30 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-15
- Update French translation - Merci Franck Pierre [SME: 1659]

* Fri Jun 30 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-14
- Change donate link to www.smeserver.org/donate/ [SME: 1668]

* Fri Jun 30 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-13
- Change new window target to _blank rather than "new" [SME: 1613]

* Wed Jun 28 2006 Gavin Weight <gweight@gmail.com> 1.2.0-12
- German and Italian text on server-manager front screen updated. [SME: 1659]

* Tue Jun 27 2006 Filippo Carletti <carletti@mobilia.it> 1.2.0-11
- Updated italian translations [SME: 1119]

* Sat Jun 10 2006 Franck Pierre <grand-pa@grand-pa.dyndns.org> 1.2.0-10
- Updated French translations [SME: 1001]

* Mon May 22 2006 Gavin Weight <gweight@gmail.com> 1.2.0-09
- Updated German translation. Thanks Dietmar Berteld. [SME: 1412]

* Tue May 16 2006 Gavin Weight <gweight@gmail.com> 1.2.0-08
- Updated Spanish emailsettings. Thanks Ernesto Lorenz [SME: 1435]

* Mon May 15 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-07
- Bump release number only

* Sun May 14 2006 Gavin Weight <gweight@gmail.com> 1.2.0-06sme01
- Updated German translations. Thanks Dietmar Berteld. [SME: 1412]

* Sun Apr 9 2006 Franck Pierre <grand-pa@grand-pa.dyndns.org> 1.2.0-05
- Updated French translations [SME: 263]

* Thu Apr 6 2006 Gavin Weight <gweight@gmail.com> 1.2.0-04
- Changed online-manual location to contribs.org in es lang. [SME: 1079]

* Thu Apr 6 2006 Gavin Weight <gweight@gmail.com> 1.2.0-03
- Changed online-manual location to contribs.org. [SME: 1079]

* Wed Mar 22 2006 Filippo Carletti <carletti@mobilia.it> 1.2.0-02
- Updated italian translations [SME: 1119]

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-01
- Roll stable stream version. [SME: 1016]

* Thu Mar 16 2006 Franck Pierre <grand-pa@grand-pa.dyndns.org> 1.0.1-12
  Wed Mar 16 2006 --> Wed Mar 15 2006 or Thu Mar 16 2006 or Wed Mar 22 2006 or ....
- Update French translations [SME: 263]

* Tue Feb 21 2006 Gavin Weight <gweight@gmail.com> 1.0.1-11
- Add loop to run dos2unix before validating lexicon files.

* Mon Feb 20 2006 Gavin Weight <gweight@gmail.com> 1.0.1-10
- New German translations (Thanks Dietmar Berteld) [SME: 823]

* Wed Feb 15 2006 Franck Pierre <grand-pa@grand-pa.dyndns.org> 1.0.1-09
- Add some French translations [SME: 263]

* Mon Feb 13 2006 Gavin Weight <gweight@gmail.com> 1.0.1-08
- Fixed German (de) domains panel (Thanks Philipp Walker) [SME: 672]

* Fri Feb 3 2006 Franck Pierre <grand-pa@grand-pa.dyndns.org> 1.0.1-07
- French translations [SME: 263]

* Mon Jan 9 2006 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-06
- Copied English emailsettings lexicon to Spanish so the panel at
  least works when browsing in Spanish [SME: 386]

* Thu Dec 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-05
  Wed Dec 15 2005 --> Wed Dec 14 2005 or Thu Dec 15 2005 or Wed Dec 21 2005 or ....
- French console translations [SME: 181]

* Thu Dec 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-04
  Wed Dec 15 2005 --> Wed Dec 14 2005 or Thu Dec 15 2005 or Wed Dec 21 2005 or ....
- French fixup for FormMagick/general [SME: 180]

* Mon Dec 05 2005 Filippo Carletti <carletti@mobilia.it> 1.0.1-03
- Change some too long italian translations [SME: 273]

* Sun Oct 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-02
  Wed Oct 30 2005 --> Wed Oct 26 2005 or Sun Oct 30 2005 or Wed Nov 02 2005 or ....
- Change 'standby' to 'stand by' in console [SME: 66]

* Sun Oct 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-01
  Wed Oct 30 2005 --> Wed Oct 26 2005 or Sun Oct 30 2005 or Wed Nov 02 2005 or ....
- Roll patches up to 1.0.0-12
- Convert all DOS format files to Unix format to ease patching [SME: 66]

* Sat Oct 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-12
  Mon Oct 15 2005 --> Mon Oct 10 2005 or Sat Oct 15 2005 or Mon Oct 17 2005 or ....
- Plus encore [SF: 1265560]

* Sat Oct 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-11
  Mon Oct 15 2005 --> Mon Oct 10 2005 or Sat Oct 15 2005 or Mon Oct 17 2005 or ....
- Revise French on review panel [SF: 1293855]

* Sat Oct 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-11
  Mon Oct 15 2005 --> Mon Oct 10 2005 or Sat Oct 15 2005 or Mon Oct 17 2005 or ....
- Add defattr definition to each sub-package [SF: 1296531]
- Remove fr-ca to fr relocation - it can stay in e-smith-base, or
  even get removed entirely. It's for 5.6 -> 6.0 upgrades in any case.

* Sat Oct 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-10
  Mon Oct 15 2005 --> Mon Oct 10 2005 or Sat Oct 15 2005 or Mon Oct 17 2005 or ....
- Add aspell-$locale as dependencies of the various locales [SF: 1296531]

* Sat Oct 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-09
- Initial work on generating separate locale packages [SF: 1309520]
- Do we really want to generate around 80 one to seven file packages? 
  I don't think so - it may be "correct", but it's really ugly

* Sat Oct 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-08
- Spec file cleanup [SF: 1309520]
- TODO: Generate locale packages to match base packages.

* Sat Oct 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-07
- Ensure zero exit status from fr pre scriptlet [SF: 1309520]
- TODO: Do we need this any more - IIRC it's for 5.5 -> 6.0
  It is also in e-smith-base, and should be removed from there

* Sat Oct 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-06
- Fix up bug references in changelog (no code change) [SF: 1309520]

* Fri Oct 14 2005 Filippo Carletti <carletti@mobilia.it> 1.0.0-05
- Italian updates

* Mon Oct 3 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-04
- Don't generate the parent (combined) package, just the sub-packages
- Remove en_US/en-us files from install tree. They are just here for
  translation convenience and to provide a comparison with the
  relevant base packages (TODO: Decide whether to delete them) [SF: 1309520]

* Sat Oct 1 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-03
- Added missing po files (new tarball) [SF: 1309520]

* Sat Oct 1 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-02
- Fixup in Italian FormMagick/general (new tarball) [SF: 1309520]

* Sat Oct 1 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-01
- Repackaging of all L10Ns except en-us in one RPM. en-us L10Ns live
  in the base packages. All languages are stored in the single source
  RPM, but a separate binary RPM is generated per language. [SF: 1309520]

%prep
%setup

%build
LEXICONS=$(find root/etc/e-smith/locale -type f)
for file in $LEXICONS
do
    /sbin/e-smith/validate-lexicon $file
done

for dir in root/etc/e-smith/locale/*
do
    ln -s initial.cgi $dir/etc/e-smith/web/functions/index.cgi
done

/sbin/e-smith/generate-lexicons

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist

for locale in %{package_locales}
do
    echo "%defattr(-,root,root)" > \
	%{name}-%{version}-%{release}-filelist-$locale

    grep -e locale/$locale/ -e locale/$(echo $locale | tr '[:upper:]_' '[:lower:]-')/ \
         %{name}-%{version}-%{release}-filelist >> %{name}-%{version}-%{release}-filelist-$locale
done

%clean 
rm -rf $RPM_BUILD_ROOT

%package bg
Summary: %{package_summary} - Bulgarian
Group: %{group}
Requires: hunspell-bg
Obsoletes: aspell-bg <= 50:0.50
Requires: smeserver-formmagick >= 1.4.0-10
%description bg
%{summary}
%files bg -f %{name}-%{version}-%{release}-filelist-bg

%package da
Summary: %{package_summary} - Danish
Group: %{group}
Requires: hunspell-da
Obsoletes: aspell-da <= 50:0.50
Requires: smeserver-formmagick >= 1.4.0-10
%description da
%{summary}
%files da -f %{name}-%{version}-%{release}-filelist-da

%package de
Summary: %{package_summary} - German
Group: %{group}
Requires: hunspell-de
Obsoletes: aspell-de <= 50:0.50
Requires: smeserver-formmagick >= 1.4.0-10
%description de
%{summary}
%files de -f %{name}-%{version}-%{release}-filelist-de

%package el
Summary: %{package_summary} - Greek
Group: %{group}
Requires: hunspell-el
Obsoletes: aspell-el <= 50:0.50
Requires: smeserver-formmagick >= 1.4.0-10
%description el
%{summary}
%files el -f %{name}-%{version}-%{release}-filelist-el

%package es
Summary: %{package_summary} - Spanish
Group: %{group}
Requires: hunspell-es
Obsoletes: aspell-es <= 50:0.50
Requires: smeserver-formmagick >= 1.4.0-10
%description es
%{summary}
%files es -f %{name}-%{version}-%{release}-filelist-es

%package et
Summary: %{package_summary} - Estonian
Group: %{group}
Requires: hunspell-et
Requires: smeserver-formmagick >= 1.4.0-10
%description et
%{summary}
%files et -f %{name}-%{version}-%{release}-filelist-et

%package fr
Summary: %{package_summary} - French
Group: %{group}
Requires: hunspell-fr
Obsoletes: aspell-fr <= 50:0.50
Requires: smeserver-formmagick >= 1.4.0-10
%description fr
%{summary}
%files fr -f %{name}-%{version}-%{release}-filelist-fr

%package he
Summary: %{package_summary} - Hebrew
Group: %{group}
Requires: hunspell-he
Requires: smeserver-formmagick >= 1.4.0-10
%description he
%{summary}
%files he -f %{name}-%{version}-%{release}-filelist-he

%package hu
Summary: %{package_summary} - Hungarian
Group: %{group}
Requires: hunspell-hu
Requires: smeserver-formmagick >= 1.4.0-10
%description hu
%{summary}
%files hu -f %{name}-%{version}-%{release}-filelist-hu

%package id
Summary: %{package_summary} - Indonesian
Group: %{group}
Requires: hunspell-id
Obsoletes: aspell-id <= 50:0.50.1
Requires: smeserver-formmagick >= 1.4.0-10
%description id
%{summary}
%files id -f %{name}-%{version}-%{release}-filelist-id

%package it
Summary: %{package_summary} - Italian
Group: %{group}
Requires: hunspell-it
Obsoletes: aspell-it <= 50:0.53
Requires: smeserver-formmagick >= 1.4.0-10
%description it
%{summary}
%files it -f %{name}-%{version}-%{release}-filelist-it

%package ja
Summary: %{package_summary} - Japanese
Group: %{group}
Requires: smeserver-formmagick >= 1.4.0-10
%description ja
%{summary}
%files ja -f %{name}-%{version}-%{release}-filelist-ja

%package nb
Summary: %{package_summary} - Norwegian (Bokmal)
Group: %{group}
Requires: hunspell-nb
Requires: smeserver-formmagick >= 1.4.0-10
%description nb
%{summary}
%files nb -f %{name}-%{version}-%{release}-filelist-nb

%package nl
Summary: %{package_summary} - Dutch
Group: %{group}
Requires: hunspell-nl
Obsoletes: aspell-nl <= 51:0.1e
Requires: smeserver-formmagick >= 1.4.0-10
%description nl
%{summary}
%files nl -f %{name}-%{version}-%{release}-filelist-nl

%package pl
Summary: %{package_summary} - Polish
Group: %{group}
Requires: hunspell-pl
Obsoletes: aspell-pl <= 50:0.51
Requires: smeserver-formmagick >= 1.4.0-10
%description pl
%{summary}
%files pl -f %{name}-%{version}-%{release}-filelist-pl

%package pt
Summary: %{package_summary} - Portugese
Group: %{group}
Requires: hunspell-pt
Obsoletes: aspell-pt <= 50:0.50
Requires: smeserver-formmagick >= 1.4.0-10
%description pt
%{summary}
%files pt -f %{name}-%{version}-%{release}-filelist-pt

%package pt_BR
Summary: %{package_summary} - Portugese (Brazilian)
Group: %{group}
Requires: hunspell-pt
Obsoletes: aspell-pt <= 50:0.50
Requires: smeserver-formmagick >= 1.4.0-10
%description pt_BR
%{summary}
%files pt_BR -f %{name}-%{version}-%{release}-filelist-pt_BR

%package ro
Summary: %{package_summary} - Romanian
Group: %{group}
Requires: hunspell-ro
Requires: smeserver-formmagick >= 1.4.0-10
%description ro
%{summary}
%files ro -f %{name}-%{version}-%{release}-filelist-ro

%package ru
Summary: %{package_summary} - Russian
Group: %{group}
Requires: hunspell-ru
Obsoletes: aspell-ru <= 50:0.99f7
Requires: smeserver-formmagick >= 1.4.0-10
%description ru
%{summary}
%files ru -f %{name}-%{version}-%{release}-filelist-ru

%package sl
Summary: %{package_summary} - Slovinian
Group: %{group}
Requires: hunspell-sl
Obsoletes: aspell-sl <= 50:0.50
Requires: smeserver-formmagick >= 1.4.0-10
%description sl
%{summary}
%files sl -f %{name}-%{version}-%{release}-filelist-sl

%package sv
Summary: %{package_summary} - Swedish
Group: %{group}
Requires: hunspell-sv
Obsoletes: aspell-sv <= 50:0.51
Requires: smeserver-formmagick >= 1.4.0-10
%description sv
%{summary}
%files sv -f %{name}-%{version}-%{release}-filelist-sv

%package th
Summary: %{package_summary} - Thai
Group: %{group}
Requires: hunspell-th
Requires: smeserver-formmagick >= 1.4.0-10
%description th
%{summary}
%files th -f %{name}-%{version}-%{release}-filelist-th

%package tr
Summary: %{package_summary} - Turkish
Group: %{group}
Requires: smeserver-formmagick >= 1.4.0-10
%description tr
%{summary}
%files tr -f %{name}-%{version}-%{release}-filelist-tr

%package zh_CN
Summary: %{package_summary} - Chinese (China)
Group: %{group}
Requires: smeserver-formmagick >= 1.4.0-10
%description zh_CN
%{summary}
%files zh_CN -f %{name}-%{version}-%{release}-filelist-zh_CN

%package zh_TW
Summary: %{package_summary} - Chinese (Taiwan)
Group: %{group}
Requires: smeserver-formmagick >= 1.4.0-10
%description zh_TW
%{summary}
%files zh_TW -f %{name}-%{version}-%{release}-filelist-zh_TW
