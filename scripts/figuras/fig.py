# Gerador de figuras humanas com contorno (estilo pictograma)
OUT = "#1e1e1e"
VIT = "#6f8aa3"   # vitima (azul acinzentado)
SOC = "#ef8a2b"   # socorrista (laranja)
SKIN = "#f2c9a5"
def limb(pts, w, color, out=OUT):
    p = " ".join(f"{x},{y}" for x, y in pts)
    return (f'<polyline points="{p}" fill="none" stroke="{out}" stroke-width="{w+5}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
def head(cx, cy, r, color, face_dx=0, face_dy=0):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" stroke="{OUT}" stroke-width="2.5"/>'
    if face_dx or face_dy:  # nariz indica para onde o rosto aponta
        nx, ny = cx + face_dx * r, cy + face_dy * r
        s += f'<circle cx="{nx}" cy="{ny}" r="{r*0.28:.1f}" fill="{color}" stroke="{OUT}" stroke-width="2"/>'
        s += f'<circle cx="{cx + face_dx*r*0.55 - face_dy*r*0.35:.1f}" cy="{cy + face_dy*r*0.55 + face_dx*r*0.35*-1:.1f}" r="{r*0.11:.1f}" fill="{OUT}"/>'
    return s
def hand(cx, cy, r=8, color=SKIN):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" stroke="{OUT}" stroke-width="2"/>'
def arrow(x1, y1, x2, y2, color="#d62828", w=4):
    import math
    a = math.atan2(y2 - y1, x2 - x1); L = 12
    p1 = (x2 - L*math.cos(a - 0.45), y2 - L*math.sin(a - 0.45)); p2 = (x2 - L*math.cos(a + 0.45), y2 - L*math.sin(a + 0.45))
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - 6*math.cos(a):.1f}" y2="{y2 - 6*math.sin(a):.1f}" stroke="{color}" stroke-width="{w}"/>'
            f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>')
def svg(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" font-family="DejaVu Sans, Arial, Helvetica, sans-serif">\n'
            f'<rect width="{w}" height="{h}" fill="#fff"/>\n'
            f'<text x="{w/2}" y="30" text-anchor="middle" font-size="20" font-weight="bold" fill="#222">{title}</text>\n{body}\n</svg>\n')
def text(x, y, s, size=13, color="#222", bold=False, anchor="start"):
    b = ' font-weight="bold"' if bold else ''
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}"{b} text-anchor="{anchor}">{s}</text>'
def box(x, y, w, h, fill="#fff4e5", stroke="#ef8a2b"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
