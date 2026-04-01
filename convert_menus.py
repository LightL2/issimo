"""
Convert PDF menu pages to JPEG images for fast mobile loading.
Output: Assets/menu-main/page-00.jpg, Assets/menu-breakfast/page-00.jpg
"""
import fitz  # PyMuPDF
import os

MENUS = [
    {
        "pdf":    r"d:\8bit]\Issimo\issimo\Assets\menu-main.pdf",
        "outdir": r"d:\8bit]\Issimo\issimo\Assets\menu-main",
    },
    {
        "pdf":    r"d:\8bit]\Issimo\issimo\Assets\menu-breakfast.pdf",
        "outdir": r"d:\8bit]\Issimo\issimo\Assets\menu-breakfast",
    },
]

# 150 DPI → crisp on mobile, reasonable file size
# max width 900px, JPEG quality 85
DPI      = 150
MAX_W    = 900
QUALITY  = 85

def convert(pdf_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    doc  = fitz.open(pdf_path)
    mat  = fitz.Matrix(DPI / 72, DPI / 72)   # 72 = PDF base DPI
    name = os.path.basename(pdf_path)
    print(f"\n[PDF] {name}  ({len(doc)} pages)")

    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=mat, alpha=False)

        # Downscale if wider than MAX_W
        if pix.width > MAX_W:
            scale = MAX_W / pix.width
            mat2  = fitz.Matrix(DPI / 72 * scale, DPI / 72 * scale)
            pix   = page.get_pixmap(matrix=mat2, alpha=False)

        out_path = os.path.join(out_dir, f"page-{i:02d}.jpg")
        pix.save(out_path, jpg_quality=QUALITY)

        size_kb = os.path.getsize(out_path) // 1024
        print(f"  page {i+1:02d}/{len(doc)} - {size_kb} KB")

    doc.close()
    # Total size
    total = sum(os.path.getsize(os.path.join(out_dir, f))
                for f in os.listdir(out_dir)) // 1024
    print(f"  DONE Total: {total} KB  ({total//1024} MB)")

for m in MENUS:
    convert(m["pdf"], m["outdir"])

print("\nConversion complete!")
