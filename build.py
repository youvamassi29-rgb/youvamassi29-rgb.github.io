#!/usr/bin/env python3
"""Génère le site Enseigne Web (page de vente, pages métiers, démos, sitemap).
Usage : python3 build.py   — relancer après toute modification des données ci-dessous."""
import html, pathlib

ROOT = pathlib.Path(__file__).parent
BASE = "https://youvamassi29-rgb.github.io"  # à remplacer par le nom de domaine définitif
BRAND = "Enseigne Web"

METIERS = {
    "plombier": dict(
        nom="plombier", pluriel="plombiers", art="un plombier",
        recherche="« plombier + votre ville », « fuite d'eau urgent », « remplacement chauffe-eau »",
        besoins=["Un bouton d'appel visible dès la première seconde, parce qu'une fuite n'attend pas",
                 "Vos zones d'intervention, commune par commune, pour sortir sur les recherches locales",
                 "Vos prestations détaillées : dépannage, chauffe-eau, salle de bain, chauffage",
                 "Un formulaire de devis qui arrive directement sur votre téléphone"],
        angle="En plomberie, le client appelle le premier professionnel qui inspire confiance. Sans site, vous dépendez du bouche-à-oreille et des plateformes qui prennent une commission sur chaque chantier."),
    "electricien": dict(
        nom="électricien", pluriel="électriciens", art="un électricien",
        recherche="« électricien + votre ville », « mise aux normes tableau électrique », « installation borne de recharge »",
        besoins=["Vos qualifications et assurances affichées clairement (décennale, labels)",
                 "Une page par prestation : mise aux normes, rénovation, borne de recharge, dépannage",
                 "Des photos de vos chantiers, avant et après",
                 "Un formulaire de devis simple, sans aller-retour inutile"],
        angle="Un chantier électrique se décide sur la confiance : le client veut voir vos qualifications, vos réalisations et vos coordonnées avant d'appeler."),
    "coiffeur": dict(
        nom="coiffeur", pluriel="coiffeurs et salons de coiffure", art="un salon de coiffure",
        recherche="« coiffeur + votre ville », « coiffeur ouvert lundi », « tarif balayage »",
        besoins=["Vos tarifs lisibles sur téléphone, sans PDF à télécharger",
                 "Vos horaires et votre adresse avec l'itinéraire",
                 "Un bouton de prise de rendez-vous (téléphone ou outil de réservation que vous utilisez déjà)",
                 "Les photos de votre salon et de vos réalisations"],
        angle="Avant de pousser la porte d'un salon, le client regarde les tarifs, les photos et les horaires. S'il ne les trouve pas, il va chez le voisin."),
    "peintre": dict(
        nom="peintre en bâtiment", pluriel="peintres en bâtiment", art="un peintre",
        recherche="« peintre + votre ville », « devis peinture appartement », « ravalement façade »",
        besoins=["Une galerie avant / après : c'est votre meilleur argument",
                 "Vos prestations : intérieur, façade, papier peint, revêtements de sol",
                 "Vos zones d'intervention",
                 "Un formulaire de devis avec surface et type de travaux"],
        angle="La peinture se vend à l'œil. Un site avec vos réalisations fait le travail de démonstration à votre place, 24 heures sur 24."),
    "macon": dict(
        nom="maçon", pluriel="maçons", art="un maçon",
        recherche="« maçon + votre ville », « extension maison », « devis terrasse béton »",
        besoins=["Vos chantiers en photos : extension, terrasse, mur, rénovation",
                 "Vos assurances et garanties affichées (décennale)",
                 "Vos zones d'intervention",
                 "Un formulaire de devis pour trier les demandes sérieuses"],
        angle="Un client qui confie plusieurs milliers d'euros de travaux vérifie toujours à qui il a affaire. Votre site est cette vérification."),
    "menuisier": dict(
        nom="menuisier", pluriel="menuisiers", art="un menuisier",
        recherche="« menuisier + votre ville », « pose fenêtres », « dressing sur mesure »",
        besoins=["Une galerie de vos réalisations sur mesure",
                 "Vos spécialités : fenêtres, portes, escaliers, agencement",
                 "Les matériaux et marques que vous posez",
                 "Un formulaire de devis avec envoi de photos"],
        angle="Le sur-mesure se choisit sur photos. Sans site, vos plus belles réalisations restent invisibles."),
    "couvreur": dict(
        nom="couvreur", pluriel="couvreurs", art="un couvreur",
        recherche="« couvreur + votre ville », « fuite toiture urgence », « démoussage toiture prix »",
        besoins=["Un numéro d'urgence visible immédiatement",
                 "Vos prestations : réparation, rénovation, zinguerie, démoussage, isolation",
                 "Vos assurances affichées (décennale)",
                 "Vos zones d'intervention"],
        angle="Le secteur de la toiture souffre des démarcheurs peu scrupuleux. Un site clair, avec votre identité et vos assurances, vous distingue immédiatement."),
    "paysagiste": dict(
        nom="paysagiste", pluriel="paysagistes", art="un paysagiste",
        recherche="« paysagiste + votre ville », « entretien jardin », « création terrasse bois »",
        besoins=["Une galerie de vos jardins, saison par saison",
                 "Vos formules d'entretien et vos créations",
                 "Vos zones d'intervention",
                 "Un formulaire de devis avec photos du terrain"],
        angle="Un jardin se vend en images. Votre site transforme chaque chantier terminé en argument pour le suivant."),
}

DEMOS = {
    "plombier": dict(nom="Plomberie Dubreuil", ville="Massy", color="#0b5fa5", accent="#f4a300", tel="01 00 00 00 00",
        baseline="Dépannage et installation, 7 jours sur 7",
        services=[("Dépannage urgent", "Fuite, canalisation bouchée, panne de chauffe-eau : intervention rapide."),
                  ("Chauffe-eau", "Remplacement et installation de chauffe-eau électriques et thermodynamiques."),
                  ("Salle de bain", "Rénovation complète : douche à l'italienne, meubles, robinetterie."),
                  ("Chauffage", "Entretien et remplacement de chaudières et radiateurs.")],
        zones="Massy, Palaiseau, Antony, Verrières-le-Buisson, Igny, Chilly-Mazarin"),
    "electricien": dict(nom="Élec Morel", ville="Arpajon", color="#1d2733", accent="#ffd23f", tel="01 00 00 00 00",
        baseline="Électricité générale, rénovation et mise aux normes",
        services=[("Mise aux normes", "Remplacement de tableau électrique et mise en sécurité de l'installation."),
                  ("Rénovation", "Réfection complète de l'installation électrique en maison et appartement."),
                  ("Borne de recharge", "Installation de bornes pour véhicules électriques."),
                  ("Dépannage", "Recherche de panne et remise en service.")],
        zones="Arpajon, Brétigny-sur-Orge, Saint-Germain-lès-Arpajon, Ollainville, Égly, Breuillet"),
    "coiffeur": dict(nom="Salon Capucine", ville="Yerres", color="#6d2e46", accent="#e8c7a9", tel="01 00 00 00 00",
        baseline="Coiffure femmes, hommes et enfants",
        services=[("Coupe femme", "Shampoing, coupe et brushing."),
                  ("Coupe homme", "Coupe aux ciseaux ou à la tondeuse, barbe."),
                  ("Couleur et balayage", "Coloration, mèches, balayage, soin."),
                  ("Coiffure de mariage", "Essai et coiffure le jour J.")],
        zones="Yerres, Brunoy, Montgeron, Crosne"),
}

def e(s): return html.escape(s, quote=True)

def page(path, title, desc, body, depth=0):
    p = "../" * depth
    canon = f"{BASE}/{path}".replace("/index.html", "/")
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
<header class="top"><div class="wrap">
<a class="logo" href="{p}index.html">Enseigne<span>Web</span></a>
<nav class="main"><a href="{p}index.html#exemples">Exemples</a><a href="{p}index.html#tarifs">Tarifs</a><a href="{p}index.html#questions">Questions</a><a class="btn small" href="{p}index.html#maquette">Ma maquette gratuite</a></nav>
</div></header>
{body}
<footer><div class="wrap"><span>© {BRAND} — sites internet pour artisans et commerces de proximité</span><span><a href="{p}mentions-legales.html">Mentions légales</a></span></div></footer>
<script src="{p}assets/config.js"></script>
<script src="{p}assets/site.js"></script>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")

PRICING = """
<section id="tarifs"><div class="wrap">
<h2>Deux formules. Aucun frais de création.</h2>
<p class="sub">Vous ne payez rien tant que vous n'avez pas vu votre site. Abonnement mensuel, résiliable à tout moment.</p>
<div class="grid g2">
<div class="card plan"><h3>Essentiel</h3><div class="price">59 €<small> / mois</small></div>
<ul><li>Site d'une page, complet et rapide</li><li>Adapté au téléphone</li><li>Bouton d'appel et formulaire de devis</li><li>Hébergement et sécurité inclus</li><li>1 modification par mois</li></ul>
<a class="btn ghost" data-plan="essentiel" href="#maquette">Choisir Essentiel</a></div>
<div class="card plan best"><span class="tag">Recommandé</span><h3>Pro</h3><div class="price">89 €<small> / mois</small></div>
<ul><li>Jusqu'à 6 pages : prestations, réalisations, zones, contact</li><li>Référencement local : une page par prestation et par zone</li><li>Galerie photos de vos chantiers</li><li>Nom de domaine à votre nom inclus</li><li>Modifications illimitées, faites sous 48 h</li></ul>
<a class="btn" data-plan="pro" href="#maquette">Choisir Pro</a></div>
</div></div></section>
"""

FORM = """
<section id="maquette" class="alt"><div class="wrap">
<h2>Recevez votre maquette gratuite sous 48 h</h2>
<p class="sub">Donnez-nous le nom de votre entreprise : nous construisons votre site et vous envoyons le lien. Il vous plaît, vous le gardez. Sinon, vous ne devez rien.</p>
<form class="lead card" id="lead-form">
<div><label for="f-nom">Nom de l'entreprise</label><input id="f-nom" name="Entreprise" required></div>
<div><label for="f-metier">Métier</label><input id="f-metier" name="Métier" required placeholder="Plombier, coiffeur, peintre…"></div>
<div><label for="f-ville">Ville</label><input id="f-ville" name="Ville" required></div>
<div><label for="f-tel">Téléphone</label><input id="f-tel" name="Téléphone" type="tel" required></div>
<div class="full"><label for="f-mail">E-mail (pour recevoir le lien de la maquette)</label><input id="f-mail" name="E-mail" type="email" required></div>
<div class="full"><button class="btn" type="submit">Recevoir ma maquette gratuite</button></div>
<div class="full" id="form-msg" role="status"></div>
</form>
</div></section>
"""

def metier_links(p=""):
    return '<div class="links">' + "".join(
        f'<a href="{p}creation-site-internet-{k}.html">Site internet {e(m["nom"])}</a>' for k, m in METIERS.items()) + "</div>"

def build_home():
    demos = "".join(
        f'<a class="card demo" href="demos/{k}.html"><div class="shot" style="background:{d["color"]}">{e(d["nom"])}</div>'
        f'<div class="meta"><p>{e(METIERS[k]["nom"].capitalize())} — {e(d["ville"])}</p><span>Voir la démonstration →</span></div></a>'
        for k, d in DEMOS.items())
    body = f"""
<section class="hero"><div class="wrap">
<h1>Votre site internet est prêt <em>avant</em> que vous payiez.</h1>
<p class="lead">Nous créons le site de votre entreprise en 48 heures et nous vous l'envoyons. S'il vous plaît, vous le gardez à partir de 59 € par mois. Sinon, vous ne devez rien.</p>
<div class="cta-row"><a class="btn" href="#maquette">Recevoir ma maquette gratuite</a><a class="btn ghost" href="#exemples">Voir des exemples</a></div>
<ul class="ticks"><li>0 € de frais de création</li><li>Sans engagement</li><li>Modifications incluses</li><li>En ligne en 48 h</li></ul>
</div></section>

<section class="alt"><div class="wrap">
<h2>Trois étapes, zéro paperasse</h2>
<p class="sub">Vous avez un métier. Le site, c'est le nôtre.</p>
<div class="grid g3">
<div class="card"><div class="step">Étape 1</div><h3>Vous nous donnez votre nom</h3><p>Entreprise, métier, ville, téléphone. Deux minutes, pas de cahier des charges.</p></div>
<div class="card"><div class="step">Étape 2</div><h3>Nous construisons votre site</h3><p>Textes, mise en page, formulaire de devis, version téléphone. Vous recevez le lien sous 48 heures.</p></div>
<div class="card"><div class="step">Étape 3</div><h3>Vous décidez</h3><p>Le site vous plaît : il est mis en ligne à votre nom. Il ne vous plaît pas : on s'arrête là, sans facture.</p></div>
</div></div></section>

<section id="exemples"><div class="wrap">
<h2>Des exemples à ouvrir tout de suite</h2>
<p class="sub">Trois sites de démonstration, avec des entreprises fictives. Le vôtre sera construit avec votre nom, vos prestations et vos photos.</p>
<div class="grid g3">{demos}</div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Tout est inclus dans l'abonnement</h2>
<p class="sub">Pas de devis à rallonge, pas de facture surprise.</p>
<div class="grid g3">
<div class="card"><h3>Pensé pour être trouvé</h3><p>Des pages construites autour de ce que vos clients tapent dans Google : votre métier, votre ville, vos prestations.</p></div>
<div class="card"><h3>Fait pour le téléphone</h3><p>Un bouton d'appel et un formulaire de devis accessibles d'un seul geste.</p></div>
<div class="card"><h3>Mis à jour pour vous</h3><p>Un nouveau tarif, une photo de chantier, un changement d'horaires : un message suffit.</p></div>
</div></div></section>
{PRICING}
<section class="alt"><div class="wrap">
<h2>Un site adapté à votre métier</h2>
<p class="sub">Chaque métier a ses clients et ses recherches. Nous construisons le site qui correspond aux vôtres.</p>
{metier_links()}
</div></section>

<section id="questions"><div class="wrap prose">
<h2>Questions fréquentes</h2>
<details><summary>Pourquoi la maquette est-elle gratuite ?</summary><p>Parce qu'il est plus simple de juger un site en le voyant qu'en lisant un devis. Si le résultat ne vous convient pas, vous ne payez rien.</p></details>
<details><summary>Y a-t-il un engagement de durée ?</summary><p>Non. L'abonnement est mensuel et vous pouvez l'arrêter à tout moment.</p></details>
<details><summary>Que se passe-t-il si j'arrête l'abonnement ?</summary><p>Le site est mis hors ligne à la fin du mois payé. Le nom de domaine enregistré pour vous peut vous être transféré.</p></details>
<details><summary>Je n'ai ni textes ni photos, est-ce un problème ?</summary><p>Non. Nous rédigeons les textes à partir de votre métier et de vos prestations. Vous pourrez ajouter vos photos quand vous le souhaitez.</p></details>
<details><summary>J'ai déjà un site, pouvez-vous le refaire ?</summary><p>Oui. Envoyez-nous son adresse dans le formulaire : nous vous proposons une nouvelle version, gratuitement, pour comparer.</p></details>
</div></section>
{FORM}"""
    page("index.html", f"{BRAND} — Site internet pour artisans dès 59 €/mois, maquette gratuite",
         "Votre site internet d'artisan ou de commerçant créé en 48 h. Maquette gratuite, 0 € de frais de création, abonnement sans engagement dès 59 €/mois.", body)

def build_metier(k, m):
    besoins = "".join(f"<li>{e(b)}</li>" for b in m["besoins"])
    demo = f'<p><a class="btn ghost" href="demos/{k}.html">Voir un exemple de site de {e(m["nom"])}</a></p>' if k in DEMOS else ""
    body = f"""
<section class="hero"><div class="wrap">
<h1>Création de site internet pour <em>{e(m["nom"])}</em></h1>
<p class="lead">Un site professionnel pour votre activité de {e(m["nom"])}, créé en 48 heures. Vous le voyez avant de payer : maquette gratuite, puis abonnement dès 59 € par mois, sans engagement.</p>
<div class="cta-row"><a class="btn" href="index.html#maquette">Recevoir ma maquette gratuite</a></div>
<ul class="ticks"><li>0 € de frais de création</li><li>Sans engagement</li><li>Modifications incluses</li></ul>
</div></section>
<section class="alt"><div class="wrap prose">
<h2>Pourquoi {e(m["art"])} a besoin d'un site internet</h2>
<p>{e(m["angle"])}</p>
<p>Vos futurs clients cherchent {e(m["recherche"])}. Un site construit autour de ces recherches vous place devant eux au moment précis où ils ont besoin de vous.</p>
<h2>Ce que contient un bon site de {e(m["nom"])}</h2>
<ul>{besoins}</ul>
{demo}
<h2>Combien coûte un site internet de {e(m["nom"])} ?</h2>
<p>Chez {BRAND}, la création est gratuite. Vous payez un abonnement mensuel qui comprend l'hébergement, la sécurité et les modifications : 59 € par mois pour un site d'une page, 89 € par mois pour un site complet avec nom de domaine et référencement local. Vous pouvez arrêter à tout moment.</p>
<h2>Comment ça se passe ?</h2>
<p>Vous remplissez le formulaire en deux minutes. Nous construisons votre site et vous envoyons le lien sous 48 heures. S'il vous plaît, il est mis en ligne à votre nom. Sinon, vous ne devez rien.</p>
</div></section>
{PRICING}
<section class="alt"><div class="wrap"><h2>Autres métiers</h2>{metier_links()}</div></section>"""
    page(f"creation-site-internet-{k}.html", f"Création site internet {m['nom']} — maquette gratuite | {BRAND}",
         f"Site internet pour {m['pluriel']} : créé en 48 h, maquette gratuite, sans engagement, dès 59 €/mois. Référencement local et formulaire de devis inclus.", body)

def build_demo(k, d):
    m = METIERS[k]
    services = "".join(f'<div class="c"><h3>{e(t)}</h3><p>{e(x)}</p></div>' for t, x in d["services"])
    tel = d["tel"].replace(" ", "")
    doc = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(d["nom"])} — {e(m["nom"].capitalize())} à {e(d["ville"])} (site de démonstration)</title>
<meta name="robots" content="noindex">
<style>
*{{box-sizing:border-box}}body{{margin:0;font:17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:#1c1c1c;background:#fff}}
.w{{max-width:1000px;margin:0 auto;padding:0 20px}}
.bar{{background:#111;color:#fff;font-size:14px;padding:8px 0;text-align:center}}.bar a{{color:#fff;font-weight:700}}
header{{background:{d["color"]};color:#fff}}header .w{{display:flex;justify-content:space-between;align-items:center;height:68px}}
.n{{font-weight:800;font-size:21px}}.tel{{background:{d["accent"]};color:#111;font-weight:800;padding:10px 16px;border-radius:8px;text-decoration:none}}
.hero{{background:{d["color"]};color:#fff;padding:60px 0 70px}}.hero h1{{font-size:clamp(30px,5vw,50px);line-height:1.1;margin:0 0 12px;max-width:18ch}}
.hero p{{font-size:20px;opacity:.9;margin:0 0 26px}}
section{{padding:54px 0}}h2{{font-size:30px;margin:0 0 22px}}
.g{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}}.c{{border:1px solid #e5e5e5;border-radius:12px;padding:22px}}.c h3{{margin:0 0 6px}}.c p{{margin:0;color:#555}}
.z{{background:#f6f5f2}}form{{display:grid;gap:12px;max-width:560px}}input,textarea{{padding:13px;border:1.5px solid #ddd;border-radius:8px;font:inherit}}
button{{background:{d["color"]};color:#fff;border:0;padding:14px;border-radius:8px;font:inherit;font-weight:700}}
footer{{background:#111;color:#bbb;padding:24px 0;font-size:14px}}
@media(max-width:700px){{.g{{grid-template-columns:1fr}}}}
</style></head><body>
<div class="bar">Site de démonstration — entreprise fictive. <a href="../index.html#maquette">Recevez le vôtre gratuitement →</a></div>
<header><div class="w"><span class="n">{e(d["nom"])}</span><a class="tel" href="tel:{tel}">☎ {e(d["tel"])}</a></div></header>
<div class="hero"><div class="w"><h1>{e(m["nom"].capitalize())} à {e(d["ville"])} et alentours</h1><p>{e(d["baseline"])}</p><a class="tel" href="#devis">Demander un devis gratuit</a></div></div>
<section><div class="w"><h2>Nos prestations</h2><div class="g">{services}</div></div></section>
<section class="z"><div class="w"><h2>Zones d'intervention</h2><p>{e(d["zones"])}.</p></div></section>
<section id="devis"><div class="w"><h2>Demande de devis</h2>
<form onsubmit="event.preventDefault();this.querySelector('button').textContent='Formulaire de démonstration';"><input placeholder="Votre nom" required><input placeholder="Votre téléphone" required><textarea rows="4" placeholder="Décrivez votre besoin"></textarea><button>Envoyer ma demande</button></form></div></section>
<footer><div class="w">{e(d["nom"])} — {e(d["ville"])} · Site de démonstration réalisé par <a style="color:#fff" href="../index.html">{BRAND}</a></div></footer>
</body></html>
"""
    (ROOT / "demos").mkdir(exist_ok=True)
    (ROOT / "demos" / f"{k}.html").write_text(doc, encoding="utf-8")

def build_legal():
    body = """<section><div class="wrap prose"><h1>Mentions légales</h1>
<p><strong>Éditeur du site :</strong> [nom et prénom ou dénomination — à compléter]</p>
<p><strong>Statut et numéro SIRET :</strong> [à compléter]</p>
<p><strong>Adresse :</strong> [à compléter]</p>
<p><strong>Contact :</strong> [adresse e-mail — à compléter]</p>
<p><strong>Directeur de la publication :</strong> [à compléter]</p>
<p><strong>Hébergeur :</strong> GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
<h2>Données personnelles</h2>
<p>Les informations saisies dans le formulaire (entreprise, métier, ville, téléphone, e-mail) servent uniquement à préparer et à envoyer la maquette demandée. Elles ne sont ni vendues ni transmises à des tiers. Vous pouvez demander leur suppression à l'adresse de contact ci-dessus.</p>
</div></section>"""
    page("mentions-legales.html", f"Mentions légales | {BRAND}", "Mentions légales du site Enseigne Web.", body)

def build_seo_files():
    urls = ["", "mentions-legales.html"] + [f"creation-site-internet-{k}.html" for k in METIERS]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
        "".join(f"  <url><loc>{BASE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sm, encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /demos/\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")

if __name__ == "__main__":
    build_home()
    for k, m in METIERS.items(): build_metier(k, m)
    for k, d in DEMOS.items(): build_demo(k, d)
    build_legal(); build_seo_files()
    print("Site généré.")
