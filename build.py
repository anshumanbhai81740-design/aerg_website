from pathlib import Path
import base64,json
p=Path(__file__).parent
css=(p/'styles.css').read_text()
js=(p/'app.js').read_text()
image='data:image/png;base64,'+base64.b64encode((p/'hero-reference.png').read_bytes()).decode()
logo='data:image/png;base64,'+base64.b64encode((p/'aerg-logo.png').read_bytes()).decode()
html='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="AERG — Avanī Ecosystem Restoration Group"><title>AERG | Restoring ecosystems</title><style>'+css+'</style></head><body><div id="app"></div><script>window.AERG_IMAGE='+json.dumps(image)+';window.AERG_LOGO='+json.dumps(logo)+';</script><script id="site-code">'+js+'</script></body></html>'
(p/'index.html').write_text(html)
print('Rebuilt website')
