# -*- mode: python ; coding: utf-8 -*-

import sys

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['e:\\download\\wechatbot'],
    binaries=[],
    datas=[
        ('e:\\download\\wechatbot\\llm', 'llm'), # 包含llm目录及其内容
        ('e:\\download\\wechatbot\\utils', 'utils'), # 包含utils目录及其内容

    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['config.json'], # 排除根目录的config.json
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='wechatbot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_info_entries=None,
    console=True, # 如果需要控制台窗口，设置为True；如果不需要，设置为False
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)


# 如果你希望生成一个单文件exe，请取消注释下面的COLLECTION部分
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='wechatbot'
)