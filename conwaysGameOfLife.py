#    An Implementation of Conway's Game of Life with A Few *Relatively* Nice Features and Design Aspects
#    Copyright (C) 2020  David Bayani
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np;
import scipy.signal as sig;



#
#
# NOTE: for the "interesting" boards that have highest number, 
#     this code can probably be sped up further by using sparce
#     matrices - at least the computation of the game time-steps.
#     Right now, however, the main slow-down and bottle neck is
#     the method used to form images and the gif after.
#
#


def stepGameOfLife(frame):
    A = sig.convolve( frame, np.ones((3,3), dtype=np.int8) , mode="same");
    assert(A.dtype == np.dtype('int8'));
    assert(A.shape == frame.shape);
    # first summand: if the grid location has a value of 3, then either it is
    # alive and has two neighbors or dead and has three neighors.
    #
    # second summand: if a grid location has value 4 and the cell there is alive,
    #     then it means it has three neighbors, so stay alive...
    result=  np.asarray(  (A - 3) ** 2 == 0 , dtype=np.int8) + \
        frame * np.asarray(  (A - 4) ** 2 == 0 , dtype=np.int8);
    assert(result.dtype == np.dtype('int8'));
    assert(result.shape == frame.shape);
    return result;

def enlargePriorToPrinting(frame, integerNumberOfTimesLarger):
    return np.kron(frame, np.ones( (integerNumberOfTimesLarger, integerNumberOfTimesLarger) ));

def simplyPrettyPrint(frame):
    printP = lambda x : "_" if( x == 0 ) else "#";
    initialMatrixOfStrings = str(np.vectorize(printP)(frame)); #np.array(list(map(printP, frame))));
    print(initialMatrixOfStrings.replace("' '", "").replace("_", " "), flush=True);

from PIL import Image;

def getInitialBoard(frame_numberRows, frame_numberCols): 
    A = np.zeros((3, 3), dtype=np.int8);
    A[1,0] = 1; A[2,1] = 1; A[:3, 2] = 1;
    # Why 0.88 below? The neighborhood of a cell is 9 elements (including the center), so if we 
    # fill a slot with probability 1/9, then in expectation there is one "element" per neighborhood
    # (so less likely to choke), and 0.88 is a little less than 1- (1/9) (so we fill a bit more 
    # often than we would otherwise).
    C = np.asarray( np.random.rand(int(frame_numberRows / 3), int(frame_numberCols/3)) >=0.88, dtype=np.int8);
    D = np.zeros((frame_numberRows, frame_numberCols),dtype=np.int8);
    E=np.kron(C,A);
    D[:(E.shape[0]), :(E.shape[1])] = E;
    return D;


factorToEnlargeImageBy=5;
assert(isinstance(factorToEnlargeImageBy, int));
frame_numberCols=150;
frame_numberRows=150;
maxNumberFrames=1200;
mutationPropotionParam=0.25; # When this is 1.0, we expect one random injection per time-step,
    # when it is higher than 1.0, we expect fewer than one per time-step, and less than 1.0 implies
    # higher than one injection per time-step...
assert(mutationPropotionParam > 0);

# Below the multiplication by four is because for roughly every one character we insert,
# numpy adds three character (the "' '" between entries), which we happen to remove in 
# the simplyPrettyPrint function prior to printing
np.set_printoptions(threshold=np.inf, \
                    linewidth=(4*factorToEnlargeImageBy * frame_numberCols + 8) ); # So that matrices are printed without truncation
#    See: https://stackoverflow.com/questions/1987694/how-to-print-the-full-numpy-array-without-truncation
#    and https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html

arrays = [];
for thisChannel in range(0,3):
    A= getInitialBoard(frame_numberRows, frame_numberCols);
    B =np.zeros((frame_numberRows, frame_numberCols),dtype=np.int8)
    arrays.append([]);
    C = np.zeros((frame_numberRows, frame_numberCols),dtype=np.int8);
    for thisIndex in range(0, maxNumberFrames):

        if(thisIndex % 20 == 0):
            if( np.all(C == A)):
                break; # to handle a common case where the board devolves into binary oscillators...
            C = A;
        arrays[-1].append(A);

        mutationRate=1.0- ( 1.0 / (frame_numberRows * frame_numberCols * mutationPropotionParam));
        randomMutation = np.asarray( \
            np.random.rand(frame_numberRows, frame_numberCols) >= mutationRate ,
            dtype=np.int8);
        assert(randomMutation.shape == A.shape);
        A=stepGameOfLife(A) ^ randomMutation;
        assert(np.all( A * (A - 1) == 0));

    arrays[-1].append(A);

    print("Number of frames: " + str(len(arrays[-1])), flush=True);

maxTimeStep= max([len(x) for x in arrays]);

images=[];
for thisIndex in range(0, maxTimeStep):
    temp2 = np.zeros(( frame_numberRows * factorToEnlargeImageBy, \
                       frame_numberCols * factorToEnlargeImageBy, \
                       3  ),dtype=np.uint8);
    for thisChannel in [0,1,2]:
        temp =enlargePriorToPrinting(\
            arrays[thisChannel][min(thisIndex, len(arrays[thisChannel]) -1)],\
            factorToEnlargeImageBy);
        temp2[:,:,thisChannel] = 255 * temp;
    # I would prefer to use mode "L" below (see https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes )
    # but for some reason PIL won't allow it....
    images.append(
        Image.fromarray(temp2, mode="RGB") \
    );

# https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving-sequences
lengthToDisplaySingleFrame= int(1000.0 / 60.0); # 60 frames per 1000 milliseconds
images[0].save('./simpleConwaysGameOfLife_imagedraw.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=lengthToDisplaySingleFrame, loop=0, mode="RGB")


