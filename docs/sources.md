# Sources Register

This register lists the external sources behind claims in PFT's principles (`core/principles/`) and guides
(`core/guides/`), which users reach through the Python API (and, for some principles, during interactive generation):
laws, standards and third parties' terms. For each source it records what is relied on, where to find it, when and how it was checked, and
the wording that supports the claim.

**WHY:** a reader should be able to check every claim about the outside world. Links break and laws change, so each
entry names the provision, not just a URL, and says when it was last checked.

**HOW to keep it current:**
- Re-check every entry whenever `EXPIRATION_DATE` in `core/utils.py` is updated (see
  [ADR 0003](adr/0003-advisory-expiration.md)), and update "Checked" and the text that relies on it.
- When you add a claim that needs a source, add an entry here in the same pull request.
- Prefer the publisher's own text. If it can't be read directly, record the official copy you used.

## Legal and regulatory sources

Checked 2026-11-03 unless stated otherwise.

### GDPR: Regulation (EU) 2016/679

- **Link:** https://eur-lex.europa.eu/eli/reg/2016/679/oj
- **Version checked:** the Official Journal text (OJ L 119, 4.5.2016), from EUR-Lex PDFs downloaded by the maintainer
  and from the EU Publications Office. The consolidated version (CELEX 02016R0679-20160504) has no amendments; its
  one corrigendum (OJ L 127, 23.5.2018) changes Art. 43(3) and Art. 65(1)(a), neither of which is cited here.
- **Relied on:**

| Provision | Used for | Wording relied on |
|---|---|---|
| Title | What the Regulation covers | "on the protection of natural persons with regard to the processing of personal data and on the free movement of such data" |
| Art. 3(1)-(2) | Territorial scope | establishment in the Union; offering goods or services to, or monitoring the behaviour of, data subjects "who are in the Union" |
| Art. 5(1)(c), 6(1), 15, 17, 17(3), 20 | Principles and rights | data minimisation; lawful bases; access; erasure and its exceptions; portability |
| Art. 20(1) | Portability conditions | data "which he or she has provided to a controller", where processing is based on consent or a contract "and" "carried out by automated means" |
| Art. 25 | Data protection by design and by default | obligations of "the controller" |
| Art. 32(1)(a) | Encryption as an example measure | "including inter alia as appropriate: (a) the pseudonymisation and encryption of personal data" |
| Art. 33(1)-(2) | Breach notification | "without undue delay and, where feasible, not later than 72 hours after having become aware of it ... unless the personal data breach is unlikely to result in a risk"; "The processor shall notify the controller without undue delay" |
| Art. 34(1), 34(3) | Telling people affected | "likely to result in a high risk ... without undue delay"; 34(3): "shall not be required if any of the following conditions are met" |
| Art. 83(4)-(5) | Fine ceilings | "up to 10 000 000 EUR, or in the case of an undertaking, up to 2 %"; "up to 20 000 000 EUR ... up to 4 % of the total worldwide annual turnover of the preceding financial year, whichever is higher" |

- **Second source for Art. 33(1):** EDPB Guidelines 9/2022 on personal data breach notification, version 2.0,
  para. 29, which quotes the article:
  https://www.edpb.europa.eu/system/files/documents/2023-04/edpb_guidelines_202209_personal_data_breach_notification_v2.0_en.pdf

### European Accessibility Act: Directive (EU) 2019/882

- **Link:** https://eur-lex.europa.eu/eli/dir/2019/882/oj
- **Version checked:** the Official Journal text (OJ L 151, 7.6.2019), as for the GDPR. The only consolidated version
  (CELEX 02019L0882-20190607) has no amendments; its corrigendum (OJ L 23, 29.1.2020) is in the Estonian version.
- **Relied on:** Art. 2 (scope: listed products and services); Art. 4(5) ("Microenterprises providing services shall
  be exempt from complying with the accessibility requirements"); Art. 31(2): the Directive applies through Member
  States' national measures ("They shall apply those measures from 28 June 2025"). Art. 31(3) lets Member States
  apply the Art. 4(8) obligations from 28 June 2027 at the latest (the "transitional periods" the text mentions).

### HIPAA: 45 CFR Part 164

- **Link:** https://www.ecfr.gov/current/title-45/part-164 (checked 2026-10-27 via the eCFR versioner, 2026-10-01 text)
- **Relied on:** 164.104 and 164.302 (applies to covered entities and business associates); 164.306(a)(1) (re-checked
  2026-11-03: "Ensure the confidentiality, integrity, and availability of all electronic protected health information
  the covered entity or business associate creates, receives, maintains, or transmits"; (a)(3) refers to uses and
  disclosures "not permitted or required under subpart E"); subpart E heading "Privacy of Individually Identifiable
  Health Information" (re-checked 2026-11-03); 164.312(a)(1) "Standard: Access control" and 164.312(b)
  "Standard: Audit controls" ("record and examine activity in information systems that contain or use electronic
  protected health information", re-checked 2026-11-03); 164.306(d)(3) (addressable
  specifications: assess; implement if reasonable and appropriate, or document why not and implement an equivalent
  alternative measure if reasonable and appropriate); 164.312(a)(2)(iv) (encryption is addressable); 164.308(b),
  164.314(a), 164.504(e) (business associate contracts).

### PCI DSS

- **Links:** https://www.pcisecuritystandards.org/standards/pci-dss/ ; FAQ 1135:
  https://www.pcisecuritystandards.org/faqs/1135 ; PCI SSC blog, 11 June 2024:
  https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1 (checked 2026-10-27)
- **Relied on:** applies to "Entities that store, process, or transmit cardholder data (CHD) and/or sensitive
  authentication data (SAD)" and those that "could impact the security of the cardholder data environment"; "PCI DSS
  v4.0 will be retired on 31 December 2024 ... v4.0.1 will be the only active version"; "implementing adequate network
  segmentation can reduce the scope of the PCI DSS assessment".
- **Not checked:** the standard's own text, which requires accepting a licence to download.

### SOC 2

- **Link:** https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2 (checked 2026-11-03)
- **Relied on:** AICPA describes SOC as "a suite of service offerings CPAs may provide in connection with system-level
  controls of a service organization", and its SOC 2 guide covers an "examination of a service organization's
  description of its system ... relevant to security, availability, processing integrity, confidentiality, or
  privacy".
- **Not checked:** the Trust Services Criteria themselves and the Type 1 / Type 2 definitions, which need an AICPA
  account. The guide therefore makes no claims about them. AICPA has published proposed 2027 criteria.

### ISO/IEC 27001

- **Link:** https://webstore.iec.ch/en/publication/79694 (IEC is a co-publisher; iso.org could not be read)
- **Relied on:** current edition ISO/IEC 27001:2022 (published 2022-10-25), amended by ISO/IEC 27001:2022/AMD1:2024
  ("Climate action changes", 2024-02-23). The guide names the standard without an edition.

### Accessibility: WCAG, ADA Title II

- **WCAG 2.2:** https://www.w3.org/TR/WCAG22/#cc1 (W3C Recommendation, 12 December 2024 edition; checked 2026-10-27).
  "three levels of conformance are defined: A (lowest), AA, and AAA (highest)"; "For Level AA conformance, the web page
  satisfies all the Level A and Level AA success criteria"; "It is not recommended that Level AAA conformance be
  required as a general policy for entire sites".
- **ADA Title II rule (US Department of Justice):** https://www.ada.gov/resources/2024-03-08-web-rule/ (checked
  2026-10-27). "WCAG Version 2.1, Level AA is the technical standard for state and local governments' web content and
  mobile apps"; an interim final rule of 20 April 2026 moved compliance dates to 26 April 2027 (population 50,000 or
  more) and 26 April 2028 (smaller entities and special districts).

### CCPA

- **Link:** https://oag.ca.gov/privacy/ccpa (California Attorney General; checked 2026-10-27). Named only as a
  consumer-privacy law; no thresholds are stated in the guide.

## Licensing and platform terms

- **US copyright default:** U.S. Copyright Office, Circular 1, https://www.copyright.gov/circs/circ01.pdf (checked
  2026-10-27): "Copyright protection in the United States exists automatically from the moment the original work of
  authorship is fixed"; the owner has the exclusive right to reproduce, prepare derivative works and distribute copies,
  "subject to certain statutory limitations", including fair use, which permits "the unlicensed use of
  copyright-protected works in certain circumstances" (re-checked 2026-11-03). Other countries' rules were not
  checked; the text says they differ.
- **GitHub Terms of Service, D.5:**
  https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#5-license-grant-to-other-users (checked
  2026-10-27): "By setting your repositories to be viewed publicly, you agree to allow others to view and 'fork' your
  repositories (this means that others may make their own copies within the Service in repositories they control)."
- **Licenses:** https://opensource.org/license/mit , https://opensource.org/license/apache-2-0 (section 3, patent
  grant), https://opensource.org/license/gpl-3-0 ; summaries from https://choosealicense.com/licenses/ (GPLv3:
  "Permissions of this strong copyleft license are conditioned on making available complete source code of licensed
  works") (checked 2026-10-27).
- **License texts in generated LICENSE files** (`core/templates/license_texts.py`): GitHub's licenses API,
  `gh api licenses/mit`, `licenses/apache-2.0` and `licenses/gpl-3.0` (fetched 2026-11-03), stored unchanged and
  pinned by SHA-256 in `tests/test_license_texts.py`. The Apache 2.0 text matches this repository's own LICENSE file.
  Where to put the copyright notice comes from each license's own "how to apply" section (the Apache appendix; the
  GPL's "How to Apply These Terms to Your New Programs"). choosealicense.com pages are at `/licenses/mit/`,
  `/licenses/apache-2.0/` and `/licenses/gpl-3.0/`; `/licenses/gpl/` returned 404 on 2026-11-03.

## Other sources

- **Alt text and search:** Google Search Central, "Image SEO best practices",
  https://developers.google.com/search/docs/appearance/google-images (checked 2026-10-27): "Google uses alt text along
  with computer vision algorithms and the contents of the page to understand the subject matter of the image."
