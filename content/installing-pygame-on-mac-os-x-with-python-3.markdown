Title: Installing Pygame on Mac OS X with Python 3
date: 2014-03-11 16:22
slug: installing-pygame-on-mac-os-x-with-python-3


This has been a bugbear of mine for sometime now. I like using Python 3.x. I like teaching kids how to use Pygame. I use a Mac.
Trying to get all three to play nicely with each other has been impossible for me up to now.

I've trawled through web pages and blog posts that recommend all manner of ways in which you can install Pygame on a Mac for Python 3, I've tried numerous solutions on StackOverflow, and I've even tried angrily shouting at my computer and threatening to throw it out of my classroom window. None of them worked.

Today I finally nailed it, and I have Pygame running. Here' what I did.

	1) Install XCode and command line tools
	2) Install Homebrew (ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)")
	3) brew install Python3
	4) brew install git
	5) brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
	6) Install XQuartz - http://xquartz.macosforge.org
	7) brew tap homebrew/headonly
	8) brew install --HEAD smpeg
	9) brew install python (needed to install mercurial)
	10) brew install mercurial
	11) pip3 install hg+http://bitbucket.org/pygame/pygame

And that's it. If you have any problems yourself or a better way then please let me know in the comments.

<del><em>note: the smpeg install is failing for me at the moment, so I'll look into this a little more. Pygame seems to be working without it though.</em></del>

_update_

I had some _brew doctor_ issues (around 20!), which might have been due to me trying to install Pygame from source earlier and therefore manually installing all the dependencies, which then conflicted with homebrew.

I deleted everything brew doctor suggested and overwrote all links as suggested. The `brew install --HEAD smpeg` suddenly worked (although that might have been because I was no longer behind a proxy). I then did a `brew unlink jpeg` and `brew link --overwrite jpeg`.

Everything is working perfectly for now. (Crosses fingers, touches wood and searches for a black cat to cross his path.)
