import os
import PyInstaller.__main__

script_dir = os.path.dirname(os.path.abspath(__file__))
main_script = os.path.join(script_dir, 'main.py')
icon_file = os.path.join(script_dir, 'Blot.ico')

if not os.path.exists(icon_file):
    raise FileNotFoundError(f"Icon file not found: {icon_file}")

# Create spec file content using os.path.normpath for paths
spec_content = '''
a = Analysis(
    [r'{}'],
    pathex=[r'{}'],
    hiddenimports=['PIL', 'PIL._tkinter_finder', 'scipy.stats', 'scipy.special._ufuncs_cxx'],
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='BlotQuant',
    debug=False,
    strip=False,
    upx=True,
    console=False,
    icon=r'{}'
)
'''.format(
    os.path.normpath(main_script),
    os.path.normpath(script_dir),
    os.path.normpath(icon_file)
)

# Write spec file
with open('BlotQuant.spec', 'w') as f:
    f.write(spec_content)

# Run PyInstaller with spec file
PyInstaller.__main__.run(['BlotQuant.spec'])