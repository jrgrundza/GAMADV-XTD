# -*- mode: python -*-
a = Analysis(['gam.py'],
             pathex=['C:\\GAMADV-XTD'],
             hiddenimports=[],
             hookspath=None,
             excludes=['_tkinter'],
             runtime_hooks=None)
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break
a.datas += [('httplib2/cacerts.txt', 'httplib2\cacerts.txt', 'DATA')]
a.datas += [('admin-settings-v2.json', 'admin-settings-v2.json', 'DATA')]
a.datas += [('cloudprint-v2.json', 'cloudprint-v2.json', 'DATA')]
a.datas += [('contacts-v3.json', 'contacts-v3.json', 'DATA')]
a.datas += [('email-audit-v1.json', 'email-audit-v1.json', 'DATA')]
a.datas += [('email-settings-v2.json', 'email-settings-v2.json', 'DATA')]
a.datas += [('sites-v1.json', 'sites-v1.json', 'DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gam.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
