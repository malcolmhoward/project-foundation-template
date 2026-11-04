# Sources Register

This register lists the external sources behind claims in PFT's principles (`core/principles/`) and guides
(`core/guides/`), which users reach through the Python API (and, for some principles, during interactive generation),
in the templates for generated files (`core/templates/`), and in CONTRIBUTING.md: laws, standards, specifications,
studies and third parties' terms. For each source it records what is relied on, where to find it, when and how it was
checked, and the wording that supports the claim.

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
- **Not checked:** the standard's own text, which requires accepting a license to download.

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

## Specifications and standards

Checked 2026-10-27 unless stated otherwise.

- **HTTP status codes:** RFC 9110, *HTTP Semantics*, section 15 (https://www.rfc-editor.org/rfc/rfc9110.html); 422 is
  "Unprocessable Content" (section 15.5.21). RFC 6585, section 4 defines 429 Too Many Requests
  (https://www.rfc-editor.org/rfc/rfc6585.html#section-4). Used in the API standards guide.
- **OAuth 2.0:** RFC 6749, *The OAuth 2.0 Authorization Framework* (https://www.rfc-editor.org/rfc/rfc6749.html).
- **Dates:** RFC 3339, *Date and Time on the Internet: Timestamps* (https://www.rfc-editor.org/rfc/rfc3339.html), a
  profile of ISO 8601.
- **Semantic Versioning 2.0.0:** https://semver.org/spec/v2.0.0.html. Item 4: "Major version zero (0.y.z) is for
  initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable." FAQ "How do I
  know when to release 1.0.0?": "If your software is being used in production, it should probably already be 1.0.0. If
  you have a stable API on which users have come to depend, you should be 1.0.0." No source was found for how widely
  SemVer is used, so the versioning principle makes no claim about adoption.
- **Conventional Commits 1.0.0:** https://www.conventionalcommits.org/en/v1.0.0/. feat "correlates with MINOR", fix
  "correlates with PATCH", and a `BREAKING CHANGE:` footer or `!` introduces a breaking change "correlating with MAJOR".
  "Types other than feat and fix MAY be used"; "Additional types are not mandated by the Conventional Commits
  specification."
- **Version ranges:** PEP 440, "Compatible release" (https://peps.python.org/pep-0440/#compatible-release) for `~=`;
  npm's node-semver README, "Caret Ranges" (https://github.com/npm/node-semver) for `^`. The versioned npm
  documentation pages returned 404, so npm's own README was used.
- **Contributor Covenant 2.0:** https://www.contributor-covenant.org/version/2/0/code_of_conduct/ (the generated code
  of conduct). The site's latest version is 3.0; moving the template to it is a separate change.
- **License texts:** the generated MIT text matches GitHub's canonical text (`gh api licenses/mit`, compared
  2026-11-03).

## Platform and programme documentation

- **Removing secrets from git history:** GitHub Docs, "Removing sensitive data from a repository",
  https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
  (checked 2026-10-27): "as a first step you need to revoke and/or rotate that secret"; rewriting history "may not be
  warranted".
- **GitHub Actions cost:** GitHub Docs, "GitHub Actions billing",
  https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions
  (checked 2026-10-27): "GitHub Actions usage is free for self-hosted runners and for public repositories that use
  standard GitHub-hosted runners."
- **Security policies:** GitHub Docs, "Adding a security policy to your repository",
  https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository (checked
  2026-10-27): "You can give instructions for how to report a security vulnerability in your project." The page does
  not say GitHub recommends a policy for every public repository, so the text no longer claims that.
- **Requesting a CVE ID:** CVE Program, https://www.cve.org/ReportRequest/ReportRequestForNonCNAs#RequestCVEID (checked
  2026-10-27; the page renders with JavaScript, so its text was read from the site's own script): find the CVE
  Numbering Authority (CNA) whose scope covers the product; the CNA of Last Resort is the fallback. No one has yet
  checked the rendered page in a browser. GitHub Docs, "About repository security advisories" and "Publishing a
  repository security advisory" (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories,
  checked 2026-10-27): "GitHub is a CVE Numbering Authority (CNA) and is authorized to assign CVE identification
  numbers"; "Anyone with admin permissions to a security advisory can request a CVE identification number."
- **CVE and the NVD:** the CVE Program's website source, https://github.com/CVEProject/cve-website (`faqs.json` and
  `About/RelatedEfforts.vue`, checked 2026-11-03): "CVE and NVD are two separate programs"; "The CVE List feeds NVD, which historically has built upon the information included in CVE Records";
  "you can request that the CVE Record be updated by contacting the CNA that assigned the CVE ID".

## Reports and studies

- **Verizon 2026 Data Breach Investigations Report:** https://www.verizon.com/business/resources/reports/dbir/ (full
  report PDF, p.10; checked 2026-10-27): "Exploitation of vulnerabilities is now the most common initial access vector
  for breaches. It has risen to 31% in this year's reporting dataset, while credential abuse—the previous leader—is
  down to 13%." The verification notes read the figure as a share of breaches with a known initial access vector
  (excluding Error and Misuse breaches), which is how the principle states it. The report has no analysis of secrets
  committed to code repositories, so it is not cited for that.
- **AI-generated content and fabricated references** (CONTRIBUTING.md, Sources and Claims; checked 2026-10-25): Huang
  et al., ACM Transactions on Information Systems, https://doi.org/10.1145/3703155 (a survey of hallucination in large
  language models); Walters & Wilder, Scientific Reports 13:14045 (2023), https://doi.org/10.1038/s41598-023-41032-5,
  which found fabricated citations in references generated by GPT-3.5 and GPT-4.
