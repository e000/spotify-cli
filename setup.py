from setuptools import setup

setup(
    name = 'spotify-cli',
    version = '0.2-dev',
    license='MIT',
    author='Edgeworth E. Euler',
    author_email = 'e@encyclopediadramatica.se',
    description = 'Command line utils for spotify.',
    platforms = 'any',
    packages = [
        'spotify_cli'
    ],
    package_dir = {
        'spotify_cli': 'src'
    },
    entry_points = """
    [console_scripts]
    splay=spotify_cli.cli:play
    spause=spotify_cli.cli:pause
    sinfo=spotify_cli.cli:info
    """

)