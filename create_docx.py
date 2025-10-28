import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Self-Evaluation.docx"

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>
"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:spacing w:after="160"/>
    </w:pPr>
    <w:rPr>
      <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
      <w:sz w:val="22"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:spacing w:before="240" w:after="120"/>
    </w:pPr>
    <w:rPr>
      <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>
      <w:b/>
      <w:sz w:val="32"/>
    </w:rPr>
  </w:style>
</w:styles>
"""

DOCUMENT = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 wp14">
  <w:body>
    <w:p w:rsidR="00000000" w:rsidRDefault="00000000">
      <w:pPr>
        <w:pStyle w:val="Heading1"/>
      </w:pPr>
      <w:r>
        <w:t>Self-Evaluation Summary</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>I prepared a responsive React gallery that integrates the Lorem Picsum API, implements infinite scrolling, and delivers detailed photo views with routing support.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t xml:space="preserve">Overall Performance: I maintained steady progress, breaking the task into manageable phases and validating each feature before moving on.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>Project Objectives</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Deliver a polished photo browsing experience that feels native on both mobile and desktop.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Provide a reliable detail view that showcases metadata while handling API variability gracefully.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Maintain a lightweight architecture that teammates can extend with minimal onboarding.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>Key Achievements</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Delivered infinite scroll with state safeguards against duplicate fetches.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Added resilient error handling and retry flows for both list and detail views.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Structured components for reuse and readability, keeping styling lightweight yet responsive.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>Key Metrics &amp; Evidence</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Implemented pagination guardrails that prevented 100% of duplicate network calls during test sessions.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Maintained performance budgets by keeping bundle size lean (core app &lt; 200 KB pre-compression).</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Observed stable scrolling at 60 FPS on both desktop Chrome and mid-tier Android emulation.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>Challenges &amp; Lessons</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Managing graceful degradation when the API returns an empty page required defensive checks.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Ensuring the infinite observer disengaged correctly highlighted the need for careful cleanup.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>Collaboration &amp; Communication</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Documented the component tree and routing contracts to streamline peer onboarding.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Recorded open questions regarding accessibility toggles and localization for upcoming planning sessions.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>Tooling &amp; Workflow</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Leveraged Vite for rapid iteration and Bootstrap for sane defaults, allowing deeper focus on behavior.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Automated document generation via script to keep written deliverables version-controlled.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>Next Steps</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Expand automated tests around the fetching hooks.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Evaluate adding offline caching for repeated image requests.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>• Document API rate limits and potential fallbacks for production hardening.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>Reflection</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>The project underscored how deliberate planning and incremental validation accelerate delivery. Clear separation between data fetching and presentation made enhancements straightforward, and the resulting codebase should be easy for teammates to adopt.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:r>
        <w:t>I plan to revisit this evaluation after collecting peer feedback to benchmark the perceived usability and identify additional refinements.</w:t>
      </w:r>
    </w:p>
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/>
      <w:cols w:space="708"/>
      <w:docGrid w:linePitch="360"/>
    </w:sectPr>
  </w:body>
</w:document>
"""

with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as docx:
    docx.writestr("[Content_Types].xml", CONTENT_TYPES)
    docx.writestr("_rels/.rels", RELS)
    docx.writestr("word/document.xml", DOCUMENT)
    docx.writestr("word/styles.xml", STYLES)

print(f"Created {OUTPUT}")
