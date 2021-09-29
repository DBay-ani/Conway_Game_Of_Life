
# An Implementation of Conway's Game of Life with A Few *Relatively* Nice Features and Design Aspects
>   Copyright (C) 2020  David Bayani
>
>   This program is free software: you can redistribute it and/or modify
>   it under the terms of the GNU General Public License as published by
>   the Free Software Foundation, either version 3 of the License, or
>   (at your option) any later version.
>
>   This program is distributed in the hope that it will be useful,
>   but WITHOUT ANY WARRANTY; without even the implied warranty of
>   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
>   GNU General Public License for more details.
>
>   You should have received a copy of the GNU General Public License
>   along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Description

This repo contains an implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
that I put together in late fall, 2020. This implementation has some relatively
nice features and efficient state-stepping, 
**compared to a very basic implementation**
that someone might put together in 7 minutes using only lists, loops, and
dumping text to terminal. I am far from claiming that this code has much to 
offer to the Game of Life extreme-enthusiast, who can find many hyper-optimized, 
feature-rich implementations in the world. That said, maybe this will be useful 
for a technically-inclined person who simply wants a reasonable-but-straightforward
implementation for (a) use in a larger project (for instance, as example of 
a discrete dynamical system with rich behavior, for testing) (b) just to
fiddle around with. For the non-extreme-enthusiast, I am sure they can find many 
repos with worthwhile code, and *maybe* this will be one of them.

### Capabilities

As shown in the example-GIF, this code can produce GIFs of results.
In the GIF, the red, blue, and green channels are all independent evolutions
of independent starting states, overlaid onto on a single image.

The code also supports text-output, printing frames as a series of 
ASCII text to terminal. If you would like
to re-implement text-printing, then see the functions
enlargePriorToPrinting and simplyPrettyPrint, which can be used to print
a reasonably-sized frame to terminal.

In addition to changing the size of grid and visualization aspect, the code
also allows you to inject random noise/perturbations into the grid. 
Depending on your goals, this feature may either sound worthwhile or entirely
useless. Either way, see the variable named "mutationPropotionParam" 
for how to control the random noise injection.

![An Example GIF Output](./example.gif)

Regarding the example-GIF included here: it was taken as the first 95MB (roughly) of the GIF in
simpleConwaysGameOfLife_imagedraw.gif.gz. The rest of the GIF (roughly 1.7MB total) can be found in
simpleConwaysGameOfLife_imagedraw.gif.gz ; due to GitHub's restrictions on the maximum size of a 
file for upload, this GIF could not be displayed here.

If you look closely at this example GIF, you will see the spots here-and-there 
where a square has been randomly turned "on" in one of the channels.

### Code Quality 

The code quality is not fantastic, but it is also not horrible. Hopefully, those who
are programming-inclined will find it easy enough to consume, though far from an
ideal example of how to ship code.

Certainly,
more effort could be put in to making a proper terminal-input interface. However,
this was designed in the process of my tinkering, so the variables of interest
are assigned internally to hard-values. If this worries you, take a glance over
conwaysGameOfLife.py and determine whether you want to use this or go elsewhere.

My intent here is to release what I have written that others might find of 
interest - not to invest any additional effort to make the program  conform closer with my 
judgment of what code with a proper interface and structure looks like.

### Some Metadata

Using script located in 
[another repo of mine](https://github.com/DBay-ani/information_preservation_and_backup_notes_and_info/tree/master/scriptsForCollectingFileMetadata), this is some older metadata for the code and larger GIF included, prior to
my addition of the license header on the code and minor wording correction in the python file.

>
> b6eada5f3ff3a3a6ee19cfc09dd5a88cb218c8c956c538f1e185b1c9b233d224eb8bdebf5b12c439350045cee08fc901cdc812c8c8f4f28d98592120c6840095,regular file,12,512,5422,-,0,2021-09-28 03:41:39.099979335 +0000,1632800499,2020-11-11 00:33:54.399335726 +0000,1605054834,2021-01-19 07:13:32.634297833 +0000,1611040412,./conwaysGameOfLife.py
> 74a4c156c8ecefbca1e1c1076a65e14da0951fc82f31bdbbaabe5ba0e38df5a7e3d2240010d6398cb18f334a320a4ad3d6fabce7679ecf39b8bc3ee43ac13767,regular file,339864,512,174002354,-,0,2021-09-28 03:44:26.935331230 +0000,1632800666,2020-11-10 19:33:25.378729782 +0000,1605036805,2020-11-10 19:37:23.133636061 +0000,1605037043,./simpleConwaysGameOfLife_imagedraw.gif
>


