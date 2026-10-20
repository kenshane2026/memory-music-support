"""Product landing page. Only existing features; no invented store availability."""
from html import escape


def render_home(lang, email):
    zh = lang == 'zh'
    base = '/memory-music-support/'
    prefix = base if zh else base + 'en/'
    tr = lambda a, b: a if zh else b
    icon = base + 'icon.png'
    assets = base + 'assets/'
    title = tr('每首歌，<br>都有你的故事。', 'Every song.<br>A story of yours.')
    return f'''<!doctype html>
<html lang="{'zh-CN' if zh else 'en'}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Memory Music · {tr('让音乐，留在你的故事里','Your music, your memories')}</title>
<meta name="description" content="{tr('为自己的音乐建立一个家。用标签、智能分类、歌单和音乐记忆，整理本地音乐；支持 iCloud 整理信息同步与备份。','A home for your local music. Organize with tags, smart collections, playlists and personal notes, with organization sync and backups.')}">
<meta name="theme-color" content="#faf8f5"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'self'; img-src 'self' data:; object-src 'none'; base-uri 'self'; form-action 'none'">
<link rel="icon" href="{icon}"><link rel="stylesheet" href="{base}style.css"><link rel="stylesheet" href="{base}product.css"></head>
<body class="product"><a class="skip" href="#main">{tr('跳至正文','Skip to content')}</a>
<header><a class="brand" href="{prefix}"><img src="{icon}" width="42" height="42" alt=""><span>Memory Music<small>{tr('音乐与记忆','MUSIC & MEMORIES')}</small></span></a>
<nav aria-label="{tr('主导航','Main navigation')}"><a href="#features">{tr('功能','Features')}</a><a href="#your-library">{tr('你的资料','Your library')}</a><a href="{prefix}support/">{tr('支持','Support')}</a><a class="language" href="{base+'en/' if zh else base}">{tr('EN','中文')}</a></nav></header>
<main id="main">
<section class="product-hero">
 <div class="hero-copy"><p class="eyebrow">YOUR MUSIC. YOUR MEMORIES.</p><h1>{title}</h1>
 <p class="hero-lead">{tr('给自己的音乐，一个用心整理的家。<br>用标签找到心情，用文字留下记忆，<br>让喜欢的歌陪你走得更远。','A thoughtful home for the music you own.<br>Find a mood with tags. Keep a moment in words.<br>Carry your favorite songs a little further.')}</p>
 <div class="hero-actions"><a class="button primary" href="#features">{tr('探索 Memory Music','Explore Memory Music')} <span>↓</span></a><a class="text-link" href="#screens">{tr('看看应用界面','See the app')} ↗</a></div>
 <div class="platforms"><span class="platform-dot"></span> Mac <i>·</i> iPhone <i>·</i> iPad <span class="release-status">{tr('发布准备中','Preparing for release')}</span></div></div>
 <figure class="hero-product" aria-label="{tr('应用示例界面','App preview with sample content')}">
  <div class="desktop-frame"><div class="window-bar"><span></span><span></span><span></span><b>Memory Music</b></div><img src="{assets}mac-library.png" width="2560" height="1600" alt="{tr('Mac 音乐库：歌曲、艺术家和专辑，使用虚构歌曲资料','Mac music library showing fictional songs, artists and albums')}" fetchpriority="high"></div>
  <div class="phone-frame"><div class="phone-cap"></div><img src="{assets}iphone-tags.png" width="1206" height="2622" alt="{tr('iPhone 标签页面，使用示例分类','iPhone tags page with sample categories')}"></div>
  <figcaption>{tr('真实应用界面 · 示例歌曲与自制封面','Real app interface · Fictional songs and original artwork')}</figcaption>
 </figure>
</section>
<div class="intro-line"><span>01 — {tr('为喜欢的音乐，留一个位置','MAKE ROOM FOR THE MUSIC YOU LOVE')}</span><p>{tr('音乐在本地，整理有自己的方式。','Music on your devices. Organization on your terms.')}</p></div>
<section class="feature-story" id="features">
 <div class="story-copy"><p class="eyebrow">A LIBRARY THAT FEELS LIKE YOU</p><h2>{tr('按自己的方式，<br>找到那一首。','Find that song.<br>Your own way.')}</h2><p>{tr('艺术家、专辑，是音乐的线索。<br>日落、雨天、在路上，是你的线索。<br>把歌曲放进属于自己的标签与分类里，下一次，顺着心情找到它。','Artists and albums tell one part of the story.<br>Sunsets, rainy days and open roads tell yours.<br>Give songs your own tags and collections, then find them by the way they feel.')}</p>
 <div class="tag-samples" aria-label="{tr('标签示例','Sample tags')}"><span>{tr('日落时分','Sunset')}</span><span>{tr('雨天散步','Rainy walks')}</span><span>{tr('在路上','On the road')}</span></div>
 <dl class="feature-facts"><div><dt>{tr('本地音乐库','Local library')}</dt><dd>{tr('选择音乐目录，按歌曲、艺术家或专辑浏览。','Choose music folders; browse songs, artists and albums.')}</dd></div><div><dt>{tr('标签与分组','Tags & groups')}</dt><dd>{tr('自由建立标签，用自己的语言组织音乐。','Create personal tags and organize them into groups.')}</dd></div></dl></div>
 <figure class="tags-preview"><div class="image-label"><span>MEMORY MUSIC</span><b>{tr('标签，让喜好有迹可循。','Tags make it personal.')}</b></div><img src="{assets}mac-tags.png" width="2560" height="1600" alt="{tr('应用真实标签页面，示例标签带有自制抽象封面','Real tags screen with sample tags and original abstract cover art')}" loading="lazy"></figure>
</section>
<section class="memory-story"><div class="memory-heading"><p class="eyebrow">MORE THAN A SONG</p><h2>{tr('有些旋律，<br>记得你忘不了的事。','Some melodies<br>keep a moment alive.')}</h2><p>{tr('为歌曲写下自己的记忆与备注。<br>让再次响起的，不只有音乐。','Keep personal notes and memories with a song.<br>Hear more than the music when it plays again.')}</p></div><div class="memory-paper"><span class="paper-overline">{tr('音乐记忆 · 文字示例','A MUSIC MEMORY · SAMPLE NOTE')}</span><div class="paper-rule"></div><blockquote>{tr('那天的风很轻，<br>回家的路突然变得很长。<br><br>一首歌，留住一个傍晚。','The breeze was soft.<br>The walk home felt a little longer.<br><br>One song, one evening to keep.')}</blockquote><div class="note-track"><span class="note-cover">♪</span><div><b>{tr('把日落装进口袋','A Pocketful of Sunset')}</b><small>Memory Music · {tr('虚构示例歌曲','FICTIONAL SAMPLE SONG')}</small></div><span>♡</span></div></div></section>
<section class="listen-story" id="screens"><div class="section-heading"><div><p class="eyebrow">ROOM FOR EVERY MOOD</p><h2>{tr('从认真整理，<br>到自在聆听。','Thoughtfully organized.<br>Ready to listen.')}</h2></div><p>{tr('智能分类与歌单，让合适的音乐聚在一起。<br>从一个清晨，到一段旅程，都有自己的播放方式。','Bring the right music together with smart collections and playlists.<br>Make room for a quiet morning or the next journey.')}</p></div>
<div class="listen-grid"><figure class="spaces-preview"><img src="{assets}mac-spaces.png" width="2560" height="1600" alt="{tr('音乐空间的智能分类界面，使用示例资料','Music Spaces smart collection screen with sample content')}" loading="lazy"><figcaption>{tr('音乐空间 · 示例资料','Music Spaces · Sample content')}</figcaption></figure><div class="listen-details"><article><span>01</span><div><h3>{tr('智能分类与歌单','Smart collections & playlists')}</h3><p>{tr('按标签等规则汇集歌曲，也可以保留一份自己喜欢的歌单。','Gather songs using tag-based rules, or keep a playlist you love.')}</p></div></article><article><span>02</span><div><h3>{tr('播放队列与后台聆听','Queues & background listening')}</h3><p>{tr('管理下一首，使用顺序、循环与随机播放，让音乐自然延续。','Shape what plays next with queues, sequential playback, repeat and shuffle.')}</p></div></article><article><span>03</span><div><h3>{tr('资料与封面补全','Metadata & artwork lookups')}</h3><p>{tr('需要时主动查找歌曲资料或封面，预览后选择应用。','Request metadata or artwork when you need it, then preview and choose what to apply.')}</p></div></article></div></div></section>
<section class="ownership" id="your-library"><div class="ownership-title"><p class="eyebrow">YOUR LIBRARY, IN YOUR HANDS</p><h2>{tr('陪你跨过设备，<br>也留住掌控感。','Across your devices.<br>Still in your hands.')}</h2></div><div class="ownership-grid"><article><span class="ownership-icon">↳</span><h3>{tr('原始音乐保留在本机','Original music stays local')}</h3><p>{tr('音乐文件由你自行准备与保管。应用不提供音乐下载，也不将原始音频上传到 CloudKit。','Bring and keep your own music files. The app does not supply music downloads or upload original audio to CloudKit.')}</p></article><article><span class="ownership-icon">⇄</span><h3>{tr('同步整理信息','Sync your organization')}</h3><p>{tr('通过同一 iCloud 账户的私人数据库，同步标签、歌单、记忆等整理资料。每台设备仍需自己的音乐文件。','Use a private iCloud database to sync tags, playlists, notes and other organization information. Each device still needs its own music files.')}</p></article><article><span class="ownership-icon">↗</span><h3>{tr('备份与恢复','Back up & restore')}</h3><p>{tr('导出支持的整理资料和用户资源，保留自己的备份。同步不代替原始音乐文件备份。','Export supported organization information and user resources. Keep your own backups; sync does not replace audio-file backups.')}</p></article></div><a class="text-link" href="{prefix}privacy/">{tr('了解具体的数据处理方式','Read how information is handled')} ↗</a></section>
<section class="release-block"><img src="{icon}" width="72" height="72" alt=""><p class="eyebrow">MEMORY MUSIC</p><h2>{tr('让喜欢的歌，<br>留在生活里。','Keep the music you love.<br>Keep it in your life.')}</h2><p>{tr('Mac、iPhone 与 iPad 版本正在进行正式发布准备。<br>下载、价格和可用地区将以上架时的信息为准。<br>当前主要界面为简体中文。','Preparing the Mac, iPhone and iPad editions for release.<br>Download details, prices and availability will be announced with the release.<br>The app interface is currently primarily Simplified Chinese.')}</p><a class="button primary" href="{prefix}support/">{tr('使用支持与联系','Support & contact')} <span>↗</span></a><small>{tr('本页为产品介绍；界面配图使用示例内容。','Product introduction. App images use sample content.')}</small></section>
</main><footer><a class="footer-brand" href="{prefix}">Memory Music</a><p>{tr('用音乐记录生活的每一刻。','A soundtrack to the moments you keep.')}</p><div><a href="{prefix}privacy/">{tr('隐私政策','Privacy')}</a><a href="{prefix}support/">{tr('使用支持','Support')}</a><a href="mailto:{escape(email)}">{escape(email)}</a></div><small>© 2026 Memory Music</small></footer></body></html>'''
