"""
Parse 3 File-Index.md files + 4 root files → global-index.json (Phase 1 skeleton)
Option A: Flat array, JS builds tree from path at runtime.
"""

import json
import re
import os

BASE_DIR = r"E:\ZEZE\Working\AI-Research\Human-Predictive-Drive"

# ─── AREA MAPPING (from path, order = most specific first) ───

AREA_RULES = [
    (r"^Core-Deep-Dive/Observation/", "observation-params"),
    (r"^Core-Deep-Dive/Body-Base/Body-Feedback/Drill-Body-Feedback/", "body-feedback"),
    (r"^Core-Deep-Dive/Body-Base/Body-Feedback/Drill-Evolutionary", "body-feedback"),
    (r"^Core-Deep-Dive/Body-Base/Body-Feedback/", "body-feedback"),
    (r"^Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/", "agent-mechanism"),
    (r"^Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/", "chunk-system"),
    (r"^Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-Internal-Processing/", "chunk-system"),
    (r"^Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-External-Development/", "chunk-system"),
    (r"^Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/", "chunk-system"),
    (r"^Core-Deep-Dive/Body-Base/Chunk/", "chunk-system"),
    (r"^Core-Deep-Dive/Body-Base/Feeling/Drill-Feeling", "feeling-system"),
    (r"^Core-Deep-Dive/Body-Base/Feeling/", "feeling-system"),
    (r"^Core-Deep-Dive/Body-Base/Schema/", "schema-anchor"),
    (r"^Core-Deep-Dive/Body-Base/Melody Lens/", "melody-lens"),
    (r"^Core-Deep-Dive/Body-Base/", "core-foundation"),
    (r"^Core-Deep-Dive/PFC/Imagination/", "pfc-system"),
    (r"^Core-Deep-Dive/PFC/", "pfc-system"),
    (r"^Core-Deep-Dive/Collective/", "collective"),
    (r"^Core-Deep-Dive/Domain/", "domain-theory"),
    (r"^Core-Deep-Dive/Clarification/", "clarification"),
    (r"^Core-Deep-Dive/", "core-foundation"),
    (r"^Research/Human-Learning/Child-Development/", "child-development"),
    (r"^Research/Human-Learning/Education-Mechanism/", "education-app"),
    (r"^Research/Global/Birth-Rate-Decline/", "global-analysis"),
    (r"^Research/Global/", "global-analysis"),
    (r"^Research/Health-Conditions/", "health-conditions"),
    (r"^Research/Melody-Technology/", "melody-lens"),
    (r"^Research/Meta-Impact/", "meta-epistemology"),
    (r"^Research/Mismatch-Patterns/", "global-analysis"),
    (r"^Research/Neuro-Measurement/", "reference-tools"),
    (r"^Research/Quote-Analysis/", "global-analysis"),
    (r"^Research/Drill-Sound-Brain/", "melody-lens"),
    (r"^Research/", "global-analysis"),
    (r"^Applications/Education-System/", "education-app"),
    (r"^Applications/", "education-app"),
]

def get_area(path):
    for pattern, area in AREA_RULES:
        if re.search(pattern, path):
            return area
    return "core-foundation"

# ─── CONTENT TYPE MAPPING ───

def get_content_type(path, group):
    pl = path.lower()
    gl = group.lower().strip() if group else ""

    # Drill detection (but synthesis/overview inside drill = keep type)
    is_drill_path = "drill" in pl and "drill-chunk/chunk" not in pl
    # Chunk-External-Development and Chunk-Internal-Processing are drill subfolders
    # but contain mechanism/synthesis files
    if "/chunk-internal-processing/" in pl or "/chunk-external-development/" in pl:
        is_drill_path = True
    if "/language-structure-analysis/" in pl:
        is_drill_path = True

    # ── FILENAME-BASED (highest priority — intentional naming) ──
    fn = os.path.basename(path).lower()
    if "analysis" in fn:
        return "analysis"
    if "observation" in fn and fn != "observation.md":
        return "observation"
    if "synthesis" in fn:
        return "overview"
    if fn.startswith("00") and ("overview" in fn or "reading" in fn or "sketch" in fn):
        return "overview"
    if "label" in fn:
        return "reference"

    # ── GROUP-BASED ──
    if gl in ("practical",):
        return "practical"
    if gl in ("planning",):
        return "reference"
    if gl in ("reference",):
        return "reference"
    if gl in ("index", "integration hub"):
        return "overview"
    if gl in ("framework",):
        return "overview"
    if "synthesis" in gl:
        return "overview"
    if gl in ("overview",):
        return "overview"
    if gl in ("mechanism", "core mechanisms", "core model", "core mechanism", "core definition"):
        return "mechanism"
    if gl in ("foundation",):
        return "drill" if is_drill_path else "mechanism"
    if gl in ("analysis", "hypothesis", "case study"):
        return "analysis"
    if gl in ("observation",):
        return "observation"
    if gl in ("cluster", "single"):
        return "analysis"
    if "bridge" in gl:
        return "mechanism"
    if gl in ("bias", "position"):
        return "analysis"
    if gl in ("proposal",):
        return "practical"
    if gl in ("core chunk dynamics", "higher mechanisms", "advanced + synthesis"):
        return "drill"
    if gl in ("map",):
        return "overview"
    if gl in ("core", "context"):
        return "mechanism"
    if gl in ("data+analysis",):
        return "analysis"
    if gl in ("output",):
        return "practical"
    if gl in ("governance",):
        return "mechanism"
    if gl in ("dynamics", "meta-synthesis", "meta-level", "patterns"):
        return "analysis"
    if gl in ("capacity deep dives", "observer labels", "processing modes", "applied understanding"):
        return "mechanism"
    if gl in ("bond types", "sustainability", "scale", "per-entity", "excess", "calibration"):
        return "mechanism"
    if gl in ("qc",):
        return "reference"
    if gl in ("evidence",):
        return "reference"

    # ── PATH-BASED fallbacks ──
    if "overview" in fn:
        return "overview"
    if is_drill_path:
        return "drill"
    if "/observation/" in pl:
        return "observation"

    return "mechanism"

# ─── DOMAINS MAPPING ───

AREA_DEFAULT_DOMAINS = {
    "core-foundation": ["core"],
    "observation-params": ["core", "neuroscience"],
    "body-feedback": ["core", "neuroscience"],
    "chunk-system": ["core", "neuroscience", "psychology"],
    "agent-mechanism": ["core", "neuroscience", "psychology"],
    "feeling-system": ["core", "psychology"],
    "schema-anchor": ["core", "psychology"],
    "melody-lens": ["psychology"],
    "pfc-system": ["core", "neuroscience"],
    "collective": ["social-collective", "behavioral"],
    "domain-theory": ["philosophy", "behavioral"],
    "clarification": ["neuroscience"],
    "child-development": ["development", "neuroscience"],
    "education-app": ["education", "development"],
    "global-analysis": ["social-collective", "behavioral"],
    "health-conditions": ["clinical", "neuroscience"],
    "meta-epistemology": ["philosophy"],
    "reference-tools": ["core"],
}

def get_domains(path, area, description):
    domains = list(AREA_DEFAULT_DOMAINS.get(area, ["core"]))
    text = (path + " " + description).lower()

    extras = []
    if any(w in text for w in ["ai-schema", "ai-self", "ai-collective", "human-ai", "ai ", "artificial", "ai-assisted", "ai era"]):
        extras.append("ai-tech")
    if any(w in text for w in ["religion", "idol", "music", "sound", "auditory", "melody"]):
        if "philosophy" not in domains:
            extras.append("philosophy")
    if any(w in text for w in ["education", "learning", "school", "teacher", "curriculum", "dạy"]):
        extras.append("education")
    if any(w in text for w in ["child", "infant", "prenatal", "parenting", "mẹ", "con"]):
        extras.append("development")
    if any(w in text for w in ["empathy", "connection", "love", "romantic", "bond", "gratitude", "obligation"]):
        extras.append("psychology")
    if any(w in text for w in ["ocd", "ptsd", "adhd", "autism", "addiction", "alzheimer", "parkinson", "nicotine", "alcohol"]):
        extras.append("clinical")
    if any(w in text for w in ["birth-rate", "innovation", "social-calibration", "collective", "society", "money", "tiền"]):
        extras.append("social-collective")
    if any(w in text for w in ["uncanny", "fidget", "sensitivity", "climate"]):
        extras.append("behavioral")

    for e in extras:
        if e not in domains:
            domains.append(e)

    return domains

# ─── SHORT DESCRIPTION ───

def make_short_desc(description):
    """Extract first meaningful clause, max ~120 chars."""
    desc = description

    # Pass 1: Strip leading markers (stars, checkmarks)
    desc = re.sub(r'^[⭐✅\s]*', '', desc)

    # Pass 2: Strip version + noise words
    # "v2.3: ...", "v3.0. FULL REWRITE: ...", "v1.0 (date). ..."
    desc = re.sub(
        r'^v[\d.]+[^A-Za-zÀ-ɏ]*'
        r'(?:(?:FULL\s+)?REWRITE|ENRICHED|(?:DEEP\s+)?REFINE|SPLIT|RENAME|(?:BOUNDARY\s+)?REFRAME|NEW|COMPLETE|DONE)'
        r'[^A-Za-zÀ-ɏ]*',
        '', desc, flags=re.IGNORECASE
    )
    desc = re.sub(r'^v[\d.]+[^A-Za-zÀ-ɏ]*', '', desc, flags=re.IGNORECASE)

    # Pass 3: Strip remaining noise prefixes
    desc = re.sub(r'^(?:ENTRY\s+POINT\s*/?\s*)', '', desc)
    desc = desc.strip()

    # Take first sentence
    parts = re.split(r'(?<=[.!?])\s+|(?<=。)\s*', desc, maxsplit=1)
    short = parts[0].strip()

    # If first fragment is just noise (< 10 chars), try next sentence
    if len(short) < 10 and len(parts) > 1:
        next_part = parts[1].strip()
        parts2 = re.split(r'(?<=[.!?])\s+', next_part, maxsplit=1)
        short = parts2[0].strip()

    if len(short) < 10 and len(desc) > 10:
        short = desc

    # Truncate to ~120 chars at word boundary
    if len(short) > 120:
        short = short[:120]
        last_space = short.rfind(' ')
        if last_space > 60:
            short = short[:last_space]
        short += "..."

    # Clean trailing punctuation noise
    short = short.strip(' .:;,')

    return short

# ─── ID GENERATION ───

def make_id(path):
    """Generate unique kebab-case id from path."""
    # Remove extension
    s = re.sub(r'\.md$', '', path, flags=re.IGNORECASE)
    # Replace path separators and spaces with -
    s = s.replace('/', '-').replace('\\', '-').replace(' ', '-')
    # Lowercase
    s = s.lower()
    # Remove consecutive dashes
    s = re.sub(r'-+', '-', s)
    # Remove leading/trailing dashes
    s = s.strip('-')
    return s

# ─── FILE INDEX PARSER ───

def parse_file_index(filepath):
    """Parse pipe-delimited File-Index.md, return list of (path, folder, group, description)."""
    entries = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Skip comments, blank lines
            if not line or line.startswith('#'):
                continue
            # Must contain pipes
            if ' | ' not in line:
                continue
            parts = [p.strip() for p in line.split('|', 3)]
            if len(parts) < 4:
                continue
            path, folder, group, description = parts
            # Skip self-reference (File-Index files themselves)
            if '01-File-Index' in path:
                continue
            # Skip if description says "File này"
            if description.startswith("File này"):
                continue
            # Skip plan/tracking files
            fn_lower = os.path.basename(path).lower()
            if fn_lower.startswith("plan") or fn_lower == "pending-quotes.md":
                continue
            entries.append((path, folder, group, description))
    return entries

# ─── ROOT FILES (not in any File-Index) ───

ROOT_FILES = [
    {
        "path": "Core-Hardware.md",
        "folder": "",
        "group": "",
        "description": "HARDWARE MAP: Physical brain architecture — 4 zones (PFC/Cortical/Subcortical/Peripheral), neural pathways, receptor systems. WHERE things are in the brain. Companion of Core-Software.md (HOW) and Ask-AI.md (INTERFACE)."
    },
    {
        "path": "Core-Software.md",
        "folder": "",
        "group": "",
        "description": "SOFTWARE MAP: Cycle-based operating mechanisms — the main loop (Domain→Body-Input→Processing→Feeling→PFC→Output→Domain). HOW the brain runs. v7.8 architecture. Companion of Core-Hardware.md (WHERE) and Ask-AI.md (INTERFACE)."
    },
    {
        "path": "Ask-AI.md",
        "folder": "",
        "group": "",
        "description": "AI INTERFACE: Protocol for using AI to explore the framework. Danger zones where AI training data conflicts with framework positions. Dual Check method (body=quality controller, domain=final arbiter). How to ask questions effectively."
    },
]

# ─── MAIN ───

def main():
    files = []

    # 1. Add root files
    for rf in ROOT_FILES:
        path = rf["path"]
        area = "core-foundation"
        ct = "overview"
        domains = ["core"]
        if "Ask-AI" in path:
            ct = "reference"
            domains = ["core", "ai-tech"]
        files.append({
            "id": make_id(path),
            "fileName": os.path.basename(path),
            "path": path,
            "domains": domains,
            "area": area,
            "contentType": ct,
            "shortDescription": make_short_desc(rf["description"]),
            "fullDescription": ""
        })

    # 2. Parse 3 File-Index files
    index_files = [
        os.path.join(BASE_DIR, "Core-Deep-Dive", "01-File-Index.md"),
        os.path.join(BASE_DIR, "Research", "01-File-Index.md"),
        os.path.join(BASE_DIR, "Applications", "01-File-Index.md"),
    ]

    for idx_path in index_files:
        entries = parse_file_index(idx_path)
        for path, folder, group, description in entries:
            area = get_area(path)
            ct = get_content_type(path, group)
            domains = get_domains(path, area, description)
            short = make_short_desc(description)

            files.append({
                "id": make_id(path),
                "fileName": os.path.basename(path),
                "path": path,
                "domains": domains,
                "area": area,
                "contentType": ct,
                "shortDescription": short,
                "fullDescription": ""
            })

    # 2b. Sort: root files first, then Core-Deep-Dive, Research, Applications last
    def sort_key(f):
        p = f["path"]
        if "/" not in p:
            return (0, p)
        if p.startswith("Core-Deep-Dive/"):
            return (1, p)
        if p.startswith("Research/"):
            return (2, p)
        if p.startswith("Applications/"):
            return (3, p)
        return (4, p)

    files.sort(key=sort_key)

    # 3. Build meta
    all_domains = sorted(set(d for f in files for d in f["domains"]))
    all_areas = sorted(set(f["area"] for f in files))
    all_types = sorted(set(f["contentType"] for f in files))

    domain_labels = {
        "core": "Core Architecture",
        "neuroscience": "Neuroscience",
        "psychology": "Psychology",
        "behavioral": "Behavioral Science",
        "development": "Human Development",
        "education": "Education",
        "clinical": "Health & Clinical",
        "social-collective": "Social & Collective",
        "ai-tech": "AI & Technology",
        "philosophy": "Philosophy & Meta",
    }
    area_labels = {
        "core-foundation": "Core Foundation",
        "body-feedback": "Body-Feedback System",
        "chunk-system": "Chunk System",
        "agent-mechanism": "Agent & Entity",
        "pfc-system": "PFC & Simulation",
        "feeling-system": "Feeling System",
        "observation-params": "Observation Parameters",
        "schema-anchor": "Schema & Anchor",
        "collective": "Collective & Coordination",
        "domain-theory": "Domain Theory",
        "health-conditions": "Health Conditions",
        "child-development": "Child Development",
        "education-app": "Education Applications",
        "global-analysis": "Global & Economic Analysis",
        "meta-epistemology": "Meta & Epistemology",
        "reference-tools": "Reference & Tools",
        "melody-lens": "Melody Lens",
        "clarification": "Clarification",
    }
    type_labels = {
        "mechanism": "Mechanism",
        "analysis": "Analysis",
        "observation": "Observation",
        "practical": "Practical Guide",
        "drill": "Drill & Deep Dive",
        "reference": "Reference",
        "overview": "Overview & Synthesis",
    }

    index = {
        "meta": {
            "totalFiles": len(files),
            "generatedDate": "2026-05-31",
            "frameworkVersion": "v7.8",
            "layers": {
                "domains": [{"id": d, "label": domain_labels.get(d, d)} for d in all_domains],
                "areas": [{"id": a, "label": area_labels.get(a, a)} for a in all_areas],
                "contentTypes": [{"id": t, "label": type_labels.get(t, t)} for t in all_types],
            },
            "folderOrder": ["Core-Deep-Dive", "Research", "Applications"],
            "collapsedFolders": ["Applications", "Drill*"]
        },
        "files": files
    }

    # 4. Write JSON
    out_path = os.path.join(BASE_DIR, "html-page", "global-index.json")

    # Also print some stats
    print(f"Total files: {len(files)}")
    print(f"Domains: {all_domains}")
    print(f"Areas: {all_areas}")
    print(f"Content types: {all_types}")
    print()

    # Count per area
    area_counts = {}
    for f in files:
        area_counts[f["area"]] = area_counts.get(f["area"], 0) + 1
    print("Files per area:")
    for a in sorted(area_counts, key=lambda x: -area_counts[x]):
        print(f"  {a}: {area_counts[a]}")

    # Count per content type
    type_counts = {}
    for f in files:
        type_counts[f["contentType"]] = type_counts.get(f["contentType"], 0) + 1
    print("\nFiles per content type:")
    for t in sorted(type_counts, key=lambda x: -type_counts[x]):
        print(f"  {t}: {type_counts[t]}")

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"\nWritten to: {out_path}")
    print(f"File size: {os.path.getsize(out_path):,} bytes")

if __name__ == "__main__":
    main()
