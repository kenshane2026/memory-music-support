#!/usr/bin/env python3
"""Build static, bilingual privacy/support pages without third-party scripts."""
from pathlib import Path
from html import escape as e
import json
import shutil
from product_home import render_home

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'content.json').read_text())
out = ROOT / 'docs'
out.mkdir(exist_ok=True)
shutil.copyfile(ROOT / 'assets/icon.png', out / 'icon.png')

def page(lang, kind):
    zh = lang == 'zh'
    if kind == 'home':
        dest = out / ('' if zh else 'en')
        dest.mkdir(parents=True, exist_ok=True)
        (dest / 'index.html').write_text(render_home(lang, data['email']))
        return
    prefix = '' if zh else '/en'
    privacy, support = ('隐私政策', '使用支持') if zh else ('Privacy', 'Support')
    title = {'home': '让音乐，留在你的故事里。' if zh else 'Keep your music. Keep your stories.',
             'privacy': '你的音乐，\n由你掌握。' if zh else 'Your music.\nYour control.',
             'support': '需要帮助时，\n我们在这里。' if zh else 'A little help,\nwhen you need it.'}[kind]
    section = 'MEMORY MUSIC' if kind == 'home' else ('PRIVACY POLICY' if kind == 'privacy' else 'SUPPORT')
    lead = {'home': '本地音乐整理与聆听。用标签、歌单和记忆，留下属于你的音乐故事。' if zh else 'A home for local music, organized with tags, playlists and the memories you make.',
            'privacy': '了解本机资料、iCloud 同步和主动触发的在线查询如何处理信息。' if zh else 'Understand local information, iCloud synchronization and the online lookups you choose.',
            'support': '从添加音乐到同步与备份，先看常见问题，也可以直接联系开发者。' if zh else 'Find practical help with your music, synchronization and backups, or contact the developer.'}[kind]
    alternate = ('/en' if zh else '') + ('/' if kind == 'home' else '/' + kind + '/')
    nav = f'<a href="{prefix}/privacy/">{privacy}</a><a href="{prefix}/support/">{support}</a><a class="language" href="{alternate}">{"English" if zh else "简体中文"}</a>'
    if kind == 'home':
        body = f'''<section class="home-links"><a class="feature" href="{prefix}/privacy/"><span>01 · PRIVACY</span><h2>{'清楚知道资料去向' if zh else 'Know where your information goes'}</h2><p>{'原始音乐保留在本机；整理信息与在线查询分别说明。' if zh else 'Original music stays on your devices. Organization sync and optional lookups are explained separately.'}</p><b>{privacy} ↗</b></a><a class="feature" href="{prefix}/support/"><span>02 · SUPPORT</span><h2>{'遇到问题，有处可问' if zh else 'Find a way forward'}</h2><p>{'目录授权、同步、备份和问题反馈，从这里开始。' if zh else 'Start here for directory access, synchronization, backups and issue reports.'}</p><b>{support} ↗</b></a></section><p class="release-note">{'发布准备中。正式下载信息将在上架后提供。' if zh else 'Preparing for release. Download information will be added when the app is available.'}</p>'''
    else:
        items = data[kind][lang]
        toc = ''.join(f'<a href="#section-{i}"><span>{i:02}</span>{e(t)}</a>' for i,(t,_) in enumerate(items,1))
        sections = ''.join(f'<section class="article-section" id="section-{i}"><span class="number">{i:02}</span><div><h2>{e(t)}</h2><p>{e(b)}</p></div></section>' for i,(t,b) in enumerate(items,1))
        contact = f'<aside class="contact"><span>{"联系我们" if zh else "CONTACT"}</span><a href="mailto:{data["email"]}">{data["email"]} ↗</a><p>{"请不要在邮件中提供密码或完整私人资料。" if zh else "Please do not email passwords or complete private libraries."}</p></aside>'
        refs = ''
        if kind == 'privacy':
            refs = '<p class="references"><a href="https://www.apple.com/legal/privacy/">Apple Privacy</a> · <a href="https://musicbrainz.org/doc/About/Privacy_Policy">MusicBrainz Privacy</a> · <a href="https://acoustid.org/">AcoustID</a> · <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy</a></p>'
        body = f'<div class="document"><aside class="toc"><p>{"本页内容" if zh else "ON THIS PAGE"}</p>{toc}</aside><article>{sections}{refs}{contact}</article></div>'
    html = f'''<!doctype html>
<html lang="{'zh-CN' if zh else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Memory Music · { {'home':'隐私与支持' if zh else 'Privacy & Support','privacy':privacy,'support':support}[kind] }</title><meta name="description" content="{e(lead)}"><meta name="theme-color" content="#faf8f5"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'self'; img-src 'self' data:; object-src 'none'; base-uri 'self'; form-action 'none'"><link rel="icon" href="/icon.png"><link rel="stylesheet" href="/style.css"></head><body><a class="skip" href="#main">{'跳至正文' if zh else 'Skip to content'}</a><header><a class="brand" href="{prefix}/"><img src="/icon.png" width="40" height="40" alt=""><span>Memory Music<small>{'音乐与记忆' if zh else 'MUSIC & MEMORIES'}</small></span></a><nav aria-label="{'导航' if zh else 'Navigation'}">{nav}</nav></header><main id="main"><section class="hero"><p class="eyebrow">{section}</p><h1>{e(title).replace(chr(10),'<br>')}</h1><p class="lead">{e(lead)}</p><p class="updated">{'更新于' if zh else 'Updated'} 2026.10.20 <span>·</span> {'隐私与支持' if zh else 'Privacy & Support'}</p></section>{body}</main><footer><a class="footer-brand" href="{prefix}/">Memory Music</a><p>{'用音乐记录生活的每一刻。' if zh else 'A soundtrack to the moments you keep.'}</p><div><a href="{prefix}/privacy/">{privacy}</a><a href="{prefix}/support/">{support}</a><a href="mailto:{data['email']}">{data['email']}</a></div><small>© 2026 Memory Music</small></footer></body></html>'''
    dest = out / ('en' if not zh else '') / ('' if kind == 'home' else kind)
    dest.mkdir(parents=True, exist_ok=True)
    html = html.replace('href="/', 'href="/memory-music-support/').replace('src="/', 'src="/memory-music-support/')
    (dest / 'index.html').write_text(html)

for lang in ['zh', 'en']:
    for kind in ['home', 'privacy', 'support']:
        page(lang, kind)
shutil.copyfile(ROOT / 'style.css', out / 'style.css')
(out / 'robots.txt').write_text('User-agent: *\nAllow: /\n')
print('Built 6 static pages with local styles and artwork.')

shutil.copyfile(ROOT / 'product.css', out / 'product.css')
shutil.copyfile(ROOT / 'product.js', out / 'product.js')
shutil.copytree(ROOT / 'assets/product', out / 'assets', dirs_exist_ok=True)
(out / '.nojekyll').touch()
