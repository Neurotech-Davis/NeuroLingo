#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on February 20, 2025, at 20:47
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from Set_Counterbalance_Here_And_NumReps
numReps = 8

# This is the amount of repetitions
# for each set of words.
# Usually we set it to 8, but for debugging set it to 1.
# Run 'Before Experiment' code from codeLoader
import random


characters_words = {}
space = '-'

# This is just a helper
# function that we use for testing phase diamonds
def center_string(a_string, b_string, return_string):
    # Identify the larger and smaller strings
    if len(a_string) >= len(b_string):
        larger_string = a_string
        smaller_string = b_string
    else:
        larger_string = b_string
        smaller_string = a_string

    # Calculate the total padding needed
    total_padding = len(larger_string) - len(smaller_string)
    
    # Calculate padding on each side
    right_padding = total_padding // 2
    left_padding = total_padding - right_padding
    
    # Center the smaller_string within the larger_string
    centered_string = space * left_padding + return_string + space * right_padding
    
    # Return the specified string
    if return_string == a_string:
        return centered_string 
    elif return_string == b_string:
        return centered_string 
    else:
        raise ValueError("return_string must be either 'a_string' or 'b_string'")

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'finaltest'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\akim0\\Documents\\OpenBCI_GUI\\NeuroLingo\\PsychoPy_stuff\\Final Test\\finaltest_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp_9') is None:
        # initialise key_resp_9
        key_resp_9 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_9',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_24') is None:
        # initialise debugging_press_enter_to_skip_24
        debugging_press_enter_to_skip_24 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_24',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_4') is None:
        # initialise debugging_press_enter_to_skip_4
        debugging_press_enter_to_skip_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_4',
        )
    # create speaker 'maybe_a_beep'
    deviceManager.addDevice(
        deviceName='maybe_a_beep',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('debugging_press_enter_to_skip_5') is None:
        # initialise debugging_press_enter_to_skip_5
        debugging_press_enter_to_skip_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_5',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_8') is None:
        # initialise debugging_press_enter_to_skip_8
        debugging_press_enter_to_skip_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_8',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_25') is None:
        # initialise debugging_press_enter_to_skip_25
        debugging_press_enter_to_skip_25 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_25',
        )
    if deviceManager.getDevice('key_resp_10') is None:
        # initialise key_resp_10
        key_resp_10 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_10',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_23') is None:
        # initialise debugging_press_enter_to_skip_23
        debugging_press_enter_to_skip_23 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_23',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_7') is None:
        # initialise debugging_press_enter_to_skip_7
        debugging_press_enter_to_skip_7 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_7',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_26') is None:
        # initialise debugging_press_enter_to_skip_26
        debugging_press_enter_to_skip_26 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_26',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_15') is None:
        # initialise debugging_press_enter_to_skip_15
        debugging_press_enter_to_skip_15 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_15',
        )
    if deviceManager.getDevice('Press_Space_When_Ready') is None:
        # initialise Press_Space_When_Ready
        Press_Space_When_Ready = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Press_Space_When_Ready',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip') is None:
        # initialise debugging_press_enter_to_skip
        debugging_press_enter_to_skip = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_2') is None:
        # initialise debugging_press_enter_to_skip_2
        debugging_press_enter_to_skip_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_2',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_6') is None:
        # initialise debugging_press_enter_to_skip_6
        debugging_press_enter_to_skip_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_6',
        )
    if deviceManager.getDevice('key_resp_11') is None:
        # initialise key_resp_11
        key_resp_11 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_11',
        )
    if deviceManager.getDevice('key_resp_5') is None:
        # initialise key_resp_5
        key_resp_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_5',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_19') is None:
        # initialise debugging_press_enter_to_skip_19
        debugging_press_enter_to_skip_19 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_19',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_9') is None:
        # initialise debugging_press_enter_to_skip_9
        debugging_press_enter_to_skip_9 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_9',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_10') is None:
        # initialise debugging_press_enter_to_skip_10
        debugging_press_enter_to_skip_10 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_10',
        )
    if deviceManager.getDevice('key_resp_6') is None:
        # initialise key_resp_6
        key_resp_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_6',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_20') is None:
        # initialise debugging_press_enter_to_skip_20
        debugging_press_enter_to_skip_20 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_20',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_11') is None:
        # initialise debugging_press_enter_to_skip_11
        debugging_press_enter_to_skip_11 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_11',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_12') is None:
        # initialise debugging_press_enter_to_skip_12
        debugging_press_enter_to_skip_12 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_12',
        )
    if deviceManager.getDevice('key_resp_7') is None:
        # initialise key_resp_7
        key_resp_7 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_7',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_21') is None:
        # initialise debugging_press_enter_to_skip_21
        debugging_press_enter_to_skip_21 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_21',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_13') is None:
        # initialise debugging_press_enter_to_skip_13
        debugging_press_enter_to_skip_13 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_13',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_14') is None:
        # initialise debugging_press_enter_to_skip_14
        debugging_press_enter_to_skip_14 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_14',
        )
    if deviceManager.getDevice('key_resp_8') is None:
        # initialise key_resp_8
        key_resp_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_8',
        )
    if deviceManager.getDevice('debugging_press_enter_to_skip_22') is None:
        # initialise debugging_press_enter_to_skip_22
        debugging_press_enter_to_skip_22 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='debugging_press_enter_to_skip_22',
        )
    if deviceManager.getDevice('goNext') is None:
        # initialise goNext
        goNext = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='goNext',
        )
    if deviceManager.getDevice('goNext1') is None:
        # initialise goNext1
        goNext1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='goNext1',
        )
    if deviceManager.getDevice('enter') is None:
        # initialise enter
        enter = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='enter',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "COUNTERBALANCE_AND_NUMREPS" ---
    # Run 'Begin Experiment' code from Set_Counterbalance_Here_And_NumReps
    #counterbalance = True
    counterbalance = False
    
    
    # In the counterbalance order, we cancel the B trials
    if counterbalance == True:
        nreps_A = 0
        nreps_B = 1
    else:
        nreps_A = 1
        nreps_B = 0
    
    # --- Initialize components for Routine "LoadCharacters" ---
    # Run 'Begin Experiment' code from codeLoader
    #make empty lists
    #set 1
    word_list1 = []
    amharic_list1 = []
    
    #set 2
    word_list2 = []
    amharic_list2 = []
    
    #set 3
    word_list3 = []
    amharic_list3 = []
    
    #set 4
    word_list4 = []
    amharic_list4 = []
    
    #check and X
    markers = []
    
    #practice sets
    practice_amharic = []
    practice_words = []
    
    checkmark_reps = 0
    xmark_reps = 0
    
    # --- Initialize components for Routine "loadAndRemoveNone" ---
    
    # --- Initialize components for Routine "GenerateQuestions" ---
    
    # --- Initialize components for Routine "practice_welcome" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='Before moving onto the proper data collection section you will be shown a short version of what the real thing will look like to better prepare you.\n\nYou will be shown 12 total symbols to learn and given an accompanying test. The real thing will follow the same procedure but differ in scale. \n\nPress SPACE to move foward with the practice trials. ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_9 = keyboard.Keyboard(deviceName='key_resp_9')
    
    # --- Initialize components for Routine "randomize_set" ---
    
    # --- Initialize components for Routine "Increment" ---
    # Run 'Begin Experiment' code from increment_index
    learning_index = -1
    practice_index = -1
    
    # --- Initialize components for Routine "practice_wrdss" ---
    practice_amharicc = visual.TextStim(win=win, name='practice_amharicc',
        text='',
        font='Arial',
        pos=(-0.3, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    practice_wordssss = visual.TextStim(win=win, name='practice_wordssss',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.15, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    debugging_press_enter_to_skip_24 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_24')
    
    # --- Initialize components for Routine "plusBetween" ---
    plus = visual.TextStim(win=win, name='plus',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_4 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_4')
    
    # --- Initialize components for Routine "breakBetweenRepeats" ---
    five_seconds = visual.TextStim(win=win, name='five_seconds',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    maybe_a_beep = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker='maybe_a_beep',    name='maybe_a_beep'
    )
    maybe_a_beep.setVolume(1.0)
    debugging_press_enter_to_skip_5 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_5')
    
    # --- Initialize components for Routine "breakBetweenSets" ---
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_8 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_8')
    
    # --- Initialize components for Routine "randomize_set" ---
    
    # --- Initialize components for Routine "Increment" ---
    # Run 'Begin Experiment' code from increment_index
    learning_index = -1
    practice_index = -1
    
    # --- Initialize components for Routine "practice_images" ---
    amharic_practice2 = visual.TextStim(win=win, name='amharic_practice2',
        text='',
        font='Arial',
        pos=(-0.3, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    image_practice = visual.ImageStim(
        win=win,
        name='image_practice', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.3, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    debugging_press_enter_to_skip_25 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_25')
    
    # --- Initialize components for Routine "plusBetween" ---
    plus = visual.TextStim(win=win, name='plus',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_4 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_4')
    
    # --- Initialize components for Routine "breakBetweenRepeats" ---
    five_seconds = visual.TextStim(win=win, name='five_seconds',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    maybe_a_beep = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker='maybe_a_beep',    name='maybe_a_beep'
    )
    maybe_a_beep.setVolume(1.0)
    debugging_press_enter_to_skip_5 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_5')
    
    # --- Initialize components for Routine "practice_test" ---
    # Run 'Begin Experiment' code from codeSymbol_9
    #item counter
    curr_item = -1
    
    index_to_button = {
        1:'left',
        2:'right',
        0:'up',
        3:'down',
    }
    
    import random
    textAmharic_9 = visual.TextStim(win=win, name='textAmharic_9',
        text='',
        font='Arial',
        pos=(-.2, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    textOptionA_9 = visual.TextStim(win=win, name='textOptionA_9',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    textOptionB_9 = visual.TextStim(win=win, name='textOptionB_9',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    textOptionC_9 = visual.TextStim(win=win, name='textOptionC_9',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    textOptionD_9 = visual.TextStim(win=win, name='textOptionD_9',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    textDiamond_8 = visual.TextStim(win=win, name='textDiamond_8',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    key_resp_10 = keyboard.Keyboard(deviceName='key_resp_10')
    debugging_press_enter_to_skip_23 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_23')
    
    # --- Initialize components for Routine "checkForCorr_5" ---
    
    # --- Initialize components for Routine "checkmark" ---
    textCheck = visual.TextStim(win=win, name='textCheck',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_7 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_7')
    
    # --- Initialize components for Routine "xmark" ---
    textXmark = visual.TextStim(win=win, name='textXmark',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_26 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_26')
    
    # --- Initialize components for Routine "resetReps" ---
    # Run 'Begin Experiment' code from code_6
    checkmark_reps = 0
    xmark_reps = 0
    
    
    # --- Initialize components for Routine "blank500" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_15 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_15')
    
    # --- Initialize components for Routine "WelcomeScreen" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Welcome to our experiment\n\nPress SPACE when ready',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Press_Space_When_Ready = keyboard.Keyboard(deviceName='Press_Space_When_Ready')
    
    # --- Initialize components for Routine "randomize_set" ---
    
    # --- Initialize components for Routine "Increment" ---
    # Run 'Begin Experiment' code from increment_index
    learning_index = -1
    practice_index = -1
    
    # --- Initialize components for Routine "amharic1_A" ---
    amharics1 = visual.TextStim(win=win, name='amharics1',
        text='',
        font='Arial',
        pos=(-.3, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    words1 = visual.TextStim(win=win, name='words1',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.15, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    debugging_press_enter_to_skip = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip')
    
    # --- Initialize components for Routine "amharic1_B" ---
    amharics1_2 = visual.TextStim(win=win, name='amharics1_2',
        text='',
        font='Arial',
        pos=(-.3, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    words1_image_2 = visual.ImageStim(
        win=win,
        name='words1_image_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.3, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    debugging_press_enter_to_skip_2 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_2')
    
    # --- Initialize components for Routine "plusBetween" ---
    plus = visual.TextStim(win=win, name='plus',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_4 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_4')
    
    # --- Initialize components for Routine "breakBetweenRepeats" ---
    five_seconds = visual.TextStim(win=win, name='five_seconds',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    maybe_a_beep = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker='maybe_a_beep',    name='maybe_a_beep'
    )
    maybe_a_beep.setVolume(1.0)
    debugging_press_enter_to_skip_5 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_5')
    
    # --- Initialize components for Routine "routine_30Seconds" ---
    thirtySeconds = visual.TextStim(win=win, name='thirtySeconds',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from var_30_secs
    print("30 seconds")
    debugging_press_enter_to_skip_6 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_6')
    
    # --- Initialize components for Routine "start_test" ---
    textWelcome = visual.TextStim(win=win, name='textWelcome',
        text='The test phase will now begin.\n\nIf you do not know an answer do not press anything. Please avoid guessing. \n\nPress SPACE to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_11 = keyboard.Keyboard(deviceName='key_resp_11')
    
    # --- Initialize components for Routine "test1_NEW" ---
    # Run 'Begin Experiment' code from codeSymbol_5
    #item counter
    curr_item = -1
    
    index_to_button = {
        1:'left',
        2:'right',
        0:'up',
        3:'down',
    }
    
    import random
    textAmharic_5 = visual.TextStim(win=win, name='textAmharic_5',
        text='',
        font='Arial',
        pos=(-.2, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    textOptionA_5 = visual.TextStim(win=win, name='textOptionA_5',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    textOptionB_5 = visual.TextStim(win=win, name='textOptionB_5',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    textOptionC_5 = visual.TextStim(win=win, name='textOptionC_5',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    textOptionD_5 = visual.TextStim(win=win, name='textOptionD_5',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    textDiamond_3 = visual.TextStim(win=win, name='textDiamond_3',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    debugging_press_enter_to_skip_19 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_19')
    
    # --- Initialize components for Routine "checkForCorr" ---
    
    # --- Initialize components for Routine "checkmark" ---
    textCheck = visual.TextStim(win=win, name='textCheck',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_7 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_7')
    
    # --- Initialize components for Routine "xmark" ---
    textXmark = visual.TextStim(win=win, name='textXmark',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_26 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_26')
    
    # --- Initialize components for Routine "resetReps" ---
    # Run 'Begin Experiment' code from code_6
    checkmark_reps = 0
    xmark_reps = 0
    
    
    # --- Initialize components for Routine "blank500" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_15 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_15')
    
    # --- Initialize components for Routine "breakBetweenSets" ---
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_8 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_8')
    
    # --- Initialize components for Routine "randomize_set" ---
    
    # --- Initialize components for Routine "Increment" ---
    # Run 'Begin Experiment' code from increment_index
    learning_index = -1
    practice_index = -1
    
    # --- Initialize components for Routine "amharic2_A" ---
    amharics2 = visual.TextStim(win=win, name='amharics2',
        text='',
        font='Arial',
        pos=(-.3, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    words2 = visual.TextStim(win=win, name='words2',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.15, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    debugging_press_enter_to_skip_9 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_9')
    
    # --- Initialize components for Routine "amharic2_B" ---
    amharics2_2 = visual.TextStim(win=win, name='amharics2_2',
        text='',
        font='Arial',
        pos=(-.3, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    words2_image_2 = visual.ImageStim(
        win=win,
        name='words2_image_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.3, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    debugging_press_enter_to_skip_10 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_10')
    
    # --- Initialize components for Routine "plusBetween" ---
    plus = visual.TextStim(win=win, name='plus',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_4 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_4')
    
    # --- Initialize components for Routine "breakBetweenRepeats" ---
    five_seconds = visual.TextStim(win=win, name='five_seconds',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    maybe_a_beep = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker='maybe_a_beep',    name='maybe_a_beep'
    )
    maybe_a_beep.setVolume(1.0)
    debugging_press_enter_to_skip_5 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_5')
    
    # --- Initialize components for Routine "routine_30Seconds" ---
    thirtySeconds = visual.TextStim(win=win, name='thirtySeconds',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from var_30_secs
    print("30 seconds")
    debugging_press_enter_to_skip_6 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_6')
    
    # --- Initialize components for Routine "start_test" ---
    textWelcome = visual.TextStim(win=win, name='textWelcome',
        text='The test phase will now begin.\n\nIf you do not know an answer do not press anything. Please avoid guessing. \n\nPress SPACE to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_11 = keyboard.Keyboard(deviceName='key_resp_11')
    
    # --- Initialize components for Routine "test2_NEW" ---
    # Run 'Begin Experiment' code from codeSymbol_6
    #item counter
    curr_item2 = -1
    
    index_to_button = {
        1:'left',
        2:'right',
        0:'up',
        3:'down',
    }
    
    import random
    textAmharic_6 = visual.TextStim(win=win, name='textAmharic_6',
        text='',
        font='Arial',
        pos=(-.2, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    textOptionA_6 = visual.TextStim(win=win, name='textOptionA_6',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    textOptionB_6 = visual.TextStim(win=win, name='textOptionB_6',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    textOptionC_6 = visual.TextStim(win=win, name='textOptionC_6',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    textOptionD_6 = visual.TextStim(win=win, name='textOptionD_6',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    textDiamond_5 = visual.TextStim(win=win, name='textDiamond_5',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    debugging_press_enter_to_skip_20 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_20')
    
    # --- Initialize components for Routine "checkForCorr_2" ---
    
    # --- Initialize components for Routine "checkmark" ---
    textCheck = visual.TextStim(win=win, name='textCheck',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_7 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_7')
    
    # --- Initialize components for Routine "xmark" ---
    textXmark = visual.TextStim(win=win, name='textXmark',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_26 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_26')
    
    # --- Initialize components for Routine "resetReps" ---
    # Run 'Begin Experiment' code from code_6
    checkmark_reps = 0
    xmark_reps = 0
    
    
    # --- Initialize components for Routine "blank500" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_15 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_15')
    
    # --- Initialize components for Routine "breakBetweenSets" ---
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_8 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_8')
    
    # --- Initialize components for Routine "randomize_set" ---
    
    # --- Initialize components for Routine "Increment" ---
    # Run 'Begin Experiment' code from increment_index
    learning_index = -1
    practice_index = -1
    
    # --- Initialize components for Routine "amharic3_A" ---
    amharics3 = visual.TextStim(win=win, name='amharics3',
        text='',
        font='Arial',
        pos=(-.3, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    words3_image = visual.ImageStim(
        win=win,
        name='words3_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.3, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    debugging_press_enter_to_skip_11 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_11')
    
    # --- Initialize components for Routine "amharic3_B" ---
    amharics3_2 = visual.TextStim(win=win, name='amharics3_2',
        text='',
        font='Arial',
        pos=(-.3, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    words3_2 = visual.TextStim(win=win, name='words3_2',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.15, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    debugging_press_enter_to_skip_12 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_12')
    
    # --- Initialize components for Routine "plusBetween" ---
    plus = visual.TextStim(win=win, name='plus',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_4 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_4')
    
    # --- Initialize components for Routine "breakBetweenRepeats" ---
    five_seconds = visual.TextStim(win=win, name='five_seconds',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    maybe_a_beep = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker='maybe_a_beep',    name='maybe_a_beep'
    )
    maybe_a_beep.setVolume(1.0)
    debugging_press_enter_to_skip_5 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_5')
    
    # --- Initialize components for Routine "routine_30Seconds" ---
    thirtySeconds = visual.TextStim(win=win, name='thirtySeconds',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from var_30_secs
    print("30 seconds")
    debugging_press_enter_to_skip_6 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_6')
    
    # --- Initialize components for Routine "start_test" ---
    textWelcome = visual.TextStim(win=win, name='textWelcome',
        text='The test phase will now begin.\n\nIf you do not know an answer do not press anything. Please avoid guessing. \n\nPress SPACE to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_11 = keyboard.Keyboard(deviceName='key_resp_11')
    
    # --- Initialize components for Routine "test3_NEW" ---
    # Run 'Begin Experiment' code from codeSymbol_7
    #item counter
    curr_item3 = -1
    
    index_to_button = {
        1:'left',
        2:'right',
        0:'up',
        3:'down',
    }
    
    import random
    textAmharic_7 = visual.TextStim(win=win, name='textAmharic_7',
        text='',
        font='Arial',
        pos=(-.2, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    textOptionA_7 = visual.TextStim(win=win, name='textOptionA_7',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    textOptionB_7 = visual.TextStim(win=win, name='textOptionB_7',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    textOptionC_7 = visual.TextStim(win=win, name='textOptionC_7',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    textOptionD_7 = visual.TextStim(win=win, name='textOptionD_7',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    textDiamond_6 = visual.TextStim(win=win, name='textDiamond_6',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    key_resp_7 = keyboard.Keyboard(deviceName='key_resp_7')
    debugging_press_enter_to_skip_21 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_21')
    
    # --- Initialize components for Routine "checkForCorr_3" ---
    
    # --- Initialize components for Routine "checkmark" ---
    textCheck = visual.TextStim(win=win, name='textCheck',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_7 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_7')
    
    # --- Initialize components for Routine "xmark" ---
    textXmark = visual.TextStim(win=win, name='textXmark',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_26 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_26')
    
    # --- Initialize components for Routine "resetReps" ---
    # Run 'Begin Experiment' code from code_6
    checkmark_reps = 0
    xmark_reps = 0
    
    
    # --- Initialize components for Routine "blank500" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_15 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_15')
    
    # --- Initialize components for Routine "breakBetweenSets" ---
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_8 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_8')
    
    # --- Initialize components for Routine "randomize_set" ---
    
    # --- Initialize components for Routine "Increment" ---
    # Run 'Begin Experiment' code from increment_index
    learning_index = -1
    practice_index = -1
    
    # --- Initialize components for Routine "amharic4_A" ---
    amharics4 = visual.TextStim(win=win, name='amharics4',
        text='',
        font='Arial',
        pos=(-.3, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    words4_image = visual.ImageStim(
        win=win,
        name='words4_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.3, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    debugging_press_enter_to_skip_13 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_13')
    
    # --- Initialize components for Routine "amharic4_B" ---
    amharics4_2 = visual.TextStim(win=win, name='amharics4_2',
        text='',
        font='Arial',
        pos=(-.3, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    words4_2 = visual.TextStim(win=win, name='words4_2',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.15, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    debugging_press_enter_to_skip_14 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_14')
    
    # --- Initialize components for Routine "plusBetween" ---
    plus = visual.TextStim(win=win, name='plus',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_4 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_4')
    
    # --- Initialize components for Routine "breakBetweenRepeats" ---
    five_seconds = visual.TextStim(win=win, name='five_seconds',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    maybe_a_beep = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker='maybe_a_beep',    name='maybe_a_beep'
    )
    maybe_a_beep.setVolume(1.0)
    debugging_press_enter_to_skip_5 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_5')
    
    # --- Initialize components for Routine "routine_30Seconds" ---
    thirtySeconds = visual.TextStim(win=win, name='thirtySeconds',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from var_30_secs
    print("30 seconds")
    debugging_press_enter_to_skip_6 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_6')
    
    # --- Initialize components for Routine "start_test" ---
    textWelcome = visual.TextStim(win=win, name='textWelcome',
        text='The test phase will now begin.\n\nIf you do not know an answer do not press anything. Please avoid guessing. \n\nPress SPACE to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_11 = keyboard.Keyboard(deviceName='key_resp_11')
    
    # --- Initialize components for Routine "test4_NEW" ---
    # Run 'Begin Experiment' code from codeSymbol_8
    #item counter
    curr_item4 = -1
    
    index_to_button = {
        1:'left',
        2:'right',
        0:'up',
        3:'down',
    }
    
    import random
    textAmharic_8 = visual.TextStim(win=win, name='textAmharic_8',
        text='',
        font='Arial',
        pos=(-.2, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    textOptionA_8 = visual.TextStim(win=win, name='textOptionA_8',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    textOptionB_8 = visual.TextStim(win=win, name='textOptionB_8',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    textOptionC_8 = visual.TextStim(win=win, name='textOptionC_8',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    textOptionD_8 = visual.TextStim(win=win, name='textOptionD_8',
        text='',
        font='Arial',
        pos=(.3, 0.0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    textDiamond_7 = visual.TextStim(win=win, name='textDiamond_7',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    key_resp_8 = keyboard.Keyboard(deviceName='key_resp_8')
    debugging_press_enter_to_skip_22 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_22')
    
    # --- Initialize components for Routine "checkForCorr_4" ---
    
    # --- Initialize components for Routine "checkmark" ---
    textCheck = visual.TextStim(win=win, name='textCheck',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_7 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_7')
    
    # --- Initialize components for Routine "xmark" ---
    textXmark = visual.TextStim(win=win, name='textXmark',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_26 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_26')
    
    # --- Initialize components for Routine "resetReps" ---
    # Run 'Begin Experiment' code from code_6
    checkmark_reps = 0
    xmark_reps = 0
    
    
    # --- Initialize components for Routine "blank500" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_15 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_15')
    
    # --- Initialize components for Routine "breakBetweenSets" ---
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.3, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    debugging_press_enter_to_skip_8 = keyboard.Keyboard(deviceName='debugging_press_enter_to_skip_8')
    
    # --- Initialize components for Routine "WelcomeSlide" ---
    Welcome = visual.TextStim(win=win, name='Welcome',
        text='We will now begin the final part of the experiment.\n(Press ENTER to continue)',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    goNext = keyboard.Keyboard(deviceName='goNext')
    
    # --- Initialize components for Routine "Instructions" ---
    instructions_text = visual.TextStim(win=win, name='instructions_text',
        text='In the next slides, you will be prompted to give the translation of a given symbol. \n\nOnce you have typed the answer, press ENTER to continue. If you do not remember the symbol, you can simply press ENTER.\n\nYou have unlimited time to respond to each question. \n\nTo continue, press ENTER\n\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    goNext1 = keyboard.Keyboard(deviceName='goNext1')
    
    # --- Initialize components for Routine "TestQuestion" ---
    answer_box = visual.TextBox2(
         win, text=None, placeholder=None, font='Arial',
         ori=0.0, pos=(0, -0.35), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='answer_box',
         depth=0, autoLog=True,
    )
    enter = keyboard.Keyboard(deviceName='enter')
    symbol = visual.TextStim(win=win, name='symbol',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    # Run 'Begin Experiment' code from RandomQuestion
    # Set item counter to be zero
    curr_item = -1
    
    
    # --- Initialize components for Routine "Evaluate" ---
    # Run 'Begin Experiment' code from CorrectAnswers
    correct = 0
    message = "You got " + str(correct) + " out of 24 correct!"
    
    # --- Initialize components for Routine "ThankYou" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='THANK YOU FOR PARTICIPATING!!!!!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "COUNTERBALANCE_AND_NUMREPS" ---
    # create an object to store info about Routine COUNTERBALANCE_AND_NUMREPS
    COUNTERBALANCE_AND_NUMREPS = data.Routine(
        name='COUNTERBALANCE_AND_NUMREPS',
        components=[],
    )
    COUNTERBALANCE_AND_NUMREPS.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for COUNTERBALANCE_AND_NUMREPS
    COUNTERBALANCE_AND_NUMREPS.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    COUNTERBALANCE_AND_NUMREPS.tStart = globalClock.getTime(format='float')
    COUNTERBALANCE_AND_NUMREPS.status = STARTED
    thisExp.addData('COUNTERBALANCE_AND_NUMREPS.started', COUNTERBALANCE_AND_NUMREPS.tStart)
    COUNTERBALANCE_AND_NUMREPS.maxDuration = None
    # keep track of which components have finished
    COUNTERBALANCE_AND_NUMREPSComponents = COUNTERBALANCE_AND_NUMREPS.components
    for thisComponent in COUNTERBALANCE_AND_NUMREPS.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "COUNTERBALANCE_AND_NUMREPS" ---
    COUNTERBALANCE_AND_NUMREPS.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            COUNTERBALANCE_AND_NUMREPS.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in COUNTERBALANCE_AND_NUMREPS.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "COUNTERBALANCE_AND_NUMREPS" ---
    for thisComponent in COUNTERBALANCE_AND_NUMREPS.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for COUNTERBALANCE_AND_NUMREPS
    COUNTERBALANCE_AND_NUMREPS.tStop = globalClock.getTime(format='float')
    COUNTERBALANCE_AND_NUMREPS.tStopRefresh = tThisFlipGlobal
    thisExp.addData('COUNTERBALANCE_AND_NUMREPS.stopped', COUNTERBALANCE_AND_NUMREPS.tStop)
    thisExp.nextEntry()
    # the Routine "COUNTERBALANCE_AND_NUMREPS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    LoopParameters = data.TrialHandler2(
        name='LoopParameters',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('testSymbols2.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(LoopParameters)  # add the loop to the experiment
    thisLoopParameter = LoopParameters.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopParameter.rgb)
    if thisLoopParameter != None:
        for paramName in thisLoopParameter:
            globals()[paramName] = thisLoopParameter[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoopParameter in LoopParameters:
        currentLoop = LoopParameters
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoopParameter.rgb)
        if thisLoopParameter != None:
            for paramName in thisLoopParameter:
                globals()[paramName] = thisLoopParameter[paramName]
        
        # --- Prepare to start Routine "LoadCharacters" ---
        # create an object to store info about Routine LoadCharacters
        LoadCharacters = data.Routine(
            name='LoadCharacters',
            components=[],
        )
        LoadCharacters.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeLoader
        #save current word and color on each iteration of the loop
        # (for tests between learning sets)
        #set 1
        word_list1.append(words_set1)
        amharic_list1.append(amharic_set1)
        
        #set 2
        word_list2.append(words_set2)
        amharic_list2.append(amharic_set2)
        
        #set 3
        word_list3.append(words_set3)
        amharic_list3.append(amharic_set3)
        
        #set 4
        word_list4.append(words_set4)
        amharic_list4.append(amharic_set4)
        
        #symbols
        markers.append(symbols)
        
        #practices
        practice_amharic.append(amharic_practices)
        practice_words.append(words_practice)
        
        # Append it onto the dictionary (for final test)
        characters_words[amharic_set1] = words_set1
        characters_words[amharic_set2] = words_set2
        characters_words[amharic_set3] = words_set3
        characters_words[amharic_set4] = words_set4
        
        
        # store start times for LoadCharacters
        LoadCharacters.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        LoadCharacters.tStart = globalClock.getTime(format='float')
        LoadCharacters.status = STARTED
        thisExp.addData('LoadCharacters.started', LoadCharacters.tStart)
        LoadCharacters.maxDuration = None
        # keep track of which components have finished
        LoadCharactersComponents = LoadCharacters.components
        for thisComponent in LoadCharacters.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "LoadCharacters" ---
        # if trial has changed, end Routine now
        if isinstance(LoopParameters, data.TrialHandler2) and thisLoopParameter.thisN != LoopParameters.thisTrial.thisN:
            continueRoutine = False
        LoadCharacters.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                LoadCharacters.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LoadCharacters.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "LoadCharacters" ---
        for thisComponent in LoadCharacters.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for LoadCharacters
        LoadCharacters.tStop = globalClock.getTime(format='float')
        LoadCharacters.tStopRefresh = tThisFlipGlobal
        thisExp.addData('LoadCharacters.stopped', LoadCharacters.tStop)
        # Run 'End Routine' code from codeLoader
        # Our trial happens 12 times because
        # we have 12 columns in our sheets
        
        # Thus... the following code tabs occur
        
        # Before experiment: 1
        # Begin experiment: 1
        # Begin Routine: 12
        # Each frame: 12 * frames
        # End Routine: 12
        # End experiment: 1
        # the Routine "LoadCharacters" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'LoopParameters'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "loadAndRemoveNone" ---
    # create an object to store info about Routine loadAndRemoveNone
    loadAndRemoveNone = data.Routine(
        name='loadAndRemoveNone',
        components=[],
    )
    loadAndRemoveNone.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from loadWordsAndRemoveNone
    #getting rid of last none variable (for tests between sets)
    #set 1
    word_list1.remove(None)
    amharic_list1.remove(None)
    
    #set 2
    word_list2.remove(None)
    amharic_list2.remove(None)
    
    #set 3
    word_list3.remove(None)
    amharic_list3.remove(None)
    
    #set 4
    word_list4.remove(None)
    amharic_list4.remove(None)
    
    # Removes None from practice set
    practice_amharic.remove(None)
    practice_words.remove(None)
    
    # Removes None from characters_words (for final test)
    del characters_words[None]
    
    # We now have a dictionary 'characters_words' where the keys are 
    # Amharic characters, and the values are the meaning they correspond to.
    
    # store start times for loadAndRemoveNone
    loadAndRemoveNone.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    loadAndRemoveNone.tStart = globalClock.getTime(format='float')
    loadAndRemoveNone.status = STARTED
    thisExp.addData('loadAndRemoveNone.started', loadAndRemoveNone.tStart)
    loadAndRemoveNone.maxDuration = None
    # keep track of which components have finished
    loadAndRemoveNoneComponents = loadAndRemoveNone.components
    for thisComponent in loadAndRemoveNone.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "loadAndRemoveNone" ---
    loadAndRemoveNone.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            loadAndRemoveNone.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loadAndRemoveNone.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "loadAndRemoveNone" ---
    for thisComponent in loadAndRemoveNone.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for loadAndRemoveNone
    loadAndRemoveNone.tStop = globalClock.getTime(format='float')
    loadAndRemoveNone.tStopRefresh = tThisFlipGlobal
    thisExp.addData('loadAndRemoveNone.stopped', loadAndRemoveNone.tStop)
    # Run 'End Routine' code from loadWordsAndRemoveNone
    # Creates a dictionary for each word list
    
    amharic_word_list1 = {}
    amharic_word_list2 = {}
    amharic_word_list3 = {}
    amharic_word_list4 = {}
    practice_list = {}
    
    for i in range(12):
        amharic_word_list1[i] = (amharic_list1[i], word_list1[i], str(f"pictures/{word_list1[i]}.jpg"))
        amharic_word_list2[i] = (amharic_list2[i], word_list2[i], str(f"pictures/{word_list2[i]}.jpg"))
        amharic_word_list3[i] = (amharic_list3[i], word_list3[i], str(f"pictures/{word_list3[i]}.jpg"))
        amharic_word_list4[i] = (amharic_list4[i], word_list4[i], str(f"pictures/{word_list4[i]}.jpg"))
        practice_list[i] = (practice_amharic[i], practice_words[i], str(f"pictures/{practice_words[i]}.jpg"))
    
    practice_keys1 = list(range(12))[:6]
    practice_keys2 = list(range(12))[6:]
    
    practice_list1 = {key: practice_list[key] for key in practice_keys1}
    practice_list2 = {key: practice_list[key] for key in practice_keys2}
    
    for i in range(12):
        print(amharic_word_list1[i])
        print(amharic_word_list2[i])
        print(amharic_word_list3[i])
        print(amharic_word_list4[i])
        print(practice_list[i])
    thisExp.nextEntry()
    # the Routine "loadAndRemoveNone" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "GenerateQuestions" ---
    # create an object to store info about Routine GenerateQuestions
    GenerateQuestions = data.Routine(
        name='GenerateQuestions',
        components=[],
    )
    GenerateQuestions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from genQuestions
    # Generate the subset of the words that they will be tested on 
    select1 = random.sample(list(range(0,23)), 12)
    select2 = random.sample(list(range(24,48)), 12)
    selected_numbers = select1 + select2
    #selected_numbers = random.sample(list(range(48)), 24) # Just selects 24 randomly
    
    characters = list(characters_words.keys())
    test_questions = {}
    for index, number in zip(list(range(24)), selected_numbers):
        test_questions[index] = (characters[number], characters_words[characters[number]])
        
    # test_questions is a dictionary with an index (0-23) as a key and the value being an ordered pair (character, meaning)
    print("ANSWER KEY:")
    print(test_questions)
    # store start times for GenerateQuestions
    GenerateQuestions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    GenerateQuestions.tStart = globalClock.getTime(format='float')
    GenerateQuestions.status = STARTED
    thisExp.addData('GenerateQuestions.started', GenerateQuestions.tStart)
    GenerateQuestions.maxDuration = None
    # keep track of which components have finished
    GenerateQuestionsComponents = GenerateQuestions.components
    for thisComponent in GenerateQuestions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GenerateQuestions" ---
    GenerateQuestions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            GenerateQuestions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GenerateQuestions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GenerateQuestions" ---
    for thisComponent in GenerateQuestions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for GenerateQuestions
    GenerateQuestions.tStop = globalClock.getTime(format='float')
    GenerateQuestions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('GenerateQuestions.stopped', GenerateQuestions.tStop)
    thisExp.nextEntry()
    # the Routine "GenerateQuestions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_welcome" ---
    # create an object to store info about Routine practice_welcome
    practice_welcome = data.Routine(
        name='practice_welcome',
        components=[text_4, key_resp_9],
    )
    practice_welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_9
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # store start times for practice_welcome
    practice_welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practice_welcome.tStart = globalClock.getTime(format='float')
    practice_welcome.status = STARTED
    thisExp.addData('practice_welcome.started', practice_welcome.tStart)
    practice_welcome.maxDuration = None
    # keep track of which components have finished
    practice_welcomeComponents = practice_welcome.components
    for thisComponent in practice_welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practice_welcome" ---
    practice_welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # *key_resp_9* updates
        waitOnFlip = False
        
        # if key_resp_9 is starting this frame...
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_9.started')
            # update status
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                key_resp_9.duration = _key_resp_9_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practice_welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_welcome" ---
    for thisComponent in practice_welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practice_welcome
    practice_welcome.tStop = globalClock.getTime(format='float')
    practice_welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practice_welcome.stopped', practice_welcome.tStop)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    thisExp.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        thisExp.addData('key_resp_9.rt', key_resp_9.rt)
        thisExp.addData('key_resp_9.duration', key_resp_9.duration)
    thisExp.nextEntry()
    # the Routine "practice_welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    pracitce_wrds = data.TrialHandler2(
        name='pracitce_wrds',
        nReps=numReps, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(pracitce_wrds)  # add the loop to the experiment
    thisPracitce_wrd = pracitce_wrds.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracitce_wrd.rgb)
    if thisPracitce_wrd != None:
        for paramName in thisPracitce_wrd:
            globals()[paramName] = thisPracitce_wrd[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracitce_wrd in pracitce_wrds:
        currentLoop = pracitce_wrds
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracitce_wrd.rgb)
        if thisPracitce_wrd != None:
            for paramName in thisPracitce_wrd:
                globals()[paramName] = thisPracitce_wrd[paramName]
        
        # --- Prepare to start Routine "randomize_set" ---
        # create an object to store info about Routine randomize_set
        randomize_set = data.Routine(
            name='randomize_set',
            components=[],
        )
        randomize_set.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from randomize_learning_set
        keys = list(range(12))
        random.shuffle(keys)
        print("learning set order: " + str(keys))
        
        practice_keys = list(range(6))
        random.shuffle(practice_keys)
        print("learning set order: " + str(keys))
        
        practice_keys2 = list(range(6,12))
        random.shuffle(practice_keys2)
        print("learning set order: " + str(keys))
        # store start times for randomize_set
        randomize_set.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        randomize_set.tStart = globalClock.getTime(format='float')
        randomize_set.status = STARTED
        thisExp.addData('randomize_set.started', randomize_set.tStart)
        randomize_set.maxDuration = None
        # keep track of which components have finished
        randomize_setComponents = randomize_set.components
        for thisComponent in randomize_set.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "randomize_set" ---
        # if trial has changed, end Routine now
        if isinstance(pracitce_wrds, data.TrialHandler2) and thisPracitce_wrd.thisN != pracitce_wrds.thisTrial.thisN:
            continueRoutine = False
        randomize_set.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                randomize_set.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in randomize_set.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "randomize_set" ---
        for thisComponent in randomize_set.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for randomize_set
        randomize_set.tStop = globalClock.getTime(format='float')
        randomize_set.tStopRefresh = tThisFlipGlobal
        thisExp.addData('randomize_set.stopped', randomize_set.tStop)
        # the Routine "randomize_set" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        practice_sets1 = data.TrialHandler2(
            name='practice_sets1',
            nReps=6.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(practice_sets1)  # add the loop to the experiment
        thisPractice_sets1 = practice_sets1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_sets1.rgb)
        if thisPractice_sets1 != None:
            for paramName in thisPractice_sets1:
                globals()[paramName] = thisPractice_sets1[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisPractice_sets1 in practice_sets1:
            currentLoop = practice_sets1
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_sets1.rgb)
            if thisPractice_sets1 != None:
                for paramName in thisPractice_sets1:
                    globals()[paramName] = thisPractice_sets1[paramName]
            
            # --- Prepare to start Routine "Increment" ---
            # create an object to store info about Routine Increment
            Increment = data.Routine(
                name='Increment',
                components=[],
            )
            Increment.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from increment_index
            learning_index += 1
            learning_index %= len(keys)
            
            practice_index += 1
            practice_index %= len(practice_keys)
            # store start times for Increment
            Increment.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Increment.tStart = globalClock.getTime(format='float')
            Increment.status = STARTED
            thisExp.addData('Increment.started', Increment.tStart)
            Increment.maxDuration = None
            # keep track of which components have finished
            IncrementComponents = Increment.components
            for thisComponent in Increment.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Increment" ---
            # if trial has changed, end Routine now
            if isinstance(practice_sets1, data.TrialHandler2) and thisPractice_sets1.thisN != practice_sets1.thisTrial.thisN:
                continueRoutine = False
            Increment.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Increment.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Increment.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Increment" ---
            for thisComponent in Increment.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Increment
            Increment.tStop = globalClock.getTime(format='float')
            Increment.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Increment.stopped', Increment.tStop)
            # the Routine "Increment" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "practice_wrdss" ---
            # create an object to store info about Routine practice_wrdss
            practice_wrdss = data.Routine(
                name='practice_wrdss',
                components=[practice_amharicc, practice_wordssss, debugging_press_enter_to_skip_24],
            )
            practice_wrdss.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            practice_amharicc.setText(practice_list1[practice_keys[practice_index]][0])
            practice_wordssss.setText(practice_list1[practice_keys[practice_index]][1])
            # create starting attributes for debugging_press_enter_to_skip_24
            debugging_press_enter_to_skip_24.keys = []
            debugging_press_enter_to_skip_24.rt = []
            _debugging_press_enter_to_skip_24_allKeys = []
            # store start times for practice_wrdss
            practice_wrdss.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            practice_wrdss.tStart = globalClock.getTime(format='float')
            practice_wrdss.status = STARTED
            thisExp.addData('practice_wrdss.started', practice_wrdss.tStart)
            practice_wrdss.maxDuration = None
            # keep track of which components have finished
            practice_wrdssComponents = practice_wrdss.components
            for thisComponent in practice_wrdss.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "practice_wrdss" ---
            # if trial has changed, end Routine now
            if isinstance(practice_sets1, data.TrialHandler2) and thisPractice_sets1.thisN != practice_sets1.thisTrial.thisN:
                continueRoutine = False
            practice_wrdss.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *practice_amharicc* updates
                
                # if practice_amharicc is starting this frame...
                if practice_amharicc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    practice_amharicc.frameNStart = frameN  # exact frame index
                    practice_amharicc.tStart = t  # local t and not account for scr refresh
                    practice_amharicc.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(practice_amharicc, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_amharicc.started')
                    # update status
                    practice_amharicc.status = STARTED
                    practice_amharicc.setAutoDraw(True)
                
                # if practice_amharicc is active this frame...
                if practice_amharicc.status == STARTED:
                    # update params
                    pass
                
                # if practice_amharicc is stopping this frame...
                if practice_amharicc.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > practice_amharicc.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        practice_amharicc.tStop = t  # not accounting for scr refresh
                        practice_amharicc.tStopRefresh = tThisFlipGlobal  # on global time
                        practice_amharicc.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'practice_amharicc.stopped')
                        # update status
                        practice_amharicc.status = FINISHED
                        practice_amharicc.setAutoDraw(False)
                
                # *practice_wordssss* updates
                
                # if practice_wordssss is starting this frame...
                if practice_wordssss.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    practice_wordssss.frameNStart = frameN  # exact frame index
                    practice_wordssss.tStart = t  # local t and not account for scr refresh
                    practice_wordssss.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(practice_wordssss, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_wordssss.started')
                    # update status
                    practice_wordssss.status = STARTED
                    practice_wordssss.setAutoDraw(True)
                
                # if practice_wordssss is active this frame...
                if practice_wordssss.status == STARTED:
                    # update params
                    pass
                
                # if practice_wordssss is stopping this frame...
                if practice_wordssss.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > practice_wordssss.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        practice_wordssss.tStop = t  # not accounting for scr refresh
                        practice_wordssss.tStopRefresh = tThisFlipGlobal  # on global time
                        practice_wordssss.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'practice_wordssss.stopped')
                        # update status
                        practice_wordssss.status = FINISHED
                        practice_wordssss.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_24* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_24 is starting this frame...
                if debugging_press_enter_to_skip_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_24.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_24.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_24.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_24, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_24.started')
                    # update status
                    debugging_press_enter_to_skip_24.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_24.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_24 is stopping this frame...
                if debugging_press_enter_to_skip_24.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_24.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_24.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_24.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_24.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_24.stopped')
                        # update status
                        debugging_press_enter_to_skip_24.status = FINISHED
                        debugging_press_enter_to_skip_24.status = FINISHED
                if debugging_press_enter_to_skip_24.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_24.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_24_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_24_allKeys):
                        debugging_press_enter_to_skip_24.keys = _debugging_press_enter_to_skip_24_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_24.rt = _debugging_press_enter_to_skip_24_allKeys[-1].rt
                        debugging_press_enter_to_skip_24.duration = _debugging_press_enter_to_skip_24_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    practice_wrdss.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practice_wrdss.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "practice_wrdss" ---
            for thisComponent in practice_wrdss.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for practice_wrdss
            practice_wrdss.tStop = globalClock.getTime(format='float')
            practice_wrdss.tStopRefresh = tThisFlipGlobal
            thisExp.addData('practice_wrdss.stopped', practice_wrdss.tStop)
            # check responses
            if debugging_press_enter_to_skip_24.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_24.keys = None
            practice_sets1.addData('debugging_press_enter_to_skip_24.keys',debugging_press_enter_to_skip_24.keys)
            if debugging_press_enter_to_skip_24.keys != None:  # we had a response
                practice_sets1.addData('debugging_press_enter_to_skip_24.rt', debugging_press_enter_to_skip_24.rt)
                practice_sets1.addData('debugging_press_enter_to_skip_24.duration', debugging_press_enter_to_skip_24.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if practice_wrdss.maxDurationReached:
                routineTimer.addTime(-practice_wrdss.maxDuration)
            elif practice_wrdss.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "plusBetween" ---
            # create an object to store info about Routine plusBetween
            plusBetween = data.Routine(
                name='plusBetween',
                components=[plus, debugging_press_enter_to_skip_4],
            )
            plusBetween.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            plus.setText('+')
            # create starting attributes for debugging_press_enter_to_skip_4
            debugging_press_enter_to_skip_4.keys = []
            debugging_press_enter_to_skip_4.rt = []
            _debugging_press_enter_to_skip_4_allKeys = []
            # store start times for plusBetween
            plusBetween.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            plusBetween.tStart = globalClock.getTime(format='float')
            plusBetween.status = STARTED
            thisExp.addData('plusBetween.started', plusBetween.tStart)
            plusBetween.maxDuration = None
            # keep track of which components have finished
            plusBetweenComponents = plusBetween.components
            for thisComponent in plusBetween.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "plusBetween" ---
            # if trial has changed, end Routine now
            if isinstance(practice_sets1, data.TrialHandler2) and thisPractice_sets1.thisN != practice_sets1.thisTrial.thisN:
                continueRoutine = False
            plusBetween.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *plus* updates
                
                # if plus is starting this frame...
                if plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    plus.frameNStart = frameN  # exact frame index
                    plus.tStart = t  # local t and not account for scr refresh
                    plus.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(plus, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'plus.started')
                    # update status
                    plus.status = STARTED
                    plus.setAutoDraw(True)
                
                # if plus is active this frame...
                if plus.status == STARTED:
                    # update params
                    pass
                
                # if plus is stopping this frame...
                if plus.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > plus.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        plus.tStop = t  # not accounting for scr refresh
                        plus.tStopRefresh = tThisFlipGlobal  # on global time
                        plus.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'plus.stopped')
                        # update status
                        plus.status = FINISHED
                        plus.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_4* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_4 is starting this frame...
                if debugging_press_enter_to_skip_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_4.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_4.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.started')
                    # update status
                    debugging_press_enter_to_skip_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_4 is stopping this frame...
                if debugging_press_enter_to_skip_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_4.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_4.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_4.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.stopped')
                        # update status
                        debugging_press_enter_to_skip_4.status = FINISHED
                        debugging_press_enter_to_skip_4.status = FINISHED
                if debugging_press_enter_to_skip_4.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_4.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_4_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_4_allKeys):
                        debugging_press_enter_to_skip_4.keys = _debugging_press_enter_to_skip_4_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_4.rt = _debugging_press_enter_to_skip_4_allKeys[-1].rt
                        debugging_press_enter_to_skip_4.duration = _debugging_press_enter_to_skip_4_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    plusBetween.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in plusBetween.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "plusBetween" ---
            for thisComponent in plusBetween.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for plusBetween
            plusBetween.tStop = globalClock.getTime(format='float')
            plusBetween.tStopRefresh = tThisFlipGlobal
            thisExp.addData('plusBetween.stopped', plusBetween.tStop)
            # check responses
            if debugging_press_enter_to_skip_4.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_4.keys = None
            practice_sets1.addData('debugging_press_enter_to_skip_4.keys',debugging_press_enter_to_skip_4.keys)
            if debugging_press_enter_to_skip_4.keys != None:  # we had a response
                practice_sets1.addData('debugging_press_enter_to_skip_4.rt', debugging_press_enter_to_skip_4.rt)
                practice_sets1.addData('debugging_press_enter_to_skip_4.duration', debugging_press_enter_to_skip_4.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if plusBetween.maxDurationReached:
                routineTimer.addTime(-plusBetween.maxDuration)
            elif plusBetween.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 6.0 repeats of 'practice_sets1'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "breakBetweenRepeats" ---
        # create an object to store info about Routine breakBetweenRepeats
        breakBetweenRepeats = data.Routine(
            name='breakBetweenRepeats',
            components=[five_seconds, maybe_a_beep, debugging_press_enter_to_skip_5],
        )
        breakBetweenRepeats.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        maybe_a_beep.setSound('A', secs=1.0, hamming=True)
        maybe_a_beep.setVolume(1.0, log=False)
        maybe_a_beep.seek(0)
        # create starting attributes for debugging_press_enter_to_skip_5
        debugging_press_enter_to_skip_5.keys = []
        debugging_press_enter_to_skip_5.rt = []
        _debugging_press_enter_to_skip_5_allKeys = []
        # store start times for breakBetweenRepeats
        breakBetweenRepeats.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        breakBetweenRepeats.tStart = globalClock.getTime(format='float')
        breakBetweenRepeats.status = STARTED
        thisExp.addData('breakBetweenRepeats.started', breakBetweenRepeats.tStart)
        breakBetweenRepeats.maxDuration = None
        # keep track of which components have finished
        breakBetweenRepeatsComponents = breakBetweenRepeats.components
        for thisComponent in breakBetweenRepeats.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "breakBetweenRepeats" ---
        # if trial has changed, end Routine now
        if isinstance(pracitce_wrds, data.TrialHandler2) and thisPracitce_wrd.thisN != pracitce_wrds.thisTrial.thisN:
            continueRoutine = False
        breakBetweenRepeats.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *five_seconds* updates
            
            # if five_seconds is starting this frame...
            if five_seconds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                five_seconds.frameNStart = frameN  # exact frame index
                five_seconds.tStart = t  # local t and not account for scr refresh
                five_seconds.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(five_seconds, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'five_seconds.started')
                # update status
                five_seconds.status = STARTED
                five_seconds.setAutoDraw(True)
            
            # if five_seconds is active this frame...
            if five_seconds.status == STARTED:
                # update params
                pass
            
            # if five_seconds is stopping this frame...
            if five_seconds.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > five_seconds.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    five_seconds.tStop = t  # not accounting for scr refresh
                    five_seconds.tStopRefresh = tThisFlipGlobal  # on global time
                    five_seconds.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'five_seconds.stopped')
                    # update status
                    five_seconds.status = FINISHED
                    five_seconds.setAutoDraw(False)
            
            # *maybe_a_beep* updates
            
            # if maybe_a_beep is starting this frame...
            if maybe_a_beep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                maybe_a_beep.frameNStart = frameN  # exact frame index
                maybe_a_beep.tStart = t  # local t and not account for scr refresh
                maybe_a_beep.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('maybe_a_beep.started', tThisFlipGlobal)
                # update status
                maybe_a_beep.status = STARTED
                maybe_a_beep.play(when=win)  # sync with win flip
            
            # if maybe_a_beep is stopping this frame...
            if maybe_a_beep.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > maybe_a_beep.tStartRefresh + 1.0-frameTolerance or maybe_a_beep.isFinished:
                    # keep track of stop time/frame for later
                    maybe_a_beep.tStop = t  # not accounting for scr refresh
                    maybe_a_beep.tStopRefresh = tThisFlipGlobal  # on global time
                    maybe_a_beep.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'maybe_a_beep.stopped')
                    # update status
                    maybe_a_beep.status = FINISHED
                    maybe_a_beep.stop()
            
            # *debugging_press_enter_to_skip_5* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_5 is starting this frame...
            if debugging_press_enter_to_skip_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_5.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_5.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.started')
                # update status
                debugging_press_enter_to_skip_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if debugging_press_enter_to_skip_5 is stopping this frame...
            if debugging_press_enter_to_skip_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > debugging_press_enter_to_skip_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    debugging_press_enter_to_skip_5.tStop = t  # not accounting for scr refresh
                    debugging_press_enter_to_skip_5.tStopRefresh = tThisFlipGlobal  # on global time
                    debugging_press_enter_to_skip_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.stopped')
                    # update status
                    debugging_press_enter_to_skip_5.status = FINISHED
                    debugging_press_enter_to_skip_5.status = FINISHED
            if debugging_press_enter_to_skip_5.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_5.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_5_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_5_allKeys):
                    debugging_press_enter_to_skip_5.keys = _debugging_press_enter_to_skip_5_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_5.rt = _debugging_press_enter_to_skip_5_allKeys[-1].rt
                    debugging_press_enter_to_skip_5.duration = _debugging_press_enter_to_skip_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[maybe_a_beep]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                breakBetweenRepeats.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in breakBetweenRepeats.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "breakBetweenRepeats" ---
        for thisComponent in breakBetweenRepeats.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for breakBetweenRepeats
        breakBetweenRepeats.tStop = globalClock.getTime(format='float')
        breakBetweenRepeats.tStopRefresh = tThisFlipGlobal
        thisExp.addData('breakBetweenRepeats.stopped', breakBetweenRepeats.tStop)
        maybe_a_beep.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if debugging_press_enter_to_skip_5.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_5.keys = None
        pracitce_wrds.addData('debugging_press_enter_to_skip_5.keys',debugging_press_enter_to_skip_5.keys)
        if debugging_press_enter_to_skip_5.keys != None:  # we had a response
            pracitce_wrds.addData('debugging_press_enter_to_skip_5.rt', debugging_press_enter_to_skip_5.rt)
            pracitce_wrds.addData('debugging_press_enter_to_skip_5.duration', debugging_press_enter_to_skip_5.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if breakBetweenRepeats.maxDurationReached:
            routineTimer.addTime(-breakBetweenRepeats.maxDuration)
        elif breakBetweenRepeats.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed numReps repeats of 'pracitce_wrds'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "breakBetweenSets" ---
    # create an object to store info about Routine breakBetweenSets
    breakBetweenSets = data.Routine(
        name='breakBetweenSets',
        components=[cross, debugging_press_enter_to_skip_8],
    )
    breakBetweenSets.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for debugging_press_enter_to_skip_8
    debugging_press_enter_to_skip_8.keys = []
    debugging_press_enter_to_skip_8.rt = []
    _debugging_press_enter_to_skip_8_allKeys = []
    # store start times for breakBetweenSets
    breakBetweenSets.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    breakBetweenSets.tStart = globalClock.getTime(format='float')
    breakBetweenSets.status = STARTED
    thisExp.addData('breakBetweenSets.started', breakBetweenSets.tStart)
    breakBetweenSets.maxDuration = None
    # keep track of which components have finished
    breakBetweenSetsComponents = breakBetweenSets.components
    for thisComponent in breakBetweenSets.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "breakBetweenSets" ---
    breakBetweenSets.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.tStopRefresh = tThisFlipGlobal  # on global time
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # *debugging_press_enter_to_skip_8* updates
        waitOnFlip = False
        
        # if debugging_press_enter_to_skip_8 is starting this frame...
        if debugging_press_enter_to_skip_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debugging_press_enter_to_skip_8.frameNStart = frameN  # exact frame index
            debugging_press_enter_to_skip_8.tStart = t  # local t and not account for scr refresh
            debugging_press_enter_to_skip_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debugging_press_enter_to_skip_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_8.started')
            # update status
            debugging_press_enter_to_skip_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(debugging_press_enter_to_skip_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(debugging_press_enter_to_skip_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if debugging_press_enter_to_skip_8 is stopping this frame...
        if debugging_press_enter_to_skip_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > debugging_press_enter_to_skip_8.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                debugging_press_enter_to_skip_8.tStop = t  # not accounting for scr refresh
                debugging_press_enter_to_skip_8.tStopRefresh = tThisFlipGlobal  # on global time
                debugging_press_enter_to_skip_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_8.stopped')
                # update status
                debugging_press_enter_to_skip_8.status = FINISHED
                debugging_press_enter_to_skip_8.status = FINISHED
        if debugging_press_enter_to_skip_8.status == STARTED and not waitOnFlip:
            theseKeys = debugging_press_enter_to_skip_8.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _debugging_press_enter_to_skip_8_allKeys.extend(theseKeys)
            if len(_debugging_press_enter_to_skip_8_allKeys):
                debugging_press_enter_to_skip_8.keys = _debugging_press_enter_to_skip_8_allKeys[-1].name  # just the last key pressed
                debugging_press_enter_to_skip_8.rt = _debugging_press_enter_to_skip_8_allKeys[-1].rt
                debugging_press_enter_to_skip_8.duration = _debugging_press_enter_to_skip_8_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            breakBetweenSets.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breakBetweenSets.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "breakBetweenSets" ---
    for thisComponent in breakBetweenSets.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for breakBetweenSets
    breakBetweenSets.tStop = globalClock.getTime(format='float')
    breakBetweenSets.tStopRefresh = tThisFlipGlobal
    thisExp.addData('breakBetweenSets.stopped', breakBetweenSets.tStop)
    # check responses
    if debugging_press_enter_to_skip_8.keys in ['', [], None]:  # No response was made
        debugging_press_enter_to_skip_8.keys = None
    thisExp.addData('debugging_press_enter_to_skip_8.keys',debugging_press_enter_to_skip_8.keys)
    if debugging_press_enter_to_skip_8.keys != None:  # we had a response
        thisExp.addData('debugging_press_enter_to_skip_8.rt', debugging_press_enter_to_skip_8.rt)
        thisExp.addData('debugging_press_enter_to_skip_8.duration', debugging_press_enter_to_skip_8.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if breakBetweenSets.maxDurationReached:
        routineTimer.addTime(-breakBetweenSets.maxDuration)
    elif breakBetweenSets.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    practice_imagess = data.TrialHandler2(
        name='practice_imagess',
        nReps=numReps, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(practice_imagess)  # add the loop to the experiment
    thisPractice_images = practice_imagess.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_images.rgb)
    if thisPractice_images != None:
        for paramName in thisPractice_images:
            globals()[paramName] = thisPractice_images[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractice_images in practice_imagess:
        currentLoop = practice_imagess
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_images.rgb)
        if thisPractice_images != None:
            for paramName in thisPractice_images:
                globals()[paramName] = thisPractice_images[paramName]
        
        # --- Prepare to start Routine "randomize_set" ---
        # create an object to store info about Routine randomize_set
        randomize_set = data.Routine(
            name='randomize_set',
            components=[],
        )
        randomize_set.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from randomize_learning_set
        keys = list(range(12))
        random.shuffle(keys)
        print("learning set order: " + str(keys))
        
        practice_keys = list(range(6))
        random.shuffle(practice_keys)
        print("learning set order: " + str(keys))
        
        practice_keys2 = list(range(6,12))
        random.shuffle(practice_keys2)
        print("learning set order: " + str(keys))
        # store start times for randomize_set
        randomize_set.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        randomize_set.tStart = globalClock.getTime(format='float')
        randomize_set.status = STARTED
        thisExp.addData('randomize_set.started', randomize_set.tStart)
        randomize_set.maxDuration = None
        # keep track of which components have finished
        randomize_setComponents = randomize_set.components
        for thisComponent in randomize_set.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "randomize_set" ---
        # if trial has changed, end Routine now
        if isinstance(practice_imagess, data.TrialHandler2) and thisPractice_images.thisN != practice_imagess.thisTrial.thisN:
            continueRoutine = False
        randomize_set.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                randomize_set.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in randomize_set.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "randomize_set" ---
        for thisComponent in randomize_set.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for randomize_set
        randomize_set.tStop = globalClock.getTime(format='float')
        randomize_set.tStopRefresh = tThisFlipGlobal
        thisExp.addData('randomize_set.stopped', randomize_set.tStop)
        # the Routine "randomize_set" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        practice_sets2 = data.TrialHandler2(
            name='practice_sets2',
            nReps=6.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(practice_sets2)  # add the loop to the experiment
        thisPractice_sets2 = practice_sets2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_sets2.rgb)
        if thisPractice_sets2 != None:
            for paramName in thisPractice_sets2:
                globals()[paramName] = thisPractice_sets2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisPractice_sets2 in practice_sets2:
            currentLoop = practice_sets2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisPractice_sets2.rgb)
            if thisPractice_sets2 != None:
                for paramName in thisPractice_sets2:
                    globals()[paramName] = thisPractice_sets2[paramName]
            
            # --- Prepare to start Routine "Increment" ---
            # create an object to store info about Routine Increment
            Increment = data.Routine(
                name='Increment',
                components=[],
            )
            Increment.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from increment_index
            learning_index += 1
            learning_index %= len(keys)
            
            practice_index += 1
            practice_index %= len(practice_keys)
            # store start times for Increment
            Increment.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Increment.tStart = globalClock.getTime(format='float')
            Increment.status = STARTED
            thisExp.addData('Increment.started', Increment.tStart)
            Increment.maxDuration = None
            # keep track of which components have finished
            IncrementComponents = Increment.components
            for thisComponent in Increment.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Increment" ---
            # if trial has changed, end Routine now
            if isinstance(practice_sets2, data.TrialHandler2) and thisPractice_sets2.thisN != practice_sets2.thisTrial.thisN:
                continueRoutine = False
            Increment.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Increment.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Increment.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Increment" ---
            for thisComponent in Increment.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Increment
            Increment.tStop = globalClock.getTime(format='float')
            Increment.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Increment.stopped', Increment.tStop)
            # the Routine "Increment" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "practice_images" ---
            # create an object to store info about Routine practice_images
            practice_images = data.Routine(
                name='practice_images',
                components=[amharic_practice2, image_practice, debugging_press_enter_to_skip_25],
            )
            practice_images.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            amharic_practice2.setText(practice_list2[practice_keys2[practice_index]][0])
            image_practice.setImage(practice_list2[practice_keys2[practice_index]][2])
            # create starting attributes for debugging_press_enter_to_skip_25
            debugging_press_enter_to_skip_25.keys = []
            debugging_press_enter_to_skip_25.rt = []
            _debugging_press_enter_to_skip_25_allKeys = []
            # store start times for practice_images
            practice_images.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            practice_images.tStart = globalClock.getTime(format='float')
            practice_images.status = STARTED
            thisExp.addData('practice_images.started', practice_images.tStart)
            practice_images.maxDuration = None
            # keep track of which components have finished
            practice_imagesComponents = practice_images.components
            for thisComponent in practice_images.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "practice_images" ---
            # if trial has changed, end Routine now
            if isinstance(practice_sets2, data.TrialHandler2) and thisPractice_sets2.thisN != practice_sets2.thisTrial.thisN:
                continueRoutine = False
            practice_images.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *amharic_practice2* updates
                
                # if amharic_practice2 is starting this frame...
                if amharic_practice2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    amharic_practice2.frameNStart = frameN  # exact frame index
                    amharic_practice2.tStart = t  # local t and not account for scr refresh
                    amharic_practice2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(amharic_practice2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'amharic_practice2.started')
                    # update status
                    amharic_practice2.status = STARTED
                    amharic_practice2.setAutoDraw(True)
                
                # if amharic_practice2 is active this frame...
                if amharic_practice2.status == STARTED:
                    # update params
                    pass
                
                # if amharic_practice2 is stopping this frame...
                if amharic_practice2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > amharic_practice2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        amharic_practice2.tStop = t  # not accounting for scr refresh
                        amharic_practice2.tStopRefresh = tThisFlipGlobal  # on global time
                        amharic_practice2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'amharic_practice2.stopped')
                        # update status
                        amharic_practice2.status = FINISHED
                        amharic_practice2.setAutoDraw(False)
                
                # *image_practice* updates
                
                # if image_practice is starting this frame...
                if image_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_practice.frameNStart = frameN  # exact frame index
                    image_practice.tStart = t  # local t and not account for scr refresh
                    image_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_practice.started')
                    # update status
                    image_practice.status = STARTED
                    image_practice.setAutoDraw(True)
                
                # if image_practice is active this frame...
                if image_practice.status == STARTED:
                    # update params
                    pass
                
                # if image_practice is stopping this frame...
                if image_practice.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_practice.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        image_practice.tStop = t  # not accounting for scr refresh
                        image_practice.tStopRefresh = tThisFlipGlobal  # on global time
                        image_practice.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_practice.stopped')
                        # update status
                        image_practice.status = FINISHED
                        image_practice.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_25* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_25 is starting this frame...
                if debugging_press_enter_to_skip_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_25.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_25.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_25.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_25, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_25.started')
                    # update status
                    debugging_press_enter_to_skip_25.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_25.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_25 is stopping this frame...
                if debugging_press_enter_to_skip_25.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_25.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_25.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_25.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_25.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_25.stopped')
                        # update status
                        debugging_press_enter_to_skip_25.status = FINISHED
                        debugging_press_enter_to_skip_25.status = FINISHED
                if debugging_press_enter_to_skip_25.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_25.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_25_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_25_allKeys):
                        debugging_press_enter_to_skip_25.keys = _debugging_press_enter_to_skip_25_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_25.rt = _debugging_press_enter_to_skip_25_allKeys[-1].rt
                        debugging_press_enter_to_skip_25.duration = _debugging_press_enter_to_skip_25_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    practice_images.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practice_images.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "practice_images" ---
            for thisComponent in practice_images.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for practice_images
            practice_images.tStop = globalClock.getTime(format='float')
            practice_images.tStopRefresh = tThisFlipGlobal
            thisExp.addData('practice_images.stopped', practice_images.tStop)
            # check responses
            if debugging_press_enter_to_skip_25.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_25.keys = None
            practice_sets2.addData('debugging_press_enter_to_skip_25.keys',debugging_press_enter_to_skip_25.keys)
            if debugging_press_enter_to_skip_25.keys != None:  # we had a response
                practice_sets2.addData('debugging_press_enter_to_skip_25.rt', debugging_press_enter_to_skip_25.rt)
                practice_sets2.addData('debugging_press_enter_to_skip_25.duration', debugging_press_enter_to_skip_25.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if practice_images.maxDurationReached:
                routineTimer.addTime(-practice_images.maxDuration)
            elif practice_images.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "plusBetween" ---
            # create an object to store info about Routine plusBetween
            plusBetween = data.Routine(
                name='plusBetween',
                components=[plus, debugging_press_enter_to_skip_4],
            )
            plusBetween.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            plus.setText('+')
            # create starting attributes for debugging_press_enter_to_skip_4
            debugging_press_enter_to_skip_4.keys = []
            debugging_press_enter_to_skip_4.rt = []
            _debugging_press_enter_to_skip_4_allKeys = []
            # store start times for plusBetween
            plusBetween.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            plusBetween.tStart = globalClock.getTime(format='float')
            plusBetween.status = STARTED
            thisExp.addData('plusBetween.started', plusBetween.tStart)
            plusBetween.maxDuration = None
            # keep track of which components have finished
            plusBetweenComponents = plusBetween.components
            for thisComponent in plusBetween.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "plusBetween" ---
            # if trial has changed, end Routine now
            if isinstance(practice_sets2, data.TrialHandler2) and thisPractice_sets2.thisN != practice_sets2.thisTrial.thisN:
                continueRoutine = False
            plusBetween.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *plus* updates
                
                # if plus is starting this frame...
                if plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    plus.frameNStart = frameN  # exact frame index
                    plus.tStart = t  # local t and not account for scr refresh
                    plus.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(plus, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'plus.started')
                    # update status
                    plus.status = STARTED
                    plus.setAutoDraw(True)
                
                # if plus is active this frame...
                if plus.status == STARTED:
                    # update params
                    pass
                
                # if plus is stopping this frame...
                if plus.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > plus.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        plus.tStop = t  # not accounting for scr refresh
                        plus.tStopRefresh = tThisFlipGlobal  # on global time
                        plus.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'plus.stopped')
                        # update status
                        plus.status = FINISHED
                        plus.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_4* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_4 is starting this frame...
                if debugging_press_enter_to_skip_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_4.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_4.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.started')
                    # update status
                    debugging_press_enter_to_skip_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_4 is stopping this frame...
                if debugging_press_enter_to_skip_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_4.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_4.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_4.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.stopped')
                        # update status
                        debugging_press_enter_to_skip_4.status = FINISHED
                        debugging_press_enter_to_skip_4.status = FINISHED
                if debugging_press_enter_to_skip_4.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_4.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_4_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_4_allKeys):
                        debugging_press_enter_to_skip_4.keys = _debugging_press_enter_to_skip_4_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_4.rt = _debugging_press_enter_to_skip_4_allKeys[-1].rt
                        debugging_press_enter_to_skip_4.duration = _debugging_press_enter_to_skip_4_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    plusBetween.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in plusBetween.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "plusBetween" ---
            for thisComponent in plusBetween.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for plusBetween
            plusBetween.tStop = globalClock.getTime(format='float')
            plusBetween.tStopRefresh = tThisFlipGlobal
            thisExp.addData('plusBetween.stopped', plusBetween.tStop)
            # check responses
            if debugging_press_enter_to_skip_4.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_4.keys = None
            practice_sets2.addData('debugging_press_enter_to_skip_4.keys',debugging_press_enter_to_skip_4.keys)
            if debugging_press_enter_to_skip_4.keys != None:  # we had a response
                practice_sets2.addData('debugging_press_enter_to_skip_4.rt', debugging_press_enter_to_skip_4.rt)
                practice_sets2.addData('debugging_press_enter_to_skip_4.duration', debugging_press_enter_to_skip_4.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if plusBetween.maxDurationReached:
                routineTimer.addTime(-plusBetween.maxDuration)
            elif plusBetween.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 6.0 repeats of 'practice_sets2'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "breakBetweenRepeats" ---
        # create an object to store info about Routine breakBetweenRepeats
        breakBetweenRepeats = data.Routine(
            name='breakBetweenRepeats',
            components=[five_seconds, maybe_a_beep, debugging_press_enter_to_skip_5],
        )
        breakBetweenRepeats.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        maybe_a_beep.setSound('A', secs=1.0, hamming=True)
        maybe_a_beep.setVolume(1.0, log=False)
        maybe_a_beep.seek(0)
        # create starting attributes for debugging_press_enter_to_skip_5
        debugging_press_enter_to_skip_5.keys = []
        debugging_press_enter_to_skip_5.rt = []
        _debugging_press_enter_to_skip_5_allKeys = []
        # store start times for breakBetweenRepeats
        breakBetweenRepeats.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        breakBetweenRepeats.tStart = globalClock.getTime(format='float')
        breakBetweenRepeats.status = STARTED
        thisExp.addData('breakBetweenRepeats.started', breakBetweenRepeats.tStart)
        breakBetweenRepeats.maxDuration = None
        # keep track of which components have finished
        breakBetweenRepeatsComponents = breakBetweenRepeats.components
        for thisComponent in breakBetweenRepeats.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "breakBetweenRepeats" ---
        # if trial has changed, end Routine now
        if isinstance(practice_imagess, data.TrialHandler2) and thisPractice_images.thisN != practice_imagess.thisTrial.thisN:
            continueRoutine = False
        breakBetweenRepeats.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *five_seconds* updates
            
            # if five_seconds is starting this frame...
            if five_seconds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                five_seconds.frameNStart = frameN  # exact frame index
                five_seconds.tStart = t  # local t and not account for scr refresh
                five_seconds.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(five_seconds, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'five_seconds.started')
                # update status
                five_seconds.status = STARTED
                five_seconds.setAutoDraw(True)
            
            # if five_seconds is active this frame...
            if five_seconds.status == STARTED:
                # update params
                pass
            
            # if five_seconds is stopping this frame...
            if five_seconds.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > five_seconds.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    five_seconds.tStop = t  # not accounting for scr refresh
                    five_seconds.tStopRefresh = tThisFlipGlobal  # on global time
                    five_seconds.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'five_seconds.stopped')
                    # update status
                    five_seconds.status = FINISHED
                    five_seconds.setAutoDraw(False)
            
            # *maybe_a_beep* updates
            
            # if maybe_a_beep is starting this frame...
            if maybe_a_beep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                maybe_a_beep.frameNStart = frameN  # exact frame index
                maybe_a_beep.tStart = t  # local t and not account for scr refresh
                maybe_a_beep.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('maybe_a_beep.started', tThisFlipGlobal)
                # update status
                maybe_a_beep.status = STARTED
                maybe_a_beep.play(when=win)  # sync with win flip
            
            # if maybe_a_beep is stopping this frame...
            if maybe_a_beep.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > maybe_a_beep.tStartRefresh + 1.0-frameTolerance or maybe_a_beep.isFinished:
                    # keep track of stop time/frame for later
                    maybe_a_beep.tStop = t  # not accounting for scr refresh
                    maybe_a_beep.tStopRefresh = tThisFlipGlobal  # on global time
                    maybe_a_beep.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'maybe_a_beep.stopped')
                    # update status
                    maybe_a_beep.status = FINISHED
                    maybe_a_beep.stop()
            
            # *debugging_press_enter_to_skip_5* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_5 is starting this frame...
            if debugging_press_enter_to_skip_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_5.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_5.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.started')
                # update status
                debugging_press_enter_to_skip_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if debugging_press_enter_to_skip_5 is stopping this frame...
            if debugging_press_enter_to_skip_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > debugging_press_enter_to_skip_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    debugging_press_enter_to_skip_5.tStop = t  # not accounting for scr refresh
                    debugging_press_enter_to_skip_5.tStopRefresh = tThisFlipGlobal  # on global time
                    debugging_press_enter_to_skip_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.stopped')
                    # update status
                    debugging_press_enter_to_skip_5.status = FINISHED
                    debugging_press_enter_to_skip_5.status = FINISHED
            if debugging_press_enter_to_skip_5.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_5.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_5_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_5_allKeys):
                    debugging_press_enter_to_skip_5.keys = _debugging_press_enter_to_skip_5_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_5.rt = _debugging_press_enter_to_skip_5_allKeys[-1].rt
                    debugging_press_enter_to_skip_5.duration = _debugging_press_enter_to_skip_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[maybe_a_beep]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                breakBetweenRepeats.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in breakBetweenRepeats.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "breakBetweenRepeats" ---
        for thisComponent in breakBetweenRepeats.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for breakBetweenRepeats
        breakBetweenRepeats.tStop = globalClock.getTime(format='float')
        breakBetweenRepeats.tStopRefresh = tThisFlipGlobal
        thisExp.addData('breakBetweenRepeats.stopped', breakBetweenRepeats.tStop)
        maybe_a_beep.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if debugging_press_enter_to_skip_5.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_5.keys = None
        practice_imagess.addData('debugging_press_enter_to_skip_5.keys',debugging_press_enter_to_skip_5.keys)
        if debugging_press_enter_to_skip_5.keys != None:  # we had a response
            practice_imagess.addData('debugging_press_enter_to_skip_5.rt', debugging_press_enter_to_skip_5.rt)
            practice_imagess.addData('debugging_press_enter_to_skip_5.duration', debugging_press_enter_to_skip_5.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if breakBetweenRepeats.maxDurationReached:
            routineTimer.addTime(-breakBetweenRepeats.maxDuration)
        elif breakBetweenRepeats.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed numReps repeats of 'practice_imagess'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    practice_testt = data.TrialHandler2(
        name='practice_testt',
        nReps=12.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(practice_testt)  # add the loop to the experiment
    thisPractice_testt = practice_testt.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_testt.rgb)
    if thisPractice_testt != None:
        for paramName in thisPractice_testt:
            globals()[paramName] = thisPractice_testt[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractice_testt in practice_testt:
        currentLoop = practice_testt
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_testt.rgb)
        if thisPractice_testt != None:
            for paramName in thisPractice_testt:
                globals()[paramName] = thisPractice_testt[paramName]
        
        # --- Prepare to start Routine "practice_test" ---
        # create an object to store info about Routine practice_test
        practice_test = data.Routine(
            name='practice_test',
            components=[textAmharic_9, textOptionA_9, textOptionB_9, textOptionC_9, textOptionD_9, textDiamond_8, key_resp_10, debugging_press_enter_to_skip_23],
        )
        practice_test.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeSymbol_9
        #incraments item counter by one
        curr_item += 1
        
        correct_word_p = practice_words[curr_item] #THIS IS THE RIGHT ANSWER   
        amharic_p = practice_amharic[curr_item]
        
        #preparing answer choices 
        lottery_list_p = []
        
        #add the right answer
        lottery_list_p.append(correct_word_p)
        
        #add 3 more non repeating answers
        copied_word_listP = []
        copied_word_listP = practice_words.copy() #copy word list
        copied_word_listP.remove(correct_word_p) #remove the right answer
        shuffle(copied_word_listP) #shuffle up the copied list
        
        for x in range(0,3):    #add 3 from the shuffled list
            lottery_list_p.append(copied_word_listP[x])
        
        random.shuffle(lottery_list_p)  #mix up the answer choices
        
        index_of_correct_answer = lottery_list_p.index(correct_word_p) #index of the correct word
        
        correctAns = index_to_button[index_of_correct_answer] #correct answer in key form
        textAmharic_9.setText(amharic_p
        )
        textOptionA_9.setText(lottery_list_p[0]
        
        )
        textOptionB_9.setText(lottery_list_p[1])
        textOptionC_9.setText(lottery_list_p[2])
        textOptionD_9.setText(lottery_list_p[3])
        textDiamond_8.setText(f"     {lottery_list_p[0]}\n   {lottery_list_p[1]}   {lottery_list_p[2]}\n     {lottery_list_p[3]}")
        # create starting attributes for key_resp_10
        key_resp_10.keys = []
        key_resp_10.rt = []
        _key_resp_10_allKeys = []
        # create starting attributes for debugging_press_enter_to_skip_23
        debugging_press_enter_to_skip_23.keys = []
        debugging_press_enter_to_skip_23.rt = []
        _debugging_press_enter_to_skip_23_allKeys = []
        # store start times for practice_test
        practice_test.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practice_test.tStart = globalClock.getTime(format='float')
        practice_test.status = STARTED
        thisExp.addData('practice_test.started', practice_test.tStart)
        practice_test.maxDuration = None
        # keep track of which components have finished
        practice_testComponents = practice_test.components
        for thisComponent in practice_test.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_test" ---
        # if trial has changed, end Routine now
        if isinstance(practice_testt, data.TrialHandler2) and thisPractice_testt.thisN != practice_testt.thisTrial.thisN:
            continueRoutine = False
        practice_test.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textAmharic_9* updates
            
            # if textAmharic_9 is starting this frame...
            if textAmharic_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textAmharic_9.frameNStart = frameN  # exact frame index
                textAmharic_9.tStart = t  # local t and not account for scr refresh
                textAmharic_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textAmharic_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textAmharic_9.started')
                # update status
                textAmharic_9.status = STARTED
                textAmharic_9.setAutoDraw(True)
            
            # if textAmharic_9 is active this frame...
            if textAmharic_9.status == STARTED:
                # update params
                pass
            
            # *textOptionA_9* updates
            
            # if textOptionA_9 is starting this frame...
            if textOptionA_9.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionA_9.frameNStart = frameN  # exact frame index
                textOptionA_9.tStart = t  # local t and not account for scr refresh
                textOptionA_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionA_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionA_9.started')
                # update status
                textOptionA_9.status = STARTED
                textOptionA_9.setAutoDraw(True)
            
            # if textOptionA_9 is active this frame...
            if textOptionA_9.status == STARTED:
                # update params
                pass
            
            # if textOptionA_9 is stopping this frame...
            if textOptionA_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionA_9.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionA_9.tStop = t  # not accounting for scr refresh
                    textOptionA_9.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionA_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionA_9.stopped')
                    # update status
                    textOptionA_9.status = FINISHED
                    textOptionA_9.setAutoDraw(False)
            
            # *textOptionB_9* updates
            
            # if textOptionB_9 is starting this frame...
            if textOptionB_9.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionB_9.frameNStart = frameN  # exact frame index
                textOptionB_9.tStart = t  # local t and not account for scr refresh
                textOptionB_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionB_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionB_9.started')
                # update status
                textOptionB_9.status = STARTED
                textOptionB_9.setAutoDraw(True)
            
            # if textOptionB_9 is active this frame...
            if textOptionB_9.status == STARTED:
                # update params
                pass
            
            # if textOptionB_9 is stopping this frame...
            if textOptionB_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionB_9.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionB_9.tStop = t  # not accounting for scr refresh
                    textOptionB_9.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionB_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionB_9.stopped')
                    # update status
                    textOptionB_9.status = FINISHED
                    textOptionB_9.setAutoDraw(False)
            
            # *textOptionC_9* updates
            
            # if textOptionC_9 is starting this frame...
            if textOptionC_9.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionC_9.frameNStart = frameN  # exact frame index
                textOptionC_9.tStart = t  # local t and not account for scr refresh
                textOptionC_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionC_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionC_9.started')
                # update status
                textOptionC_9.status = STARTED
                textOptionC_9.setAutoDraw(True)
            
            # if textOptionC_9 is active this frame...
            if textOptionC_9.status == STARTED:
                # update params
                pass
            
            # if textOptionC_9 is stopping this frame...
            if textOptionC_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionC_9.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionC_9.tStop = t  # not accounting for scr refresh
                    textOptionC_9.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionC_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionC_9.stopped')
                    # update status
                    textOptionC_9.status = FINISHED
                    textOptionC_9.setAutoDraw(False)
            
            # *textOptionD_9* updates
            
            # if textOptionD_9 is starting this frame...
            if textOptionD_9.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionD_9.frameNStart = frameN  # exact frame index
                textOptionD_9.tStart = t  # local t and not account for scr refresh
                textOptionD_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionD_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionD_9.started')
                # update status
                textOptionD_9.status = STARTED
                textOptionD_9.setAutoDraw(True)
            
            # if textOptionD_9 is active this frame...
            if textOptionD_9.status == STARTED:
                # update params
                pass
            
            # if textOptionD_9 is stopping this frame...
            if textOptionD_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionD_9.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionD_9.tStop = t  # not accounting for scr refresh
                    textOptionD_9.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionD_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionD_9.stopped')
                    # update status
                    textOptionD_9.status = FINISHED
                    textOptionD_9.setAutoDraw(False)
            
            # *textDiamond_8* updates
            
            # if textDiamond_8 is starting this frame...
            if textDiamond_8.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                textDiamond_8.frameNStart = frameN  # exact frame index
                textDiamond_8.tStart = t  # local t and not account for scr refresh
                textDiamond_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textDiamond_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textDiamond_8.started')
                # update status
                textDiamond_8.status = STARTED
                textDiamond_8.setAutoDraw(True)
            
            # if textDiamond_8 is active this frame...
            if textDiamond_8.status == STARTED:
                # update params
                pass
            
            # *key_resp_10* updates
            waitOnFlip = False
            
            # if key_resp_10 is starting this frame...
            if key_resp_10.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_10.frameNStart = frameN  # exact frame index
                key_resp_10.tStart = t  # local t and not account for scr refresh
                key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_10.started')
                # update status
                key_resp_10.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_10.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_10.getKeys(keyList=['right','up','left','down', 'space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_10_allKeys.extend(theseKeys)
                if len(_key_resp_10_allKeys):
                    key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                    key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                    key_resp_10.duration = _key_resp_10_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_10.keys == str(correctAns)) or (key_resp_10.keys == correctAns):
                        key_resp_10.corr = 1
                    else:
                        key_resp_10.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *debugging_press_enter_to_skip_23* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_23 is starting this frame...
            if debugging_press_enter_to_skip_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_23.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_23.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_23.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_23, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_23.started')
                # update status
                debugging_press_enter_to_skip_23.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_23.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if debugging_press_enter_to_skip_23.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_23.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_23_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_23_allKeys):
                    debugging_press_enter_to_skip_23.keys = _debugging_press_enter_to_skip_23_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_23.rt = _debugging_press_enter_to_skip_23_allKeys[-1].rt
                    debugging_press_enter_to_skip_23.duration = _debugging_press_enter_to_skip_23_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practice_test.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_test.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_test" ---
        for thisComponent in practice_test.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practice_test
        practice_test.tStop = globalClock.getTime(format='float')
        practice_test.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practice_test.stopped', practice_test.tStop)
        # check responses
        if key_resp_10.keys in ['', [], None]:  # No response was made
            key_resp_10.keys = None
            # was no response the correct answer?!
            if str(correctAns).lower() == 'none':
               key_resp_10.corr = 1;  # correct non-response
            else:
               key_resp_10.corr = 0;  # failed to respond (incorrectly)
        # store data for practice_testt (TrialHandler)
        practice_testt.addData('key_resp_10.keys',key_resp_10.keys)
        practice_testt.addData('key_resp_10.corr', key_resp_10.corr)
        if key_resp_10.keys != None:  # we had a response
            practice_testt.addData('key_resp_10.rt', key_resp_10.rt)
            practice_testt.addData('key_resp_10.duration', key_resp_10.duration)
        # check responses
        if debugging_press_enter_to_skip_23.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_23.keys = None
        practice_testt.addData('debugging_press_enter_to_skip_23.keys',debugging_press_enter_to_skip_23.keys)
        if debugging_press_enter_to_skip_23.keys != None:  # we had a response
            practice_testt.addData('debugging_press_enter_to_skip_23.rt', debugging_press_enter_to_skip_23.rt)
            practice_testt.addData('debugging_press_enter_to_skip_23.duration', debugging_press_enter_to_skip_23.duration)
        # the Routine "practice_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "checkForCorr_5" ---
        # create an object to store info about Routine checkForCorr_5
        checkForCorr_5 = data.Routine(
            name='checkForCorr_5',
            components=[],
        )
        checkForCorr_5.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_7
        if key_resp_10.corr == 1:
            checkmark_reps = 1
            xmark_reps = 0
        if key_resp_10.corr == 0:
            checkmark_reps = 0
            xmark_reps = 1
        # store start times for checkForCorr_5
        checkForCorr_5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        checkForCorr_5.tStart = globalClock.getTime(format='float')
        checkForCorr_5.status = STARTED
        thisExp.addData('checkForCorr_5.started', checkForCorr_5.tStart)
        checkForCorr_5.maxDuration = None
        # keep track of which components have finished
        checkForCorr_5Components = checkForCorr_5.components
        for thisComponent in checkForCorr_5.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "checkForCorr_5" ---
        # if trial has changed, end Routine now
        if isinstance(practice_testt, data.TrialHandler2) and thisPractice_testt.thisN != practice_testt.thisTrial.thisN:
            continueRoutine = False
        checkForCorr_5.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                checkForCorr_5.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in checkForCorr_5.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "checkForCorr_5" ---
        for thisComponent in checkForCorr_5.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for checkForCorr_5
        checkForCorr_5.tStop = globalClock.getTime(format='float')
        checkForCorr_5.tStopRefresh = tThisFlipGlobal
        thisExp.addData('checkForCorr_5.stopped', checkForCorr_5.tStop)
        # the Routine "checkForCorr_5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        checkLoop = data.TrialHandler2(
            name='checkLoop',
            nReps=checkmark_reps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(checkLoop)  # add the loop to the experiment
        thisCheckLoop = checkLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisCheckLoop.rgb)
        if thisCheckLoop != None:
            for paramName in thisCheckLoop:
                globals()[paramName] = thisCheckLoop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisCheckLoop in checkLoop:
            currentLoop = checkLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisCheckLoop.rgb)
            if thisCheckLoop != None:
                for paramName in thisCheckLoop:
                    globals()[paramName] = thisCheckLoop[paramName]
            
            # --- Prepare to start Routine "checkmark" ---
            # create an object to store info about Routine checkmark
            checkmark = data.Routine(
                name='checkmark',
                components=[textCheck, debugging_press_enter_to_skip_7],
            )
            checkmark.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textCheck.setText(markers[0])
            # create starting attributes for debugging_press_enter_to_skip_7
            debugging_press_enter_to_skip_7.keys = []
            debugging_press_enter_to_skip_7.rt = []
            _debugging_press_enter_to_skip_7_allKeys = []
            # store start times for checkmark
            checkmark.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            checkmark.tStart = globalClock.getTime(format='float')
            checkmark.status = STARTED
            thisExp.addData('checkmark.started', checkmark.tStart)
            checkmark.maxDuration = None
            # keep track of which components have finished
            checkmarkComponents = checkmark.components
            for thisComponent in checkmark.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "checkmark" ---
            # if trial has changed, end Routine now
            if isinstance(checkLoop, data.TrialHandler2) and thisCheckLoop.thisN != checkLoop.thisTrial.thisN:
                continueRoutine = False
            checkmark.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textCheck* updates
                
                # if textCheck is starting this frame...
                if textCheck.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textCheck.frameNStart = frameN  # exact frame index
                    textCheck.tStart = t  # local t and not account for scr refresh
                    textCheck.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textCheck, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textCheck.started')
                    # update status
                    textCheck.status = STARTED
                    textCheck.setAutoDraw(True)
                
                # if textCheck is active this frame...
                if textCheck.status == STARTED:
                    # update params
                    pass
                
                # if textCheck is stopping this frame...
                if textCheck.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textCheck.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textCheck.tStop = t  # not accounting for scr refresh
                        textCheck.tStopRefresh = tThisFlipGlobal  # on global time
                        textCheck.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textCheck.stopped')
                        # update status
                        textCheck.status = FINISHED
                        textCheck.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_7* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_7 is starting this frame...
                if debugging_press_enter_to_skip_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_7.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_7.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_7.started')
                    # update status
                    debugging_press_enter_to_skip_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_7.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_7 is stopping this frame...
                if debugging_press_enter_to_skip_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_7.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_7.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_7.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_7.stopped')
                        # update status
                        debugging_press_enter_to_skip_7.status = FINISHED
                        debugging_press_enter_to_skip_7.status = FINISHED
                if debugging_press_enter_to_skip_7.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_7.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_7_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_7_allKeys):
                        debugging_press_enter_to_skip_7.keys = _debugging_press_enter_to_skip_7_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_7.rt = _debugging_press_enter_to_skip_7_allKeys[-1].rt
                        debugging_press_enter_to_skip_7.duration = _debugging_press_enter_to_skip_7_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    checkmark.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in checkmark.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "checkmark" ---
            for thisComponent in checkmark.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for checkmark
            checkmark.tStop = globalClock.getTime(format='float')
            checkmark.tStopRefresh = tThisFlipGlobal
            thisExp.addData('checkmark.stopped', checkmark.tStop)
            # check responses
            if debugging_press_enter_to_skip_7.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_7.keys = None
            checkLoop.addData('debugging_press_enter_to_skip_7.keys',debugging_press_enter_to_skip_7.keys)
            if debugging_press_enter_to_skip_7.keys != None:  # we had a response
                checkLoop.addData('debugging_press_enter_to_skip_7.rt', debugging_press_enter_to_skip_7.rt)
                checkLoop.addData('debugging_press_enter_to_skip_7.duration', debugging_press_enter_to_skip_7.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if checkmark.maxDurationReached:
                routineTimer.addTime(-checkmark.maxDuration)
            elif checkmark.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed checkmark_reps repeats of 'checkLoop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        xmarkLoop = data.TrialHandler2(
            name='xmarkLoop',
            nReps=xmark_reps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(xmarkLoop)  # add the loop to the experiment
        thisXmarkLoop = xmarkLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisXmarkLoop.rgb)
        if thisXmarkLoop != None:
            for paramName in thisXmarkLoop:
                globals()[paramName] = thisXmarkLoop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisXmarkLoop in xmarkLoop:
            currentLoop = xmarkLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisXmarkLoop.rgb)
            if thisXmarkLoop != None:
                for paramName in thisXmarkLoop:
                    globals()[paramName] = thisXmarkLoop[paramName]
            
            # --- Prepare to start Routine "xmark" ---
            # create an object to store info about Routine xmark
            xmark = data.Routine(
                name='xmark',
                components=[textXmark, debugging_press_enter_to_skip_26],
            )
            xmark.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textXmark.setText(markers[1])
            # create starting attributes for debugging_press_enter_to_skip_26
            debugging_press_enter_to_skip_26.keys = []
            debugging_press_enter_to_skip_26.rt = []
            _debugging_press_enter_to_skip_26_allKeys = []
            # store start times for xmark
            xmark.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            xmark.tStart = globalClock.getTime(format='float')
            xmark.status = STARTED
            thisExp.addData('xmark.started', xmark.tStart)
            xmark.maxDuration = None
            # keep track of which components have finished
            xmarkComponents = xmark.components
            for thisComponent in xmark.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "xmark" ---
            # if trial has changed, end Routine now
            if isinstance(xmarkLoop, data.TrialHandler2) and thisXmarkLoop.thisN != xmarkLoop.thisTrial.thisN:
                continueRoutine = False
            xmark.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textXmark* updates
                
                # if textXmark is starting this frame...
                if textXmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textXmark.frameNStart = frameN  # exact frame index
                    textXmark.tStart = t  # local t and not account for scr refresh
                    textXmark.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textXmark, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textXmark.started')
                    # update status
                    textXmark.status = STARTED
                    textXmark.setAutoDraw(True)
                
                # if textXmark is active this frame...
                if textXmark.status == STARTED:
                    # update params
                    pass
                
                # if textXmark is stopping this frame...
                if textXmark.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textXmark.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textXmark.tStop = t  # not accounting for scr refresh
                        textXmark.tStopRefresh = tThisFlipGlobal  # on global time
                        textXmark.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textXmark.stopped')
                        # update status
                        textXmark.status = FINISHED
                        textXmark.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_26* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_26 is starting this frame...
                if debugging_press_enter_to_skip_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_26.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_26.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_26, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_26.started')
                    # update status
                    debugging_press_enter_to_skip_26.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_26.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_26 is stopping this frame...
                if debugging_press_enter_to_skip_26.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_26.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_26.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_26.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_26.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_26.stopped')
                        # update status
                        debugging_press_enter_to_skip_26.status = FINISHED
                        debugging_press_enter_to_skip_26.status = FINISHED
                if debugging_press_enter_to_skip_26.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_26.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_26_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_26_allKeys):
                        debugging_press_enter_to_skip_26.keys = _debugging_press_enter_to_skip_26_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_26.rt = _debugging_press_enter_to_skip_26_allKeys[-1].rt
                        debugging_press_enter_to_skip_26.duration = _debugging_press_enter_to_skip_26_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    xmark.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in xmark.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "xmark" ---
            for thisComponent in xmark.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for xmark
            xmark.tStop = globalClock.getTime(format='float')
            xmark.tStopRefresh = tThisFlipGlobal
            thisExp.addData('xmark.stopped', xmark.tStop)
            # check responses
            if debugging_press_enter_to_skip_26.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_26.keys = None
            xmarkLoop.addData('debugging_press_enter_to_skip_26.keys',debugging_press_enter_to_skip_26.keys)
            if debugging_press_enter_to_skip_26.keys != None:  # we had a response
                xmarkLoop.addData('debugging_press_enter_to_skip_26.rt', debugging_press_enter_to_skip_26.rt)
                xmarkLoop.addData('debugging_press_enter_to_skip_26.duration', debugging_press_enter_to_skip_26.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if xmark.maxDurationReached:
                routineTimer.addTime(-xmark.maxDuration)
            elif xmark.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed xmark_reps repeats of 'xmarkLoop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "resetReps" ---
        # create an object to store info about Routine resetReps
        resetReps = data.Routine(
            name='resetReps',
            components=[],
        )
        resetReps.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for resetReps
        resetReps.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        resetReps.tStart = globalClock.getTime(format='float')
        resetReps.status = STARTED
        thisExp.addData('resetReps.started', resetReps.tStart)
        resetReps.maxDuration = None
        # keep track of which components have finished
        resetRepsComponents = resetReps.components
        for thisComponent in resetReps.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "resetReps" ---
        # if trial has changed, end Routine now
        if isinstance(practice_testt, data.TrialHandler2) and thisPractice_testt.thisN != practice_testt.thisTrial.thisN:
            continueRoutine = False
        resetReps.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                resetReps.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in resetReps.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "resetReps" ---
        for thisComponent in resetReps.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for resetReps
        resetReps.tStop = globalClock.getTime(format='float')
        resetReps.tStopRefresh = tThisFlipGlobal
        thisExp.addData('resetReps.stopped', resetReps.tStop)
        # the Routine "resetReps" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        # create an object to store info about Routine blank500
        blank500 = data.Routine(
            name='blank500',
            components=[text_2, debugging_press_enter_to_skip_15],
        )
        blank500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_2.setText('')
        # create starting attributes for debugging_press_enter_to_skip_15
        debugging_press_enter_to_skip_15.keys = []
        debugging_press_enter_to_skip_15.rt = []
        _debugging_press_enter_to_skip_15_allKeys = []
        # store start times for blank500
        blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank500.tStart = globalClock.getTime(format='float')
        blank500.status = STARTED
        thisExp.addData('blank500.started', blank500.tStart)
        blank500.maxDuration = None
        # keep track of which components have finished
        blank500Components = blank500.components
        for thisComponent in blank500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        # if trial has changed, end Routine now
        if isinstance(practice_testt, data.TrialHandler2) and thisPractice_testt.thisN != practice_testt.thisTrial.thisN:
            continueRoutine = False
        blank500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # *debugging_press_enter_to_skip_15* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_15 is starting this frame...
            if debugging_press_enter_to_skip_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_15.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_15.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_15.started')
                # update status
                debugging_press_enter_to_skip_15.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_15.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if debugging_press_enter_to_skip_15 is stopping this frame...
            if debugging_press_enter_to_skip_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > debugging_press_enter_to_skip_15.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    debugging_press_enter_to_skip_15.tStop = t  # not accounting for scr refresh
                    debugging_press_enter_to_skip_15.tStopRefresh = tThisFlipGlobal  # on global time
                    debugging_press_enter_to_skip_15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_15.stopped')
                    # update status
                    debugging_press_enter_to_skip_15.status = FINISHED
                    debugging_press_enter_to_skip_15.status = FINISHED
            if debugging_press_enter_to_skip_15.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_15.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_15_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_15_allKeys):
                    debugging_press_enter_to_skip_15.keys = _debugging_press_enter_to_skip_15_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_15.rt = _debugging_press_enter_to_skip_15_allKeys[-1].rt
                    debugging_press_enter_to_skip_15.duration = _debugging_press_enter_to_skip_15_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank500
        blank500.tStop = globalClock.getTime(format='float')
        blank500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank500.stopped', blank500.tStop)
        # check responses
        if debugging_press_enter_to_skip_15.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_15.keys = None
        practice_testt.addData('debugging_press_enter_to_skip_15.keys',debugging_press_enter_to_skip_15.keys)
        if debugging_press_enter_to_skip_15.keys != None:  # we had a response
            practice_testt.addData('debugging_press_enter_to_skip_15.rt', debugging_press_enter_to_skip_15.rt)
            practice_testt.addData('debugging_press_enter_to_skip_15.duration', debugging_press_enter_to_skip_15.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank500.maxDurationReached:
            routineTimer.addTime(-blank500.maxDuration)
        elif blank500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed 12.0 repeats of 'practice_testt'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "WelcomeScreen" ---
    # create an object to store info about Routine WelcomeScreen
    WelcomeScreen = data.Routine(
        name='WelcomeScreen',
        components=[text_3, Press_Space_When_Ready],
    )
    WelcomeScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for Press_Space_When_Ready
    Press_Space_When_Ready.keys = []
    Press_Space_When_Ready.rt = []
    _Press_Space_When_Ready_allKeys = []
    # store start times for WelcomeScreen
    WelcomeScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    WelcomeScreen.tStart = globalClock.getTime(format='float')
    WelcomeScreen.status = STARTED
    thisExp.addData('WelcomeScreen.started', WelcomeScreen.tStart)
    WelcomeScreen.maxDuration = None
    # keep track of which components have finished
    WelcomeScreenComponents = WelcomeScreen.components
    for thisComponent in WelcomeScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "WelcomeScreen" ---
    WelcomeScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # *Press_Space_When_Ready* updates
        waitOnFlip = False
        
        # if Press_Space_When_Ready is starting this frame...
        if Press_Space_When_Ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Press_Space_When_Ready.frameNStart = frameN  # exact frame index
            Press_Space_When_Ready.tStart = t  # local t and not account for scr refresh
            Press_Space_When_Ready.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Press_Space_When_Ready, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Press_Space_When_Ready.started')
            # update status
            Press_Space_When_Ready.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Press_Space_When_Ready.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Press_Space_When_Ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Press_Space_When_Ready.status == STARTED and not waitOnFlip:
            theseKeys = Press_Space_When_Ready.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Press_Space_When_Ready_allKeys.extend(theseKeys)
            if len(_Press_Space_When_Ready_allKeys):
                Press_Space_When_Ready.keys = _Press_Space_When_Ready_allKeys[-1].name  # just the last key pressed
                Press_Space_When_Ready.rt = _Press_Space_When_Ready_allKeys[-1].rt
                Press_Space_When_Ready.duration = _Press_Space_When_Ready_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            WelcomeScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WelcomeScreen" ---
    for thisComponent in WelcomeScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for WelcomeScreen
    WelcomeScreen.tStop = globalClock.getTime(format='float')
    WelcomeScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('WelcomeScreen.stopped', WelcomeScreen.tStop)
    # check responses
    if Press_Space_When_Ready.keys in ['', [], None]:  # No response was made
        Press_Space_When_Ready.keys = None
    thisExp.addData('Press_Space_When_Ready.keys',Press_Space_When_Ready.keys)
    if Press_Space_When_Ready.keys != None:  # we had a response
        thisExp.addData('Press_Space_When_Ready.rt', Press_Space_When_Ready.rt)
        thisExp.addData('Press_Space_When_Ready.duration', Press_Space_When_Ready.duration)
    thisExp.nextEntry()
    # the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    LearningSetOne = data.TrialHandler2(
        name='LearningSetOne',
        nReps=numReps, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(LearningSetOne)  # add the loop to the experiment
    thisLearningSetOne = LearningSetOne.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLearningSetOne.rgb)
    if thisLearningSetOne != None:
        for paramName in thisLearningSetOne:
            globals()[paramName] = thisLearningSetOne[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLearningSetOne in LearningSetOne:
        currentLoop = LearningSetOne
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLearningSetOne.rgb)
        if thisLearningSetOne != None:
            for paramName in thisLearningSetOne:
                globals()[paramName] = thisLearningSetOne[paramName]
        
        # --- Prepare to start Routine "randomize_set" ---
        # create an object to store info about Routine randomize_set
        randomize_set = data.Routine(
            name='randomize_set',
            components=[],
        )
        randomize_set.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from randomize_learning_set
        keys = list(range(12))
        random.shuffle(keys)
        print("learning set order: " + str(keys))
        
        practice_keys = list(range(6))
        random.shuffle(practice_keys)
        print("learning set order: " + str(keys))
        
        practice_keys2 = list(range(6,12))
        random.shuffle(practice_keys2)
        print("learning set order: " + str(keys))
        # store start times for randomize_set
        randomize_set.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        randomize_set.tStart = globalClock.getTime(format='float')
        randomize_set.status = STARTED
        thisExp.addData('randomize_set.started', randomize_set.tStart)
        randomize_set.maxDuration = None
        # keep track of which components have finished
        randomize_setComponents = randomize_set.components
        for thisComponent in randomize_set.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "randomize_set" ---
        # if trial has changed, end Routine now
        if isinstance(LearningSetOne, data.TrialHandler2) and thisLearningSetOne.thisN != LearningSetOne.thisTrial.thisN:
            continueRoutine = False
        randomize_set.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                randomize_set.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in randomize_set.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "randomize_set" ---
        for thisComponent in randomize_set.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for randomize_set
        randomize_set.tStop = globalClock.getTime(format='float')
        randomize_set.tStopRefresh = tThisFlipGlobal
        thisExp.addData('randomize_set.stopped', randomize_set.tStop)
        # the Routine "randomize_set" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        setOne = data.TrialHandler2(
            name='setOne',
            nReps=12.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(setOne)  # add the loop to the experiment
        thisSetOne = setOne.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSetOne.rgb)
        if thisSetOne != None:
            for paramName in thisSetOne:
                globals()[paramName] = thisSetOne[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisSetOne in setOne:
            currentLoop = setOne
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisSetOne.rgb)
            if thisSetOne != None:
                for paramName in thisSetOne:
                    globals()[paramName] = thisSetOne[paramName]
            
            # --- Prepare to start Routine "Increment" ---
            # create an object to store info about Routine Increment
            Increment = data.Routine(
                name='Increment',
                components=[],
            )
            Increment.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from increment_index
            learning_index += 1
            learning_index %= len(keys)
            
            practice_index += 1
            practice_index %= len(practice_keys)
            # store start times for Increment
            Increment.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Increment.tStart = globalClock.getTime(format='float')
            Increment.status = STARTED
            thisExp.addData('Increment.started', Increment.tStart)
            Increment.maxDuration = None
            # keep track of which components have finished
            IncrementComponents = Increment.components
            for thisComponent in Increment.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Increment" ---
            # if trial has changed, end Routine now
            if isinstance(setOne, data.TrialHandler2) and thisSetOne.thisN != setOne.thisTrial.thisN:
                continueRoutine = False
            Increment.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Increment.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Increment.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Increment" ---
            for thisComponent in Increment.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Increment
            Increment.tStop = globalClock.getTime(format='float')
            Increment.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Increment.stopped', Increment.tStop)
            # the Routine "Increment" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            nreps_A1 = data.TrialHandler2(
                name='nreps_A1',
                nReps=nreps_A, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(nreps_A1)  # add the loop to the experiment
            thisNreps_A1 = nreps_A1.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisNreps_A1.rgb)
            if thisNreps_A1 != None:
                for paramName in thisNreps_A1:
                    globals()[paramName] = thisNreps_A1[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisNreps_A1 in nreps_A1:
                currentLoop = nreps_A1
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisNreps_A1.rgb)
                if thisNreps_A1 != None:
                    for paramName in thisNreps_A1:
                        globals()[paramName] = thisNreps_A1[paramName]
                
                # --- Prepare to start Routine "amharic1_A" ---
                # create an object to store info about Routine amharic1_A
                amharic1_A = data.Routine(
                    name='amharic1_A',
                    components=[amharics1, words1, debugging_press_enter_to_skip],
                )
                amharic1_A.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                amharics1.setText(amharic_word_list1[keys[learning_index]][0])
                words1.setText(amharic_word_list1[keys[learning_index]][1])
                # Run 'Begin Routine' code from amharic_word_code1_3
                print("Index: " + str(keys[learning_index]) + 
                      "\n Character: " + str(amharic_word_list1[keys[learning_index]][0]) + 
                      "\n Meaning: " + str(amharic_word_list1[keys[learning_index]][1]) + 
                      "\n Image Path: " + str(amharic_word_list1[keys[learning_index]][2]))
                # create starting attributes for debugging_press_enter_to_skip
                debugging_press_enter_to_skip.keys = []
                debugging_press_enter_to_skip.rt = []
                _debugging_press_enter_to_skip_allKeys = []
                # store start times for amharic1_A
                amharic1_A.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                amharic1_A.tStart = globalClock.getTime(format='float')
                amharic1_A.status = STARTED
                thisExp.addData('amharic1_A.started', amharic1_A.tStart)
                amharic1_A.maxDuration = None
                # keep track of which components have finished
                amharic1_AComponents = amharic1_A.components
                for thisComponent in amharic1_A.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "amharic1_A" ---
                # if trial has changed, end Routine now
                if isinstance(nreps_A1, data.TrialHandler2) and thisNreps_A1.thisN != nreps_A1.thisTrial.thisN:
                    continueRoutine = False
                amharic1_A.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *amharics1* updates
                    
                    # if amharics1 is starting this frame...
                    if amharics1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        amharics1.frameNStart = frameN  # exact frame index
                        amharics1.tStart = t  # local t and not account for scr refresh
                        amharics1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(amharics1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'amharics1.started')
                        # update status
                        amharics1.status = STARTED
                        amharics1.setAutoDraw(True)
                    
                    # if amharics1 is active this frame...
                    if amharics1.status == STARTED:
                        # update params
                        pass
                    
                    # if amharics1 is stopping this frame...
                    if amharics1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > amharics1.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            amharics1.tStop = t  # not accounting for scr refresh
                            amharics1.tStopRefresh = tThisFlipGlobal  # on global time
                            amharics1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'amharics1.stopped')
                            # update status
                            amharics1.status = FINISHED
                            amharics1.setAutoDraw(False)
                    
                    # *words1* updates
                    
                    # if words1 is starting this frame...
                    if words1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        words1.frameNStart = frameN  # exact frame index
                        words1.tStart = t  # local t and not account for scr refresh
                        words1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(words1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'words1.started')
                        # update status
                        words1.status = STARTED
                        words1.setAutoDraw(True)
                    
                    # if words1 is active this frame...
                    if words1.status == STARTED:
                        # update params
                        pass
                    
                    # if words1 is stopping this frame...
                    if words1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > words1.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            words1.tStop = t  # not accounting for scr refresh
                            words1.tStopRefresh = tThisFlipGlobal  # on global time
                            words1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'words1.stopped')
                            # update status
                            words1.status = FINISHED
                            words1.setAutoDraw(False)
                    
                    # *debugging_press_enter_to_skip* updates
                    waitOnFlip = False
                    
                    # if debugging_press_enter_to_skip is starting this frame...
                    if debugging_press_enter_to_skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        debugging_press_enter_to_skip.frameNStart = frameN  # exact frame index
                        debugging_press_enter_to_skip.tStart = t  # local t and not account for scr refresh
                        debugging_press_enter_to_skip.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(debugging_press_enter_to_skip, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip.started')
                        # update status
                        debugging_press_enter_to_skip.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(debugging_press_enter_to_skip.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(debugging_press_enter_to_skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if debugging_press_enter_to_skip is stopping this frame...
                    if debugging_press_enter_to_skip.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > debugging_press_enter_to_skip.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            debugging_press_enter_to_skip.tStop = t  # not accounting for scr refresh
                            debugging_press_enter_to_skip.tStopRefresh = tThisFlipGlobal  # on global time
                            debugging_press_enter_to_skip.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip.stopped')
                            # update status
                            debugging_press_enter_to_skip.status = FINISHED
                            debugging_press_enter_to_skip.status = FINISHED
                    if debugging_press_enter_to_skip.status == STARTED and not waitOnFlip:
                        theseKeys = debugging_press_enter_to_skip.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                        _debugging_press_enter_to_skip_allKeys.extend(theseKeys)
                        if len(_debugging_press_enter_to_skip_allKeys):
                            debugging_press_enter_to_skip.keys = _debugging_press_enter_to_skip_allKeys[-1].name  # just the last key pressed
                            debugging_press_enter_to_skip.rt = _debugging_press_enter_to_skip_allKeys[-1].rt
                            debugging_press_enter_to_skip.duration = _debugging_press_enter_to_skip_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        amharic1_A.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in amharic1_A.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "amharic1_A" ---
                for thisComponent in amharic1_A.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for amharic1_A
                amharic1_A.tStop = globalClock.getTime(format='float')
                amharic1_A.tStopRefresh = tThisFlipGlobal
                thisExp.addData('amharic1_A.stopped', amharic1_A.tStop)
                # check responses
                if debugging_press_enter_to_skip.keys in ['', [], None]:  # No response was made
                    debugging_press_enter_to_skip.keys = None
                nreps_A1.addData('debugging_press_enter_to_skip.keys',debugging_press_enter_to_skip.keys)
                if debugging_press_enter_to_skip.keys != None:  # we had a response
                    nreps_A1.addData('debugging_press_enter_to_skip.rt', debugging_press_enter_to_skip.rt)
                    nreps_A1.addData('debugging_press_enter_to_skip.duration', debugging_press_enter_to_skip.duration)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if amharic1_A.maxDurationReached:
                    routineTimer.addTime(-amharic1_A.maxDuration)
                elif amharic1_A.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
            # completed nreps_A repeats of 'nreps_A1'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # set up handler to look after randomisation of conditions etc
            nreps_B1 = data.TrialHandler2(
                name='nreps_B1',
                nReps=nreps_B, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(nreps_B1)  # add the loop to the experiment
            thisNreps_B1 = nreps_B1.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisNreps_B1.rgb)
            if thisNreps_B1 != None:
                for paramName in thisNreps_B1:
                    globals()[paramName] = thisNreps_B1[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisNreps_B1 in nreps_B1:
                currentLoop = nreps_B1
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisNreps_B1.rgb)
                if thisNreps_B1 != None:
                    for paramName in thisNreps_B1:
                        globals()[paramName] = thisNreps_B1[paramName]
                
                # --- Prepare to start Routine "amharic1_B" ---
                # create an object to store info about Routine amharic1_B
                amharic1_B = data.Routine(
                    name='amharic1_B',
                    components=[amharics1_2, words1_image_2, debugging_press_enter_to_skip_2],
                )
                amharic1_B.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                amharics1_2.setText(amharic_word_list1[keys[learning_index]][0])
                words1_image_2.setImage(amharic_word_list1[keys[learning_index]][2])
                # Run 'Begin Routine' code from amharic_word_code1_2
                print("Index: " + str(keys[learning_index]) + 
                      "\n Character: " + str(amharic_word_list1[keys[learning_index]][0]) + 
                      "\n Meaning: " + str(amharic_word_list1[keys[learning_index]][1]) + 
                      "\n Image Path: " + str(amharic_word_list1[keys[learning_index]][2]))
                # create starting attributes for debugging_press_enter_to_skip_2
                debugging_press_enter_to_skip_2.keys = []
                debugging_press_enter_to_skip_2.rt = []
                _debugging_press_enter_to_skip_2_allKeys = []
                # store start times for amharic1_B
                amharic1_B.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                amharic1_B.tStart = globalClock.getTime(format='float')
                amharic1_B.status = STARTED
                thisExp.addData('amharic1_B.started', amharic1_B.tStart)
                amharic1_B.maxDuration = None
                # keep track of which components have finished
                amharic1_BComponents = amharic1_B.components
                for thisComponent in amharic1_B.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "amharic1_B" ---
                # if trial has changed, end Routine now
                if isinstance(nreps_B1, data.TrialHandler2) and thisNreps_B1.thisN != nreps_B1.thisTrial.thisN:
                    continueRoutine = False
                amharic1_B.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *amharics1_2* updates
                    
                    # if amharics1_2 is starting this frame...
                    if amharics1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        amharics1_2.frameNStart = frameN  # exact frame index
                        amharics1_2.tStart = t  # local t and not account for scr refresh
                        amharics1_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(amharics1_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'amharics1_2.started')
                        # update status
                        amharics1_2.status = STARTED
                        amharics1_2.setAutoDraw(True)
                    
                    # if amharics1_2 is active this frame...
                    if amharics1_2.status == STARTED:
                        # update params
                        pass
                    
                    # if amharics1_2 is stopping this frame...
                    if amharics1_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > amharics1_2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            amharics1_2.tStop = t  # not accounting for scr refresh
                            amharics1_2.tStopRefresh = tThisFlipGlobal  # on global time
                            amharics1_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'amharics1_2.stopped')
                            # update status
                            amharics1_2.status = FINISHED
                            amharics1_2.setAutoDraw(False)
                    
                    # *words1_image_2* updates
                    
                    # if words1_image_2 is starting this frame...
                    if words1_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        words1_image_2.frameNStart = frameN  # exact frame index
                        words1_image_2.tStart = t  # local t and not account for scr refresh
                        words1_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(words1_image_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'words1_image_2.started')
                        # update status
                        words1_image_2.status = STARTED
                        words1_image_2.setAutoDraw(True)
                    
                    # if words1_image_2 is active this frame...
                    if words1_image_2.status == STARTED:
                        # update params
                        pass
                    
                    # if words1_image_2 is stopping this frame...
                    if words1_image_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > words1_image_2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            words1_image_2.tStop = t  # not accounting for scr refresh
                            words1_image_2.tStopRefresh = tThisFlipGlobal  # on global time
                            words1_image_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'words1_image_2.stopped')
                            # update status
                            words1_image_2.status = FINISHED
                            words1_image_2.setAutoDraw(False)
                    
                    # *debugging_press_enter_to_skip_2* updates
                    waitOnFlip = False
                    
                    # if debugging_press_enter_to_skip_2 is starting this frame...
                    if debugging_press_enter_to_skip_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        debugging_press_enter_to_skip_2.frameNStart = frameN  # exact frame index
                        debugging_press_enter_to_skip_2.tStart = t  # local t and not account for scr refresh
                        debugging_press_enter_to_skip_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(debugging_press_enter_to_skip_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_2.started')
                        # update status
                        debugging_press_enter_to_skip_2.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(debugging_press_enter_to_skip_2.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(debugging_press_enter_to_skip_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if debugging_press_enter_to_skip_2 is stopping this frame...
                    if debugging_press_enter_to_skip_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > debugging_press_enter_to_skip_2.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            debugging_press_enter_to_skip_2.tStop = t  # not accounting for scr refresh
                            debugging_press_enter_to_skip_2.tStopRefresh = tThisFlipGlobal  # on global time
                            debugging_press_enter_to_skip_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_2.stopped')
                            # update status
                            debugging_press_enter_to_skip_2.status = FINISHED
                            debugging_press_enter_to_skip_2.status = FINISHED
                    if debugging_press_enter_to_skip_2.status == STARTED and not waitOnFlip:
                        theseKeys = debugging_press_enter_to_skip_2.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                        _debugging_press_enter_to_skip_2_allKeys.extend(theseKeys)
                        if len(_debugging_press_enter_to_skip_2_allKeys):
                            debugging_press_enter_to_skip_2.keys = _debugging_press_enter_to_skip_2_allKeys[-1].name  # just the last key pressed
                            debugging_press_enter_to_skip_2.rt = _debugging_press_enter_to_skip_2_allKeys[-1].rt
                            debugging_press_enter_to_skip_2.duration = _debugging_press_enter_to_skip_2_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        amharic1_B.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in amharic1_B.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "amharic1_B" ---
                for thisComponent in amharic1_B.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for amharic1_B
                amharic1_B.tStop = globalClock.getTime(format='float')
                amharic1_B.tStopRefresh = tThisFlipGlobal
                thisExp.addData('amharic1_B.stopped', amharic1_B.tStop)
                # check responses
                if debugging_press_enter_to_skip_2.keys in ['', [], None]:  # No response was made
                    debugging_press_enter_to_skip_2.keys = None
                nreps_B1.addData('debugging_press_enter_to_skip_2.keys',debugging_press_enter_to_skip_2.keys)
                if debugging_press_enter_to_skip_2.keys != None:  # we had a response
                    nreps_B1.addData('debugging_press_enter_to_skip_2.rt', debugging_press_enter_to_skip_2.rt)
                    nreps_B1.addData('debugging_press_enter_to_skip_2.duration', debugging_press_enter_to_skip_2.duration)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if amharic1_B.maxDurationReached:
                    routineTimer.addTime(-amharic1_B.maxDuration)
                elif amharic1_B.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
            # completed nreps_B repeats of 'nreps_B1'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # --- Prepare to start Routine "plusBetween" ---
            # create an object to store info about Routine plusBetween
            plusBetween = data.Routine(
                name='plusBetween',
                components=[plus, debugging_press_enter_to_skip_4],
            )
            plusBetween.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            plus.setText('+')
            # create starting attributes for debugging_press_enter_to_skip_4
            debugging_press_enter_to_skip_4.keys = []
            debugging_press_enter_to_skip_4.rt = []
            _debugging_press_enter_to_skip_4_allKeys = []
            # store start times for plusBetween
            plusBetween.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            plusBetween.tStart = globalClock.getTime(format='float')
            plusBetween.status = STARTED
            thisExp.addData('plusBetween.started', plusBetween.tStart)
            plusBetween.maxDuration = None
            # keep track of which components have finished
            plusBetweenComponents = plusBetween.components
            for thisComponent in plusBetween.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "plusBetween" ---
            # if trial has changed, end Routine now
            if isinstance(setOne, data.TrialHandler2) and thisSetOne.thisN != setOne.thisTrial.thisN:
                continueRoutine = False
            plusBetween.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *plus* updates
                
                # if plus is starting this frame...
                if plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    plus.frameNStart = frameN  # exact frame index
                    plus.tStart = t  # local t and not account for scr refresh
                    plus.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(plus, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'plus.started')
                    # update status
                    plus.status = STARTED
                    plus.setAutoDraw(True)
                
                # if plus is active this frame...
                if plus.status == STARTED:
                    # update params
                    pass
                
                # if plus is stopping this frame...
                if plus.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > plus.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        plus.tStop = t  # not accounting for scr refresh
                        plus.tStopRefresh = tThisFlipGlobal  # on global time
                        plus.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'plus.stopped')
                        # update status
                        plus.status = FINISHED
                        plus.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_4* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_4 is starting this frame...
                if debugging_press_enter_to_skip_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_4.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_4.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.started')
                    # update status
                    debugging_press_enter_to_skip_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_4 is stopping this frame...
                if debugging_press_enter_to_skip_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_4.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_4.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_4.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.stopped')
                        # update status
                        debugging_press_enter_to_skip_4.status = FINISHED
                        debugging_press_enter_to_skip_4.status = FINISHED
                if debugging_press_enter_to_skip_4.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_4.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_4_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_4_allKeys):
                        debugging_press_enter_to_skip_4.keys = _debugging_press_enter_to_skip_4_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_4.rt = _debugging_press_enter_to_skip_4_allKeys[-1].rt
                        debugging_press_enter_to_skip_4.duration = _debugging_press_enter_to_skip_4_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    plusBetween.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in plusBetween.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "plusBetween" ---
            for thisComponent in plusBetween.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for plusBetween
            plusBetween.tStop = globalClock.getTime(format='float')
            plusBetween.tStopRefresh = tThisFlipGlobal
            thisExp.addData('plusBetween.stopped', plusBetween.tStop)
            # check responses
            if debugging_press_enter_to_skip_4.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_4.keys = None
            setOne.addData('debugging_press_enter_to_skip_4.keys',debugging_press_enter_to_skip_4.keys)
            if debugging_press_enter_to_skip_4.keys != None:  # we had a response
                setOne.addData('debugging_press_enter_to_skip_4.rt', debugging_press_enter_to_skip_4.rt)
                setOne.addData('debugging_press_enter_to_skip_4.duration', debugging_press_enter_to_skip_4.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if plusBetween.maxDurationReached:
                routineTimer.addTime(-plusBetween.maxDuration)
            elif plusBetween.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 12.0 repeats of 'setOne'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "breakBetweenRepeats" ---
        # create an object to store info about Routine breakBetweenRepeats
        breakBetweenRepeats = data.Routine(
            name='breakBetweenRepeats',
            components=[five_seconds, maybe_a_beep, debugging_press_enter_to_skip_5],
        )
        breakBetweenRepeats.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        maybe_a_beep.setSound('A', secs=1.0, hamming=True)
        maybe_a_beep.setVolume(1.0, log=False)
        maybe_a_beep.seek(0)
        # create starting attributes for debugging_press_enter_to_skip_5
        debugging_press_enter_to_skip_5.keys = []
        debugging_press_enter_to_skip_5.rt = []
        _debugging_press_enter_to_skip_5_allKeys = []
        # store start times for breakBetweenRepeats
        breakBetweenRepeats.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        breakBetweenRepeats.tStart = globalClock.getTime(format='float')
        breakBetweenRepeats.status = STARTED
        thisExp.addData('breakBetweenRepeats.started', breakBetweenRepeats.tStart)
        breakBetweenRepeats.maxDuration = None
        # keep track of which components have finished
        breakBetweenRepeatsComponents = breakBetweenRepeats.components
        for thisComponent in breakBetweenRepeats.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "breakBetweenRepeats" ---
        # if trial has changed, end Routine now
        if isinstance(LearningSetOne, data.TrialHandler2) and thisLearningSetOne.thisN != LearningSetOne.thisTrial.thisN:
            continueRoutine = False
        breakBetweenRepeats.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *five_seconds* updates
            
            # if five_seconds is starting this frame...
            if five_seconds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                five_seconds.frameNStart = frameN  # exact frame index
                five_seconds.tStart = t  # local t and not account for scr refresh
                five_seconds.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(five_seconds, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'five_seconds.started')
                # update status
                five_seconds.status = STARTED
                five_seconds.setAutoDraw(True)
            
            # if five_seconds is active this frame...
            if five_seconds.status == STARTED:
                # update params
                pass
            
            # if five_seconds is stopping this frame...
            if five_seconds.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > five_seconds.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    five_seconds.tStop = t  # not accounting for scr refresh
                    five_seconds.tStopRefresh = tThisFlipGlobal  # on global time
                    five_seconds.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'five_seconds.stopped')
                    # update status
                    five_seconds.status = FINISHED
                    five_seconds.setAutoDraw(False)
            
            # *maybe_a_beep* updates
            
            # if maybe_a_beep is starting this frame...
            if maybe_a_beep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                maybe_a_beep.frameNStart = frameN  # exact frame index
                maybe_a_beep.tStart = t  # local t and not account for scr refresh
                maybe_a_beep.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('maybe_a_beep.started', tThisFlipGlobal)
                # update status
                maybe_a_beep.status = STARTED
                maybe_a_beep.play(when=win)  # sync with win flip
            
            # if maybe_a_beep is stopping this frame...
            if maybe_a_beep.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > maybe_a_beep.tStartRefresh + 1.0-frameTolerance or maybe_a_beep.isFinished:
                    # keep track of stop time/frame for later
                    maybe_a_beep.tStop = t  # not accounting for scr refresh
                    maybe_a_beep.tStopRefresh = tThisFlipGlobal  # on global time
                    maybe_a_beep.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'maybe_a_beep.stopped')
                    # update status
                    maybe_a_beep.status = FINISHED
                    maybe_a_beep.stop()
            
            # *debugging_press_enter_to_skip_5* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_5 is starting this frame...
            if debugging_press_enter_to_skip_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_5.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_5.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.started')
                # update status
                debugging_press_enter_to_skip_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if debugging_press_enter_to_skip_5 is stopping this frame...
            if debugging_press_enter_to_skip_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > debugging_press_enter_to_skip_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    debugging_press_enter_to_skip_5.tStop = t  # not accounting for scr refresh
                    debugging_press_enter_to_skip_5.tStopRefresh = tThisFlipGlobal  # on global time
                    debugging_press_enter_to_skip_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.stopped')
                    # update status
                    debugging_press_enter_to_skip_5.status = FINISHED
                    debugging_press_enter_to_skip_5.status = FINISHED
            if debugging_press_enter_to_skip_5.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_5.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_5_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_5_allKeys):
                    debugging_press_enter_to_skip_5.keys = _debugging_press_enter_to_skip_5_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_5.rt = _debugging_press_enter_to_skip_5_allKeys[-1].rt
                    debugging_press_enter_to_skip_5.duration = _debugging_press_enter_to_skip_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[maybe_a_beep]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                breakBetweenRepeats.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in breakBetweenRepeats.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "breakBetweenRepeats" ---
        for thisComponent in breakBetweenRepeats.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for breakBetweenRepeats
        breakBetweenRepeats.tStop = globalClock.getTime(format='float')
        breakBetweenRepeats.tStopRefresh = tThisFlipGlobal
        thisExp.addData('breakBetweenRepeats.stopped', breakBetweenRepeats.tStop)
        maybe_a_beep.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if debugging_press_enter_to_skip_5.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_5.keys = None
        LearningSetOne.addData('debugging_press_enter_to_skip_5.keys',debugging_press_enter_to_skip_5.keys)
        if debugging_press_enter_to_skip_5.keys != None:  # we had a response
            LearningSetOne.addData('debugging_press_enter_to_skip_5.rt', debugging_press_enter_to_skip_5.rt)
            LearningSetOne.addData('debugging_press_enter_to_skip_5.duration', debugging_press_enter_to_skip_5.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if breakBetweenRepeats.maxDurationReached:
            routineTimer.addTime(-breakBetweenRepeats.maxDuration)
        elif breakBetweenRepeats.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed numReps repeats of 'LearningSetOne'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "routine_30Seconds" ---
    # create an object to store info about Routine routine_30Seconds
    routine_30Seconds = data.Routine(
        name='routine_30Seconds',
        components=[thirtySeconds, debugging_press_enter_to_skip_6],
    )
    routine_30Seconds.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for debugging_press_enter_to_skip_6
    debugging_press_enter_to_skip_6.keys = []
    debugging_press_enter_to_skip_6.rt = []
    _debugging_press_enter_to_skip_6_allKeys = []
    # store start times for routine_30Seconds
    routine_30Seconds.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_30Seconds.tStart = globalClock.getTime(format='float')
    routine_30Seconds.status = STARTED
    thisExp.addData('routine_30Seconds.started', routine_30Seconds.tStart)
    routine_30Seconds.maxDuration = None
    # keep track of which components have finished
    routine_30SecondsComponents = routine_30Seconds.components
    for thisComponent in routine_30Seconds.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_30Seconds" ---
    routine_30Seconds.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thirtySeconds* updates
        
        # if thirtySeconds is starting this frame...
        if thirtySeconds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thirtySeconds.frameNStart = frameN  # exact frame index
            thirtySeconds.tStart = t  # local t and not account for scr refresh
            thirtySeconds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thirtySeconds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thirtySeconds.started')
            # update status
            thirtySeconds.status = STARTED
            thirtySeconds.setAutoDraw(True)
        
        # if thirtySeconds is active this frame...
        if thirtySeconds.status == STARTED:
            # update params
            pass
        
        # if thirtySeconds is stopping this frame...
        if thirtySeconds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > thirtySeconds.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                thirtySeconds.tStop = t  # not accounting for scr refresh
                thirtySeconds.tStopRefresh = tThisFlipGlobal  # on global time
                thirtySeconds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'thirtySeconds.stopped')
                # update status
                thirtySeconds.status = FINISHED
                thirtySeconds.setAutoDraw(False)
        
        # *debugging_press_enter_to_skip_6* updates
        waitOnFlip = False
        
        # if debugging_press_enter_to_skip_6 is starting this frame...
        if debugging_press_enter_to_skip_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debugging_press_enter_to_skip_6.frameNStart = frameN  # exact frame index
            debugging_press_enter_to_skip_6.tStart = t  # local t and not account for scr refresh
            debugging_press_enter_to_skip_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debugging_press_enter_to_skip_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_6.started')
            # update status
            debugging_press_enter_to_skip_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(debugging_press_enter_to_skip_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(debugging_press_enter_to_skip_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if debugging_press_enter_to_skip_6 is stopping this frame...
        if debugging_press_enter_to_skip_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > debugging_press_enter_to_skip_6.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                debugging_press_enter_to_skip_6.tStop = t  # not accounting for scr refresh
                debugging_press_enter_to_skip_6.tStopRefresh = tThisFlipGlobal  # on global time
                debugging_press_enter_to_skip_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_6.stopped')
                # update status
                debugging_press_enter_to_skip_6.status = FINISHED
                debugging_press_enter_to_skip_6.status = FINISHED
        if debugging_press_enter_to_skip_6.status == STARTED and not waitOnFlip:
            theseKeys = debugging_press_enter_to_skip_6.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _debugging_press_enter_to_skip_6_allKeys.extend(theseKeys)
            if len(_debugging_press_enter_to_skip_6_allKeys):
                debugging_press_enter_to_skip_6.keys = _debugging_press_enter_to_skip_6_allKeys[-1].name  # just the last key pressed
                debugging_press_enter_to_skip_6.rt = _debugging_press_enter_to_skip_6_allKeys[-1].rt
                debugging_press_enter_to_skip_6.duration = _debugging_press_enter_to_skip_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routine_30Seconds.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_30Seconds.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_30Seconds" ---
    for thisComponent in routine_30Seconds.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_30Seconds
    routine_30Seconds.tStop = globalClock.getTime(format='float')
    routine_30Seconds.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_30Seconds.stopped', routine_30Seconds.tStop)
    # check responses
    if debugging_press_enter_to_skip_6.keys in ['', [], None]:  # No response was made
        debugging_press_enter_to_skip_6.keys = None
    thisExp.addData('debugging_press_enter_to_skip_6.keys',debugging_press_enter_to_skip_6.keys)
    if debugging_press_enter_to_skip_6.keys != None:  # we had a response
        thisExp.addData('debugging_press_enter_to_skip_6.rt', debugging_press_enter_to_skip_6.rt)
        thisExp.addData('debugging_press_enter_to_skip_6.duration', debugging_press_enter_to_skip_6.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_30Seconds.maxDurationReached:
        routineTimer.addTime(-routine_30Seconds.maxDuration)
    elif routine_30Seconds.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "start_test" ---
    # create an object to store info about Routine start_test
    start_test = data.Routine(
        name='start_test',
        components=[textWelcome, key_resp_11],
    )
    start_test.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_11
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # store start times for start_test
    start_test.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    start_test.tStart = globalClock.getTime(format='float')
    start_test.status = STARTED
    thisExp.addData('start_test.started', start_test.tStart)
    start_test.maxDuration = None
    # keep track of which components have finished
    start_testComponents = start_test.components
    for thisComponent in start_test.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start_test" ---
    start_test.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        
        # if textWelcome is starting this frame...
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.started')
            # update status
            textWelcome.status = STARTED
            textWelcome.setAutoDraw(True)
        
        # if textWelcome is active this frame...
        if textWelcome.status == STARTED:
            # update params
            pass
        
        # *key_resp_11* updates
        waitOnFlip = False
        
        # if key_resp_11 is starting this frame...
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_11.started')
            # update status
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                key_resp_11.duration = _key_resp_11_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            start_test.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_test.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start_test" ---
    for thisComponent in start_test.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for start_test
    start_test.tStop = globalClock.getTime(format='float')
    start_test.tStopRefresh = tThisFlipGlobal
    thisExp.addData('start_test.stopped', start_test.tStop)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    thisExp.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        thisExp.addData('key_resp_11.rt', key_resp_11.rt)
        thisExp.addData('key_resp_11.duration', key_resp_11.duration)
    thisExp.nextEntry()
    # the Routine "start_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testSet1 = data.TrialHandler2(
        name='testSet1',
        nReps=12.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(testSet1)  # add the loop to the experiment
    thisTestSet1 = testSet1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestSet1.rgb)
    if thisTestSet1 != None:
        for paramName in thisTestSet1:
            globals()[paramName] = thisTestSet1[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTestSet1 in testSet1:
        currentLoop = testSet1
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTestSet1.rgb)
        if thisTestSet1 != None:
            for paramName in thisTestSet1:
                globals()[paramName] = thisTestSet1[paramName]
        
        # --- Prepare to start Routine "test1_NEW" ---
        # create an object to store info about Routine test1_NEW
        test1_NEW = data.Routine(
            name='test1_NEW',
            components=[textAmharic_5, textOptionA_5, textOptionB_5, textOptionC_5, textOptionD_5, textDiamond_3, key_resp_5, debugging_press_enter_to_skip_19],
        )
        test1_NEW.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeSymbol_5
        #incraments item counter by one
        curr_item += 1
        curr_item %= 11
        
        correct_word1 = word_list1[curr_item] #THIS IS THE RIGHT ANSWER   
        amharic1 = amharic_list1[curr_item]
        
        #preparing answer choices 
        lottery_list1 = []
        
        #add the right answer
        lottery_list1.append(correct_word1)
        
        #add 3 more non repeating answers
        copied_word1_list1 = []
        copied_word1_list1 = word_list1.copy() #copy word list
        copied_word1_list1.remove(correct_word1) #remove the right answer
        shuffle(copied_word1_list1) #shuffle up the copied list
        
        for x in range(0,3):    #add 3 from the shuffled list
            lottery_list1.append(copied_word1_list1[x])
        
        random.shuffle(lottery_list1)  #mix up the answer choices
        
        index_of_correct_answer = lottery_list1.index(correct_word1) #index of the correct word
        
        correctAns = index_to_button[index_of_correct_answer] #correct answer in key form
        textAmharic_5.setText(amharic1)
        textOptionA_5.setText(lottery_list1[0]
        
        )
        textOptionB_5.setText(lottery_list1[1])
        textOptionC_5.setText(lottery_list1[2])
        textOptionD_5.setText(lottery_list1[3])
        textDiamond_3.setText(f"     {lottery_list1[0]}\n   {lottery_list1[1]}   {lottery_list1[2]}\n     {lottery_list1[3]}")
        # create starting attributes for key_resp_5
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # create starting attributes for debugging_press_enter_to_skip_19
        debugging_press_enter_to_skip_19.keys = []
        debugging_press_enter_to_skip_19.rt = []
        _debugging_press_enter_to_skip_19_allKeys = []
        # store start times for test1_NEW
        test1_NEW.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        test1_NEW.tStart = globalClock.getTime(format='float')
        test1_NEW.status = STARTED
        thisExp.addData('test1_NEW.started', test1_NEW.tStart)
        test1_NEW.maxDuration = None
        # keep track of which components have finished
        test1_NEWComponents = test1_NEW.components
        for thisComponent in test1_NEW.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test1_NEW" ---
        # if trial has changed, end Routine now
        if isinstance(testSet1, data.TrialHandler2) and thisTestSet1.thisN != testSet1.thisTrial.thisN:
            continueRoutine = False
        test1_NEW.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textAmharic_5* updates
            
            # if textAmharic_5 is starting this frame...
            if textAmharic_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textAmharic_5.frameNStart = frameN  # exact frame index
                textAmharic_5.tStart = t  # local t and not account for scr refresh
                textAmharic_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textAmharic_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textAmharic_5.started')
                # update status
                textAmharic_5.status = STARTED
                textAmharic_5.setAutoDraw(True)
            
            # if textAmharic_5 is active this frame...
            if textAmharic_5.status == STARTED:
                # update params
                pass
            
            # *textOptionA_5* updates
            
            # if textOptionA_5 is starting this frame...
            if textOptionA_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionA_5.frameNStart = frameN  # exact frame index
                textOptionA_5.tStart = t  # local t and not account for scr refresh
                textOptionA_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionA_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionA_5.started')
                # update status
                textOptionA_5.status = STARTED
                textOptionA_5.setAutoDraw(True)
            
            # if textOptionA_5 is active this frame...
            if textOptionA_5.status == STARTED:
                # update params
                pass
            
            # if textOptionA_5 is stopping this frame...
            if textOptionA_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionA_5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionA_5.tStop = t  # not accounting for scr refresh
                    textOptionA_5.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionA_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionA_5.stopped')
                    # update status
                    textOptionA_5.status = FINISHED
                    textOptionA_5.setAutoDraw(False)
            
            # *textOptionB_5* updates
            
            # if textOptionB_5 is starting this frame...
            if textOptionB_5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionB_5.frameNStart = frameN  # exact frame index
                textOptionB_5.tStart = t  # local t and not account for scr refresh
                textOptionB_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionB_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionB_5.started')
                # update status
                textOptionB_5.status = STARTED
                textOptionB_5.setAutoDraw(True)
            
            # if textOptionB_5 is active this frame...
            if textOptionB_5.status == STARTED:
                # update params
                pass
            
            # if textOptionB_5 is stopping this frame...
            if textOptionB_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionB_5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionB_5.tStop = t  # not accounting for scr refresh
                    textOptionB_5.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionB_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionB_5.stopped')
                    # update status
                    textOptionB_5.status = FINISHED
                    textOptionB_5.setAutoDraw(False)
            
            # *textOptionC_5* updates
            
            # if textOptionC_5 is starting this frame...
            if textOptionC_5.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionC_5.frameNStart = frameN  # exact frame index
                textOptionC_5.tStart = t  # local t and not account for scr refresh
                textOptionC_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionC_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionC_5.started')
                # update status
                textOptionC_5.status = STARTED
                textOptionC_5.setAutoDraw(True)
            
            # if textOptionC_5 is active this frame...
            if textOptionC_5.status == STARTED:
                # update params
                pass
            
            # if textOptionC_5 is stopping this frame...
            if textOptionC_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionC_5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionC_5.tStop = t  # not accounting for scr refresh
                    textOptionC_5.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionC_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionC_5.stopped')
                    # update status
                    textOptionC_5.status = FINISHED
                    textOptionC_5.setAutoDraw(False)
            
            # *textOptionD_5* updates
            
            # if textOptionD_5 is starting this frame...
            if textOptionD_5.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionD_5.frameNStart = frameN  # exact frame index
                textOptionD_5.tStart = t  # local t and not account for scr refresh
                textOptionD_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionD_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionD_5.started')
                # update status
                textOptionD_5.status = STARTED
                textOptionD_5.setAutoDraw(True)
            
            # if textOptionD_5 is active this frame...
            if textOptionD_5.status == STARTED:
                # update params
                pass
            
            # if textOptionD_5 is stopping this frame...
            if textOptionD_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionD_5.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionD_5.tStop = t  # not accounting for scr refresh
                    textOptionD_5.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionD_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionD_5.stopped')
                    # update status
                    textOptionD_5.status = FINISHED
                    textOptionD_5.setAutoDraw(False)
            
            # *textDiamond_3* updates
            
            # if textDiamond_3 is starting this frame...
            if textDiamond_3.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                textDiamond_3.frameNStart = frameN  # exact frame index
                textDiamond_3.tStart = t  # local t and not account for scr refresh
                textDiamond_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textDiamond_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textDiamond_3.started')
                # update status
                textDiamond_3.status = STARTED
                textDiamond_3.setAutoDraw(True)
            
            # if textDiamond_3 is active this frame...
            if textDiamond_3.status == STARTED:
                # update params
                pass
            
            # *key_resp_5* updates
            waitOnFlip = False
            
            # if key_resp_5 is starting this frame...
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                # update status
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['right','up','left','down', 'space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_5.keys == str(correctAns)) or (key_resp_5.keys == correctAns):
                        key_resp_5.corr = 1
                    else:
                        key_resp_5.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *debugging_press_enter_to_skip_19* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_19 is starting this frame...
            if debugging_press_enter_to_skip_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_19.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_19.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_19, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_19.started')
                # update status
                debugging_press_enter_to_skip_19.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_19.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if debugging_press_enter_to_skip_19.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_19.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_19_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_19_allKeys):
                    debugging_press_enter_to_skip_19.keys = _debugging_press_enter_to_skip_19_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_19.rt = _debugging_press_enter_to_skip_19_allKeys[-1].rt
                    debugging_press_enter_to_skip_19.duration = _debugging_press_enter_to_skip_19_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                test1_NEW.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test1_NEW.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test1_NEW" ---
        for thisComponent in test1_NEW.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for test1_NEW
        test1_NEW.tStop = globalClock.getTime(format='float')
        test1_NEW.tStopRefresh = tThisFlipGlobal
        thisExp.addData('test1_NEW.stopped', test1_NEW.tStop)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
            # was no response the correct answer?!
            if str(correctAns).lower() == 'none':
               key_resp_5.corr = 1;  # correct non-response
            else:
               key_resp_5.corr = 0;  # failed to respond (incorrectly)
        # store data for testSet1 (TrialHandler)
        testSet1.addData('key_resp_5.keys',key_resp_5.keys)
        testSet1.addData('key_resp_5.corr', key_resp_5.corr)
        if key_resp_5.keys != None:  # we had a response
            testSet1.addData('key_resp_5.rt', key_resp_5.rt)
            testSet1.addData('key_resp_5.duration', key_resp_5.duration)
        # check responses
        if debugging_press_enter_to_skip_19.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_19.keys = None
        testSet1.addData('debugging_press_enter_to_skip_19.keys',debugging_press_enter_to_skip_19.keys)
        if debugging_press_enter_to_skip_19.keys != None:  # we had a response
            testSet1.addData('debugging_press_enter_to_skip_19.rt', debugging_press_enter_to_skip_19.rt)
            testSet1.addData('debugging_press_enter_to_skip_19.duration', debugging_press_enter_to_skip_19.duration)
        # the Routine "test1_NEW" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "checkForCorr" ---
        # create an object to store info about Routine checkForCorr
        checkForCorr = data.Routine(
            name='checkForCorr',
            components=[],
        )
        checkForCorr.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        if key_resp_5.corr == 1:
            checkmark_reps = 1
            xmark_reps = 0
        if key_resp_5.corr == 0:
            checkmark_reps = 0
            xmark_reps = 1
        # store start times for checkForCorr
        checkForCorr.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        checkForCorr.tStart = globalClock.getTime(format='float')
        checkForCorr.status = STARTED
        thisExp.addData('checkForCorr.started', checkForCorr.tStart)
        checkForCorr.maxDuration = None
        # keep track of which components have finished
        checkForCorrComponents = checkForCorr.components
        for thisComponent in checkForCorr.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "checkForCorr" ---
        # if trial has changed, end Routine now
        if isinstance(testSet1, data.TrialHandler2) and thisTestSet1.thisN != testSet1.thisTrial.thisN:
            continueRoutine = False
        checkForCorr.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                checkForCorr.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in checkForCorr.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "checkForCorr" ---
        for thisComponent in checkForCorr.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for checkForCorr
        checkForCorr.tStop = globalClock.getTime(format='float')
        checkForCorr.tStopRefresh = tThisFlipGlobal
        thisExp.addData('checkForCorr.stopped', checkForCorr.tStop)
        # the Routine "checkForCorr" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        checkloop = data.TrialHandler2(
            name='checkloop',
            nReps=checkmark_reps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(checkloop)  # add the loop to the experiment
        thisCheckloop = checkloop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisCheckloop.rgb)
        if thisCheckloop != None:
            for paramName in thisCheckloop:
                globals()[paramName] = thisCheckloop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisCheckloop in checkloop:
            currentLoop = checkloop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisCheckloop.rgb)
            if thisCheckloop != None:
                for paramName in thisCheckloop:
                    globals()[paramName] = thisCheckloop[paramName]
            
            # --- Prepare to start Routine "checkmark" ---
            # create an object to store info about Routine checkmark
            checkmark = data.Routine(
                name='checkmark',
                components=[textCheck, debugging_press_enter_to_skip_7],
            )
            checkmark.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textCheck.setText(markers[0])
            # create starting attributes for debugging_press_enter_to_skip_7
            debugging_press_enter_to_skip_7.keys = []
            debugging_press_enter_to_skip_7.rt = []
            _debugging_press_enter_to_skip_7_allKeys = []
            # store start times for checkmark
            checkmark.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            checkmark.tStart = globalClock.getTime(format='float')
            checkmark.status = STARTED
            thisExp.addData('checkmark.started', checkmark.tStart)
            checkmark.maxDuration = None
            # keep track of which components have finished
            checkmarkComponents = checkmark.components
            for thisComponent in checkmark.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "checkmark" ---
            # if trial has changed, end Routine now
            if isinstance(checkloop, data.TrialHandler2) and thisCheckloop.thisN != checkloop.thisTrial.thisN:
                continueRoutine = False
            checkmark.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textCheck* updates
                
                # if textCheck is starting this frame...
                if textCheck.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textCheck.frameNStart = frameN  # exact frame index
                    textCheck.tStart = t  # local t and not account for scr refresh
                    textCheck.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textCheck, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textCheck.started')
                    # update status
                    textCheck.status = STARTED
                    textCheck.setAutoDraw(True)
                
                # if textCheck is active this frame...
                if textCheck.status == STARTED:
                    # update params
                    pass
                
                # if textCheck is stopping this frame...
                if textCheck.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textCheck.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textCheck.tStop = t  # not accounting for scr refresh
                        textCheck.tStopRefresh = tThisFlipGlobal  # on global time
                        textCheck.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textCheck.stopped')
                        # update status
                        textCheck.status = FINISHED
                        textCheck.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_7* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_7 is starting this frame...
                if debugging_press_enter_to_skip_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_7.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_7.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_7.started')
                    # update status
                    debugging_press_enter_to_skip_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_7.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_7 is stopping this frame...
                if debugging_press_enter_to_skip_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_7.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_7.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_7.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_7.stopped')
                        # update status
                        debugging_press_enter_to_skip_7.status = FINISHED
                        debugging_press_enter_to_skip_7.status = FINISHED
                if debugging_press_enter_to_skip_7.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_7.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_7_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_7_allKeys):
                        debugging_press_enter_to_skip_7.keys = _debugging_press_enter_to_skip_7_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_7.rt = _debugging_press_enter_to_skip_7_allKeys[-1].rt
                        debugging_press_enter_to_skip_7.duration = _debugging_press_enter_to_skip_7_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    checkmark.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in checkmark.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "checkmark" ---
            for thisComponent in checkmark.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for checkmark
            checkmark.tStop = globalClock.getTime(format='float')
            checkmark.tStopRefresh = tThisFlipGlobal
            thisExp.addData('checkmark.stopped', checkmark.tStop)
            # check responses
            if debugging_press_enter_to_skip_7.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_7.keys = None
            checkloop.addData('debugging_press_enter_to_skip_7.keys',debugging_press_enter_to_skip_7.keys)
            if debugging_press_enter_to_skip_7.keys != None:  # we had a response
                checkloop.addData('debugging_press_enter_to_skip_7.rt', debugging_press_enter_to_skip_7.rt)
                checkloop.addData('debugging_press_enter_to_skip_7.duration', debugging_press_enter_to_skip_7.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if checkmark.maxDurationReached:
                routineTimer.addTime(-checkmark.maxDuration)
            elif checkmark.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed checkmark_reps repeats of 'checkloop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        xloop = data.TrialHandler2(
            name='xloop',
            nReps=xmark_reps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(xloop)  # add the loop to the experiment
        thisXloop = xloop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisXloop.rgb)
        if thisXloop != None:
            for paramName in thisXloop:
                globals()[paramName] = thisXloop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisXloop in xloop:
            currentLoop = xloop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisXloop.rgb)
            if thisXloop != None:
                for paramName in thisXloop:
                    globals()[paramName] = thisXloop[paramName]
            
            # --- Prepare to start Routine "xmark" ---
            # create an object to store info about Routine xmark
            xmark = data.Routine(
                name='xmark',
                components=[textXmark, debugging_press_enter_to_skip_26],
            )
            xmark.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textXmark.setText(markers[1])
            # create starting attributes for debugging_press_enter_to_skip_26
            debugging_press_enter_to_skip_26.keys = []
            debugging_press_enter_to_skip_26.rt = []
            _debugging_press_enter_to_skip_26_allKeys = []
            # store start times for xmark
            xmark.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            xmark.tStart = globalClock.getTime(format='float')
            xmark.status = STARTED
            thisExp.addData('xmark.started', xmark.tStart)
            xmark.maxDuration = None
            # keep track of which components have finished
            xmarkComponents = xmark.components
            for thisComponent in xmark.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "xmark" ---
            # if trial has changed, end Routine now
            if isinstance(xloop, data.TrialHandler2) and thisXloop.thisN != xloop.thisTrial.thisN:
                continueRoutine = False
            xmark.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textXmark* updates
                
                # if textXmark is starting this frame...
                if textXmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textXmark.frameNStart = frameN  # exact frame index
                    textXmark.tStart = t  # local t and not account for scr refresh
                    textXmark.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textXmark, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textXmark.started')
                    # update status
                    textXmark.status = STARTED
                    textXmark.setAutoDraw(True)
                
                # if textXmark is active this frame...
                if textXmark.status == STARTED:
                    # update params
                    pass
                
                # if textXmark is stopping this frame...
                if textXmark.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textXmark.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textXmark.tStop = t  # not accounting for scr refresh
                        textXmark.tStopRefresh = tThisFlipGlobal  # on global time
                        textXmark.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textXmark.stopped')
                        # update status
                        textXmark.status = FINISHED
                        textXmark.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_26* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_26 is starting this frame...
                if debugging_press_enter_to_skip_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_26.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_26.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_26, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_26.started')
                    # update status
                    debugging_press_enter_to_skip_26.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_26.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_26 is stopping this frame...
                if debugging_press_enter_to_skip_26.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_26.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_26.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_26.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_26.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_26.stopped')
                        # update status
                        debugging_press_enter_to_skip_26.status = FINISHED
                        debugging_press_enter_to_skip_26.status = FINISHED
                if debugging_press_enter_to_skip_26.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_26.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_26_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_26_allKeys):
                        debugging_press_enter_to_skip_26.keys = _debugging_press_enter_to_skip_26_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_26.rt = _debugging_press_enter_to_skip_26_allKeys[-1].rt
                        debugging_press_enter_to_skip_26.duration = _debugging_press_enter_to_skip_26_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    xmark.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in xmark.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "xmark" ---
            for thisComponent in xmark.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for xmark
            xmark.tStop = globalClock.getTime(format='float')
            xmark.tStopRefresh = tThisFlipGlobal
            thisExp.addData('xmark.stopped', xmark.tStop)
            # check responses
            if debugging_press_enter_to_skip_26.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_26.keys = None
            xloop.addData('debugging_press_enter_to_skip_26.keys',debugging_press_enter_to_skip_26.keys)
            if debugging_press_enter_to_skip_26.keys != None:  # we had a response
                xloop.addData('debugging_press_enter_to_skip_26.rt', debugging_press_enter_to_skip_26.rt)
                xloop.addData('debugging_press_enter_to_skip_26.duration', debugging_press_enter_to_skip_26.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if xmark.maxDurationReached:
                routineTimer.addTime(-xmark.maxDuration)
            elif xmark.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed xmark_reps repeats of 'xloop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "resetReps" ---
        # create an object to store info about Routine resetReps
        resetReps = data.Routine(
            name='resetReps',
            components=[],
        )
        resetReps.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for resetReps
        resetReps.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        resetReps.tStart = globalClock.getTime(format='float')
        resetReps.status = STARTED
        thisExp.addData('resetReps.started', resetReps.tStart)
        resetReps.maxDuration = None
        # keep track of which components have finished
        resetRepsComponents = resetReps.components
        for thisComponent in resetReps.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "resetReps" ---
        # if trial has changed, end Routine now
        if isinstance(testSet1, data.TrialHandler2) and thisTestSet1.thisN != testSet1.thisTrial.thisN:
            continueRoutine = False
        resetReps.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                resetReps.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in resetReps.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "resetReps" ---
        for thisComponent in resetReps.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for resetReps
        resetReps.tStop = globalClock.getTime(format='float')
        resetReps.tStopRefresh = tThisFlipGlobal
        thisExp.addData('resetReps.stopped', resetReps.tStop)
        # the Routine "resetReps" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        # create an object to store info about Routine blank500
        blank500 = data.Routine(
            name='blank500',
            components=[text_2, debugging_press_enter_to_skip_15],
        )
        blank500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_2.setText('')
        # create starting attributes for debugging_press_enter_to_skip_15
        debugging_press_enter_to_skip_15.keys = []
        debugging_press_enter_to_skip_15.rt = []
        _debugging_press_enter_to_skip_15_allKeys = []
        # store start times for blank500
        blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank500.tStart = globalClock.getTime(format='float')
        blank500.status = STARTED
        thisExp.addData('blank500.started', blank500.tStart)
        blank500.maxDuration = None
        # keep track of which components have finished
        blank500Components = blank500.components
        for thisComponent in blank500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        # if trial has changed, end Routine now
        if isinstance(testSet1, data.TrialHandler2) and thisTestSet1.thisN != testSet1.thisTrial.thisN:
            continueRoutine = False
        blank500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # *debugging_press_enter_to_skip_15* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_15 is starting this frame...
            if debugging_press_enter_to_skip_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_15.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_15.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_15.started')
                # update status
                debugging_press_enter_to_skip_15.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_15.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if debugging_press_enter_to_skip_15 is stopping this frame...
            if debugging_press_enter_to_skip_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > debugging_press_enter_to_skip_15.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    debugging_press_enter_to_skip_15.tStop = t  # not accounting for scr refresh
                    debugging_press_enter_to_skip_15.tStopRefresh = tThisFlipGlobal  # on global time
                    debugging_press_enter_to_skip_15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_15.stopped')
                    # update status
                    debugging_press_enter_to_skip_15.status = FINISHED
                    debugging_press_enter_to_skip_15.status = FINISHED
            if debugging_press_enter_to_skip_15.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_15.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_15_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_15_allKeys):
                    debugging_press_enter_to_skip_15.keys = _debugging_press_enter_to_skip_15_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_15.rt = _debugging_press_enter_to_skip_15_allKeys[-1].rt
                    debugging_press_enter_to_skip_15.duration = _debugging_press_enter_to_skip_15_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank500
        blank500.tStop = globalClock.getTime(format='float')
        blank500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank500.stopped', blank500.tStop)
        # check responses
        if debugging_press_enter_to_skip_15.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_15.keys = None
        testSet1.addData('debugging_press_enter_to_skip_15.keys',debugging_press_enter_to_skip_15.keys)
        if debugging_press_enter_to_skip_15.keys != None:  # we had a response
            testSet1.addData('debugging_press_enter_to_skip_15.rt', debugging_press_enter_to_skip_15.rt)
            testSet1.addData('debugging_press_enter_to_skip_15.duration', debugging_press_enter_to_skip_15.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank500.maxDurationReached:
            routineTimer.addTime(-blank500.maxDuration)
        elif blank500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed 12.0 repeats of 'testSet1'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "breakBetweenSets" ---
    # create an object to store info about Routine breakBetweenSets
    breakBetweenSets = data.Routine(
        name='breakBetweenSets',
        components=[cross, debugging_press_enter_to_skip_8],
    )
    breakBetweenSets.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for debugging_press_enter_to_skip_8
    debugging_press_enter_to_skip_8.keys = []
    debugging_press_enter_to_skip_8.rt = []
    _debugging_press_enter_to_skip_8_allKeys = []
    # store start times for breakBetweenSets
    breakBetweenSets.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    breakBetweenSets.tStart = globalClock.getTime(format='float')
    breakBetweenSets.status = STARTED
    thisExp.addData('breakBetweenSets.started', breakBetweenSets.tStart)
    breakBetweenSets.maxDuration = None
    # keep track of which components have finished
    breakBetweenSetsComponents = breakBetweenSets.components
    for thisComponent in breakBetweenSets.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "breakBetweenSets" ---
    breakBetweenSets.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.tStopRefresh = tThisFlipGlobal  # on global time
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # *debugging_press_enter_to_skip_8* updates
        waitOnFlip = False
        
        # if debugging_press_enter_to_skip_8 is starting this frame...
        if debugging_press_enter_to_skip_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debugging_press_enter_to_skip_8.frameNStart = frameN  # exact frame index
            debugging_press_enter_to_skip_8.tStart = t  # local t and not account for scr refresh
            debugging_press_enter_to_skip_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debugging_press_enter_to_skip_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_8.started')
            # update status
            debugging_press_enter_to_skip_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(debugging_press_enter_to_skip_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(debugging_press_enter_to_skip_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if debugging_press_enter_to_skip_8 is stopping this frame...
        if debugging_press_enter_to_skip_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > debugging_press_enter_to_skip_8.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                debugging_press_enter_to_skip_8.tStop = t  # not accounting for scr refresh
                debugging_press_enter_to_skip_8.tStopRefresh = tThisFlipGlobal  # on global time
                debugging_press_enter_to_skip_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_8.stopped')
                # update status
                debugging_press_enter_to_skip_8.status = FINISHED
                debugging_press_enter_to_skip_8.status = FINISHED
        if debugging_press_enter_to_skip_8.status == STARTED and not waitOnFlip:
            theseKeys = debugging_press_enter_to_skip_8.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _debugging_press_enter_to_skip_8_allKeys.extend(theseKeys)
            if len(_debugging_press_enter_to_skip_8_allKeys):
                debugging_press_enter_to_skip_8.keys = _debugging_press_enter_to_skip_8_allKeys[-1].name  # just the last key pressed
                debugging_press_enter_to_skip_8.rt = _debugging_press_enter_to_skip_8_allKeys[-1].rt
                debugging_press_enter_to_skip_8.duration = _debugging_press_enter_to_skip_8_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            breakBetweenSets.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breakBetweenSets.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "breakBetweenSets" ---
    for thisComponent in breakBetweenSets.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for breakBetweenSets
    breakBetweenSets.tStop = globalClock.getTime(format='float')
    breakBetweenSets.tStopRefresh = tThisFlipGlobal
    thisExp.addData('breakBetweenSets.stopped', breakBetweenSets.tStop)
    # check responses
    if debugging_press_enter_to_skip_8.keys in ['', [], None]:  # No response was made
        debugging_press_enter_to_skip_8.keys = None
    thisExp.addData('debugging_press_enter_to_skip_8.keys',debugging_press_enter_to_skip_8.keys)
    if debugging_press_enter_to_skip_8.keys != None:  # we had a response
        thisExp.addData('debugging_press_enter_to_skip_8.rt', debugging_press_enter_to_skip_8.rt)
        thisExp.addData('debugging_press_enter_to_skip_8.duration', debugging_press_enter_to_skip_8.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if breakBetweenSets.maxDurationReached:
        routineTimer.addTime(-breakBetweenSets.maxDuration)
    elif breakBetweenSets.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    LearningSetTwo = data.TrialHandler2(
        name='LearningSetTwo',
        nReps=numReps, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(LearningSetTwo)  # add the loop to the experiment
    thisLearningSetTwo = LearningSetTwo.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLearningSetTwo.rgb)
    if thisLearningSetTwo != None:
        for paramName in thisLearningSetTwo:
            globals()[paramName] = thisLearningSetTwo[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLearningSetTwo in LearningSetTwo:
        currentLoop = LearningSetTwo
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLearningSetTwo.rgb)
        if thisLearningSetTwo != None:
            for paramName in thisLearningSetTwo:
                globals()[paramName] = thisLearningSetTwo[paramName]
        
        # --- Prepare to start Routine "randomize_set" ---
        # create an object to store info about Routine randomize_set
        randomize_set = data.Routine(
            name='randomize_set',
            components=[],
        )
        randomize_set.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from randomize_learning_set
        keys = list(range(12))
        random.shuffle(keys)
        print("learning set order: " + str(keys))
        
        practice_keys = list(range(6))
        random.shuffle(practice_keys)
        print("learning set order: " + str(keys))
        
        practice_keys2 = list(range(6,12))
        random.shuffle(practice_keys2)
        print("learning set order: " + str(keys))
        # store start times for randomize_set
        randomize_set.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        randomize_set.tStart = globalClock.getTime(format='float')
        randomize_set.status = STARTED
        thisExp.addData('randomize_set.started', randomize_set.tStart)
        randomize_set.maxDuration = None
        # keep track of which components have finished
        randomize_setComponents = randomize_set.components
        for thisComponent in randomize_set.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "randomize_set" ---
        # if trial has changed, end Routine now
        if isinstance(LearningSetTwo, data.TrialHandler2) and thisLearningSetTwo.thisN != LearningSetTwo.thisTrial.thisN:
            continueRoutine = False
        randomize_set.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                randomize_set.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in randomize_set.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "randomize_set" ---
        for thisComponent in randomize_set.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for randomize_set
        randomize_set.tStop = globalClock.getTime(format='float')
        randomize_set.tStopRefresh = tThisFlipGlobal
        thisExp.addData('randomize_set.stopped', randomize_set.tStop)
        # the Routine "randomize_set" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        setTwo = data.TrialHandler2(
            name='setTwo',
            nReps=12.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(setTwo)  # add the loop to the experiment
        thisSetTwo = setTwo.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSetTwo.rgb)
        if thisSetTwo != None:
            for paramName in thisSetTwo:
                globals()[paramName] = thisSetTwo[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisSetTwo in setTwo:
            currentLoop = setTwo
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisSetTwo.rgb)
            if thisSetTwo != None:
                for paramName in thisSetTwo:
                    globals()[paramName] = thisSetTwo[paramName]
            
            # --- Prepare to start Routine "Increment" ---
            # create an object to store info about Routine Increment
            Increment = data.Routine(
                name='Increment',
                components=[],
            )
            Increment.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from increment_index
            learning_index += 1
            learning_index %= len(keys)
            
            practice_index += 1
            practice_index %= len(practice_keys)
            # store start times for Increment
            Increment.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Increment.tStart = globalClock.getTime(format='float')
            Increment.status = STARTED
            thisExp.addData('Increment.started', Increment.tStart)
            Increment.maxDuration = None
            # keep track of which components have finished
            IncrementComponents = Increment.components
            for thisComponent in Increment.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Increment" ---
            # if trial has changed, end Routine now
            if isinstance(setTwo, data.TrialHandler2) and thisSetTwo.thisN != setTwo.thisTrial.thisN:
                continueRoutine = False
            Increment.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Increment.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Increment.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Increment" ---
            for thisComponent in Increment.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Increment
            Increment.tStop = globalClock.getTime(format='float')
            Increment.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Increment.stopped', Increment.tStop)
            # the Routine "Increment" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            nreps_A2 = data.TrialHandler2(
                name='nreps_A2',
                nReps=nreps_A, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(nreps_A2)  # add the loop to the experiment
            thisNreps_A2 = nreps_A2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisNreps_A2.rgb)
            if thisNreps_A2 != None:
                for paramName in thisNreps_A2:
                    globals()[paramName] = thisNreps_A2[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisNreps_A2 in nreps_A2:
                currentLoop = nreps_A2
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisNreps_A2.rgb)
                if thisNreps_A2 != None:
                    for paramName in thisNreps_A2:
                        globals()[paramName] = thisNreps_A2[paramName]
                
                # --- Prepare to start Routine "amharic2_A" ---
                # create an object to store info about Routine amharic2_A
                amharic2_A = data.Routine(
                    name='amharic2_A',
                    components=[amharics2, words2, debugging_press_enter_to_skip_9],
                )
                amharic2_A.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                amharics2.setText(amharic_word_list2[keys[learning_index]][0])
                words2.setText(amharic_word_list2[keys[learning_index]][1])
                # Run 'Begin Routine' code from amharic_word_code_2
                print("Index: " + str(keys[learning_index]) + 
                      "\n Character: " + str(amharic_word_list2[keys[learning_index]][0]) + 
                      "\n Meaning: " + str(amharic_word_list2[keys[learning_index]][1]) + 
                      "\n Image Path: " + str(amharic_word_list2[keys[learning_index]][2]))
                # create starting attributes for debugging_press_enter_to_skip_9
                debugging_press_enter_to_skip_9.keys = []
                debugging_press_enter_to_skip_9.rt = []
                _debugging_press_enter_to_skip_9_allKeys = []
                # store start times for amharic2_A
                amharic2_A.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                amharic2_A.tStart = globalClock.getTime(format='float')
                amharic2_A.status = STARTED
                thisExp.addData('amharic2_A.started', amharic2_A.tStart)
                amharic2_A.maxDuration = None
                # keep track of which components have finished
                amharic2_AComponents = amharic2_A.components
                for thisComponent in amharic2_A.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "amharic2_A" ---
                # if trial has changed, end Routine now
                if isinstance(nreps_A2, data.TrialHandler2) and thisNreps_A2.thisN != nreps_A2.thisTrial.thisN:
                    continueRoutine = False
                amharic2_A.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *amharics2* updates
                    
                    # if amharics2 is starting this frame...
                    if amharics2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        amharics2.frameNStart = frameN  # exact frame index
                        amharics2.tStart = t  # local t and not account for scr refresh
                        amharics2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(amharics2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'amharics2.started')
                        # update status
                        amharics2.status = STARTED
                        amharics2.setAutoDraw(True)
                    
                    # if amharics2 is active this frame...
                    if amharics2.status == STARTED:
                        # update params
                        pass
                    
                    # if amharics2 is stopping this frame...
                    if amharics2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > amharics2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            amharics2.tStop = t  # not accounting for scr refresh
                            amharics2.tStopRefresh = tThisFlipGlobal  # on global time
                            amharics2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'amharics2.stopped')
                            # update status
                            amharics2.status = FINISHED
                            amharics2.setAutoDraw(False)
                    
                    # *words2* updates
                    
                    # if words2 is starting this frame...
                    if words2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        words2.frameNStart = frameN  # exact frame index
                        words2.tStart = t  # local t and not account for scr refresh
                        words2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(words2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'words2.started')
                        # update status
                        words2.status = STARTED
                        words2.setAutoDraw(True)
                    
                    # if words2 is active this frame...
                    if words2.status == STARTED:
                        # update params
                        pass
                    
                    # if words2 is stopping this frame...
                    if words2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > words2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            words2.tStop = t  # not accounting for scr refresh
                            words2.tStopRefresh = tThisFlipGlobal  # on global time
                            words2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'words2.stopped')
                            # update status
                            words2.status = FINISHED
                            words2.setAutoDraw(False)
                    
                    # *debugging_press_enter_to_skip_9* updates
                    waitOnFlip = False
                    
                    # if debugging_press_enter_to_skip_9 is starting this frame...
                    if debugging_press_enter_to_skip_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        debugging_press_enter_to_skip_9.frameNStart = frameN  # exact frame index
                        debugging_press_enter_to_skip_9.tStart = t  # local t and not account for scr refresh
                        debugging_press_enter_to_skip_9.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(debugging_press_enter_to_skip_9, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_9.started')
                        # update status
                        debugging_press_enter_to_skip_9.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(debugging_press_enter_to_skip_9.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(debugging_press_enter_to_skip_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if debugging_press_enter_to_skip_9 is stopping this frame...
                    if debugging_press_enter_to_skip_9.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > debugging_press_enter_to_skip_9.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            debugging_press_enter_to_skip_9.tStop = t  # not accounting for scr refresh
                            debugging_press_enter_to_skip_9.tStopRefresh = tThisFlipGlobal  # on global time
                            debugging_press_enter_to_skip_9.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_9.stopped')
                            # update status
                            debugging_press_enter_to_skip_9.status = FINISHED
                            debugging_press_enter_to_skip_9.status = FINISHED
                    if debugging_press_enter_to_skip_9.status == STARTED and not waitOnFlip:
                        theseKeys = debugging_press_enter_to_skip_9.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                        _debugging_press_enter_to_skip_9_allKeys.extend(theseKeys)
                        if len(_debugging_press_enter_to_skip_9_allKeys):
                            debugging_press_enter_to_skip_9.keys = _debugging_press_enter_to_skip_9_allKeys[-1].name  # just the last key pressed
                            debugging_press_enter_to_skip_9.rt = _debugging_press_enter_to_skip_9_allKeys[-1].rt
                            debugging_press_enter_to_skip_9.duration = _debugging_press_enter_to_skip_9_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        amharic2_A.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in amharic2_A.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "amharic2_A" ---
                for thisComponent in amharic2_A.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for amharic2_A
                amharic2_A.tStop = globalClock.getTime(format='float')
                amharic2_A.tStopRefresh = tThisFlipGlobal
                thisExp.addData('amharic2_A.stopped', amharic2_A.tStop)
                # check responses
                if debugging_press_enter_to_skip_9.keys in ['', [], None]:  # No response was made
                    debugging_press_enter_to_skip_9.keys = None
                nreps_A2.addData('debugging_press_enter_to_skip_9.keys',debugging_press_enter_to_skip_9.keys)
                if debugging_press_enter_to_skip_9.keys != None:  # we had a response
                    nreps_A2.addData('debugging_press_enter_to_skip_9.rt', debugging_press_enter_to_skip_9.rt)
                    nreps_A2.addData('debugging_press_enter_to_skip_9.duration', debugging_press_enter_to_skip_9.duration)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if amharic2_A.maxDurationReached:
                    routineTimer.addTime(-amharic2_A.maxDuration)
                elif amharic2_A.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
            # completed nreps_A repeats of 'nreps_A2'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # set up handler to look after randomisation of conditions etc
            nreps_B2 = data.TrialHandler2(
                name='nreps_B2',
                nReps=nreps_B, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(nreps_B2)  # add the loop to the experiment
            thisNreps_B2 = nreps_B2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisNreps_B2.rgb)
            if thisNreps_B2 != None:
                for paramName in thisNreps_B2:
                    globals()[paramName] = thisNreps_B2[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisNreps_B2 in nreps_B2:
                currentLoop = nreps_B2
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisNreps_B2.rgb)
                if thisNreps_B2 != None:
                    for paramName in thisNreps_B2:
                        globals()[paramName] = thisNreps_B2[paramName]
                
                # --- Prepare to start Routine "amharic2_B" ---
                # create an object to store info about Routine amharic2_B
                amharic2_B = data.Routine(
                    name='amharic2_B',
                    components=[amharics2_2, words2_image_2, debugging_press_enter_to_skip_10],
                )
                amharic2_B.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                amharics2_2.setText(amharic_word_list2[keys[learning_index]][0])
                words2_image_2.setImage(amharic_word_list2[keys[learning_index]][2])
                # Run 'Begin Routine' code from amharic_word_code
                print("Index: " + str(keys[learning_index]) + 
                      "\n Character: " + str(amharic_word_list2[keys[learning_index]][0]) + 
                      "\n Meaning: " + str(amharic_word_list2[keys[learning_index]][1]) + 
                      "\n Image Path: " + str(amharic_word_list2[keys[learning_index]][2]))
                # create starting attributes for debugging_press_enter_to_skip_10
                debugging_press_enter_to_skip_10.keys = []
                debugging_press_enter_to_skip_10.rt = []
                _debugging_press_enter_to_skip_10_allKeys = []
                # store start times for amharic2_B
                amharic2_B.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                amharic2_B.tStart = globalClock.getTime(format='float')
                amharic2_B.status = STARTED
                thisExp.addData('amharic2_B.started', amharic2_B.tStart)
                amharic2_B.maxDuration = None
                # keep track of which components have finished
                amharic2_BComponents = amharic2_B.components
                for thisComponent in amharic2_B.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "amharic2_B" ---
                # if trial has changed, end Routine now
                if isinstance(nreps_B2, data.TrialHandler2) and thisNreps_B2.thisN != nreps_B2.thisTrial.thisN:
                    continueRoutine = False
                amharic2_B.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *amharics2_2* updates
                    
                    # if amharics2_2 is starting this frame...
                    if amharics2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        amharics2_2.frameNStart = frameN  # exact frame index
                        amharics2_2.tStart = t  # local t and not account for scr refresh
                        amharics2_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(amharics2_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'amharics2_2.started')
                        # update status
                        amharics2_2.status = STARTED
                        amharics2_2.setAutoDraw(True)
                    
                    # if amharics2_2 is active this frame...
                    if amharics2_2.status == STARTED:
                        # update params
                        pass
                    
                    # if amharics2_2 is stopping this frame...
                    if amharics2_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > amharics2_2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            amharics2_2.tStop = t  # not accounting for scr refresh
                            amharics2_2.tStopRefresh = tThisFlipGlobal  # on global time
                            amharics2_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'amharics2_2.stopped')
                            # update status
                            amharics2_2.status = FINISHED
                            amharics2_2.setAutoDraw(False)
                    
                    # *words2_image_2* updates
                    
                    # if words2_image_2 is starting this frame...
                    if words2_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        words2_image_2.frameNStart = frameN  # exact frame index
                        words2_image_2.tStart = t  # local t and not account for scr refresh
                        words2_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(words2_image_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'words2_image_2.started')
                        # update status
                        words2_image_2.status = STARTED
                        words2_image_2.setAutoDraw(True)
                    
                    # if words2_image_2 is active this frame...
                    if words2_image_2.status == STARTED:
                        # update params
                        pass
                    
                    # if words2_image_2 is stopping this frame...
                    if words2_image_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > words2_image_2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            words2_image_2.tStop = t  # not accounting for scr refresh
                            words2_image_2.tStopRefresh = tThisFlipGlobal  # on global time
                            words2_image_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'words2_image_2.stopped')
                            # update status
                            words2_image_2.status = FINISHED
                            words2_image_2.setAutoDraw(False)
                    
                    # *debugging_press_enter_to_skip_10* updates
                    waitOnFlip = False
                    
                    # if debugging_press_enter_to_skip_10 is starting this frame...
                    if debugging_press_enter_to_skip_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        debugging_press_enter_to_skip_10.frameNStart = frameN  # exact frame index
                        debugging_press_enter_to_skip_10.tStart = t  # local t and not account for scr refresh
                        debugging_press_enter_to_skip_10.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(debugging_press_enter_to_skip_10, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_10.started')
                        # update status
                        debugging_press_enter_to_skip_10.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(debugging_press_enter_to_skip_10.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(debugging_press_enter_to_skip_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if debugging_press_enter_to_skip_10 is stopping this frame...
                    if debugging_press_enter_to_skip_10.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > debugging_press_enter_to_skip_10.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            debugging_press_enter_to_skip_10.tStop = t  # not accounting for scr refresh
                            debugging_press_enter_to_skip_10.tStopRefresh = tThisFlipGlobal  # on global time
                            debugging_press_enter_to_skip_10.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_10.stopped')
                            # update status
                            debugging_press_enter_to_skip_10.status = FINISHED
                            debugging_press_enter_to_skip_10.status = FINISHED
                    if debugging_press_enter_to_skip_10.status == STARTED and not waitOnFlip:
                        theseKeys = debugging_press_enter_to_skip_10.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                        _debugging_press_enter_to_skip_10_allKeys.extend(theseKeys)
                        if len(_debugging_press_enter_to_skip_10_allKeys):
                            debugging_press_enter_to_skip_10.keys = _debugging_press_enter_to_skip_10_allKeys[-1].name  # just the last key pressed
                            debugging_press_enter_to_skip_10.rt = _debugging_press_enter_to_skip_10_allKeys[-1].rt
                            debugging_press_enter_to_skip_10.duration = _debugging_press_enter_to_skip_10_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        amharic2_B.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in amharic2_B.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "amharic2_B" ---
                for thisComponent in amharic2_B.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for amharic2_B
                amharic2_B.tStop = globalClock.getTime(format='float')
                amharic2_B.tStopRefresh = tThisFlipGlobal
                thisExp.addData('amharic2_B.stopped', amharic2_B.tStop)
                # check responses
                if debugging_press_enter_to_skip_10.keys in ['', [], None]:  # No response was made
                    debugging_press_enter_to_skip_10.keys = None
                nreps_B2.addData('debugging_press_enter_to_skip_10.keys',debugging_press_enter_to_skip_10.keys)
                if debugging_press_enter_to_skip_10.keys != None:  # we had a response
                    nreps_B2.addData('debugging_press_enter_to_skip_10.rt', debugging_press_enter_to_skip_10.rt)
                    nreps_B2.addData('debugging_press_enter_to_skip_10.duration', debugging_press_enter_to_skip_10.duration)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if amharic2_B.maxDurationReached:
                    routineTimer.addTime(-amharic2_B.maxDuration)
                elif amharic2_B.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
            # completed nreps_B repeats of 'nreps_B2'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # --- Prepare to start Routine "plusBetween" ---
            # create an object to store info about Routine plusBetween
            plusBetween = data.Routine(
                name='plusBetween',
                components=[plus, debugging_press_enter_to_skip_4],
            )
            plusBetween.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            plus.setText('+')
            # create starting attributes for debugging_press_enter_to_skip_4
            debugging_press_enter_to_skip_4.keys = []
            debugging_press_enter_to_skip_4.rt = []
            _debugging_press_enter_to_skip_4_allKeys = []
            # store start times for plusBetween
            plusBetween.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            plusBetween.tStart = globalClock.getTime(format='float')
            plusBetween.status = STARTED
            thisExp.addData('plusBetween.started', plusBetween.tStart)
            plusBetween.maxDuration = None
            # keep track of which components have finished
            plusBetweenComponents = plusBetween.components
            for thisComponent in plusBetween.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "plusBetween" ---
            # if trial has changed, end Routine now
            if isinstance(setTwo, data.TrialHandler2) and thisSetTwo.thisN != setTwo.thisTrial.thisN:
                continueRoutine = False
            plusBetween.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *plus* updates
                
                # if plus is starting this frame...
                if plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    plus.frameNStart = frameN  # exact frame index
                    plus.tStart = t  # local t and not account for scr refresh
                    plus.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(plus, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'plus.started')
                    # update status
                    plus.status = STARTED
                    plus.setAutoDraw(True)
                
                # if plus is active this frame...
                if plus.status == STARTED:
                    # update params
                    pass
                
                # if plus is stopping this frame...
                if plus.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > plus.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        plus.tStop = t  # not accounting for scr refresh
                        plus.tStopRefresh = tThisFlipGlobal  # on global time
                        plus.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'plus.stopped')
                        # update status
                        plus.status = FINISHED
                        plus.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_4* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_4 is starting this frame...
                if debugging_press_enter_to_skip_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_4.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_4.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.started')
                    # update status
                    debugging_press_enter_to_skip_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_4 is stopping this frame...
                if debugging_press_enter_to_skip_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_4.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_4.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_4.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.stopped')
                        # update status
                        debugging_press_enter_to_skip_4.status = FINISHED
                        debugging_press_enter_to_skip_4.status = FINISHED
                if debugging_press_enter_to_skip_4.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_4.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_4_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_4_allKeys):
                        debugging_press_enter_to_skip_4.keys = _debugging_press_enter_to_skip_4_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_4.rt = _debugging_press_enter_to_skip_4_allKeys[-1].rt
                        debugging_press_enter_to_skip_4.duration = _debugging_press_enter_to_skip_4_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    plusBetween.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in plusBetween.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "plusBetween" ---
            for thisComponent in plusBetween.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for plusBetween
            plusBetween.tStop = globalClock.getTime(format='float')
            plusBetween.tStopRefresh = tThisFlipGlobal
            thisExp.addData('plusBetween.stopped', plusBetween.tStop)
            # check responses
            if debugging_press_enter_to_skip_4.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_4.keys = None
            setTwo.addData('debugging_press_enter_to_skip_4.keys',debugging_press_enter_to_skip_4.keys)
            if debugging_press_enter_to_skip_4.keys != None:  # we had a response
                setTwo.addData('debugging_press_enter_to_skip_4.rt', debugging_press_enter_to_skip_4.rt)
                setTwo.addData('debugging_press_enter_to_skip_4.duration', debugging_press_enter_to_skip_4.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if plusBetween.maxDurationReached:
                routineTimer.addTime(-plusBetween.maxDuration)
            elif plusBetween.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 12.0 repeats of 'setTwo'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "breakBetweenRepeats" ---
        # create an object to store info about Routine breakBetweenRepeats
        breakBetweenRepeats = data.Routine(
            name='breakBetweenRepeats',
            components=[five_seconds, maybe_a_beep, debugging_press_enter_to_skip_5],
        )
        breakBetweenRepeats.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        maybe_a_beep.setSound('A', secs=1.0, hamming=True)
        maybe_a_beep.setVolume(1.0, log=False)
        maybe_a_beep.seek(0)
        # create starting attributes for debugging_press_enter_to_skip_5
        debugging_press_enter_to_skip_5.keys = []
        debugging_press_enter_to_skip_5.rt = []
        _debugging_press_enter_to_skip_5_allKeys = []
        # store start times for breakBetweenRepeats
        breakBetweenRepeats.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        breakBetweenRepeats.tStart = globalClock.getTime(format='float')
        breakBetweenRepeats.status = STARTED
        thisExp.addData('breakBetweenRepeats.started', breakBetweenRepeats.tStart)
        breakBetweenRepeats.maxDuration = None
        # keep track of which components have finished
        breakBetweenRepeatsComponents = breakBetweenRepeats.components
        for thisComponent in breakBetweenRepeats.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "breakBetweenRepeats" ---
        # if trial has changed, end Routine now
        if isinstance(LearningSetTwo, data.TrialHandler2) and thisLearningSetTwo.thisN != LearningSetTwo.thisTrial.thisN:
            continueRoutine = False
        breakBetweenRepeats.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *five_seconds* updates
            
            # if five_seconds is starting this frame...
            if five_seconds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                five_seconds.frameNStart = frameN  # exact frame index
                five_seconds.tStart = t  # local t and not account for scr refresh
                five_seconds.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(five_seconds, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'five_seconds.started')
                # update status
                five_seconds.status = STARTED
                five_seconds.setAutoDraw(True)
            
            # if five_seconds is active this frame...
            if five_seconds.status == STARTED:
                # update params
                pass
            
            # if five_seconds is stopping this frame...
            if five_seconds.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > five_seconds.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    five_seconds.tStop = t  # not accounting for scr refresh
                    five_seconds.tStopRefresh = tThisFlipGlobal  # on global time
                    five_seconds.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'five_seconds.stopped')
                    # update status
                    five_seconds.status = FINISHED
                    five_seconds.setAutoDraw(False)
            
            # *maybe_a_beep* updates
            
            # if maybe_a_beep is starting this frame...
            if maybe_a_beep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                maybe_a_beep.frameNStart = frameN  # exact frame index
                maybe_a_beep.tStart = t  # local t and not account for scr refresh
                maybe_a_beep.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('maybe_a_beep.started', tThisFlipGlobal)
                # update status
                maybe_a_beep.status = STARTED
                maybe_a_beep.play(when=win)  # sync with win flip
            
            # if maybe_a_beep is stopping this frame...
            if maybe_a_beep.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > maybe_a_beep.tStartRefresh + 1.0-frameTolerance or maybe_a_beep.isFinished:
                    # keep track of stop time/frame for later
                    maybe_a_beep.tStop = t  # not accounting for scr refresh
                    maybe_a_beep.tStopRefresh = tThisFlipGlobal  # on global time
                    maybe_a_beep.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'maybe_a_beep.stopped')
                    # update status
                    maybe_a_beep.status = FINISHED
                    maybe_a_beep.stop()
            
            # *debugging_press_enter_to_skip_5* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_5 is starting this frame...
            if debugging_press_enter_to_skip_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_5.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_5.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.started')
                # update status
                debugging_press_enter_to_skip_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if debugging_press_enter_to_skip_5 is stopping this frame...
            if debugging_press_enter_to_skip_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > debugging_press_enter_to_skip_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    debugging_press_enter_to_skip_5.tStop = t  # not accounting for scr refresh
                    debugging_press_enter_to_skip_5.tStopRefresh = tThisFlipGlobal  # on global time
                    debugging_press_enter_to_skip_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.stopped')
                    # update status
                    debugging_press_enter_to_skip_5.status = FINISHED
                    debugging_press_enter_to_skip_5.status = FINISHED
            if debugging_press_enter_to_skip_5.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_5.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_5_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_5_allKeys):
                    debugging_press_enter_to_skip_5.keys = _debugging_press_enter_to_skip_5_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_5.rt = _debugging_press_enter_to_skip_5_allKeys[-1].rt
                    debugging_press_enter_to_skip_5.duration = _debugging_press_enter_to_skip_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[maybe_a_beep]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                breakBetweenRepeats.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in breakBetweenRepeats.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "breakBetweenRepeats" ---
        for thisComponent in breakBetweenRepeats.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for breakBetweenRepeats
        breakBetweenRepeats.tStop = globalClock.getTime(format='float')
        breakBetweenRepeats.tStopRefresh = tThisFlipGlobal
        thisExp.addData('breakBetweenRepeats.stopped', breakBetweenRepeats.tStop)
        maybe_a_beep.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if debugging_press_enter_to_skip_5.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_5.keys = None
        LearningSetTwo.addData('debugging_press_enter_to_skip_5.keys',debugging_press_enter_to_skip_5.keys)
        if debugging_press_enter_to_skip_5.keys != None:  # we had a response
            LearningSetTwo.addData('debugging_press_enter_to_skip_5.rt', debugging_press_enter_to_skip_5.rt)
            LearningSetTwo.addData('debugging_press_enter_to_skip_5.duration', debugging_press_enter_to_skip_5.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if breakBetweenRepeats.maxDurationReached:
            routineTimer.addTime(-breakBetweenRepeats.maxDuration)
        elif breakBetweenRepeats.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed numReps repeats of 'LearningSetTwo'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "routine_30Seconds" ---
    # create an object to store info about Routine routine_30Seconds
    routine_30Seconds = data.Routine(
        name='routine_30Seconds',
        components=[thirtySeconds, debugging_press_enter_to_skip_6],
    )
    routine_30Seconds.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for debugging_press_enter_to_skip_6
    debugging_press_enter_to_skip_6.keys = []
    debugging_press_enter_to_skip_6.rt = []
    _debugging_press_enter_to_skip_6_allKeys = []
    # store start times for routine_30Seconds
    routine_30Seconds.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_30Seconds.tStart = globalClock.getTime(format='float')
    routine_30Seconds.status = STARTED
    thisExp.addData('routine_30Seconds.started', routine_30Seconds.tStart)
    routine_30Seconds.maxDuration = None
    # keep track of which components have finished
    routine_30SecondsComponents = routine_30Seconds.components
    for thisComponent in routine_30Seconds.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_30Seconds" ---
    routine_30Seconds.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thirtySeconds* updates
        
        # if thirtySeconds is starting this frame...
        if thirtySeconds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thirtySeconds.frameNStart = frameN  # exact frame index
            thirtySeconds.tStart = t  # local t and not account for scr refresh
            thirtySeconds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thirtySeconds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thirtySeconds.started')
            # update status
            thirtySeconds.status = STARTED
            thirtySeconds.setAutoDraw(True)
        
        # if thirtySeconds is active this frame...
        if thirtySeconds.status == STARTED:
            # update params
            pass
        
        # if thirtySeconds is stopping this frame...
        if thirtySeconds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > thirtySeconds.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                thirtySeconds.tStop = t  # not accounting for scr refresh
                thirtySeconds.tStopRefresh = tThisFlipGlobal  # on global time
                thirtySeconds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'thirtySeconds.stopped')
                # update status
                thirtySeconds.status = FINISHED
                thirtySeconds.setAutoDraw(False)
        
        # *debugging_press_enter_to_skip_6* updates
        waitOnFlip = False
        
        # if debugging_press_enter_to_skip_6 is starting this frame...
        if debugging_press_enter_to_skip_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debugging_press_enter_to_skip_6.frameNStart = frameN  # exact frame index
            debugging_press_enter_to_skip_6.tStart = t  # local t and not account for scr refresh
            debugging_press_enter_to_skip_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debugging_press_enter_to_skip_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_6.started')
            # update status
            debugging_press_enter_to_skip_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(debugging_press_enter_to_skip_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(debugging_press_enter_to_skip_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if debugging_press_enter_to_skip_6 is stopping this frame...
        if debugging_press_enter_to_skip_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > debugging_press_enter_to_skip_6.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                debugging_press_enter_to_skip_6.tStop = t  # not accounting for scr refresh
                debugging_press_enter_to_skip_6.tStopRefresh = tThisFlipGlobal  # on global time
                debugging_press_enter_to_skip_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_6.stopped')
                # update status
                debugging_press_enter_to_skip_6.status = FINISHED
                debugging_press_enter_to_skip_6.status = FINISHED
        if debugging_press_enter_to_skip_6.status == STARTED and not waitOnFlip:
            theseKeys = debugging_press_enter_to_skip_6.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _debugging_press_enter_to_skip_6_allKeys.extend(theseKeys)
            if len(_debugging_press_enter_to_skip_6_allKeys):
                debugging_press_enter_to_skip_6.keys = _debugging_press_enter_to_skip_6_allKeys[-1].name  # just the last key pressed
                debugging_press_enter_to_skip_6.rt = _debugging_press_enter_to_skip_6_allKeys[-1].rt
                debugging_press_enter_to_skip_6.duration = _debugging_press_enter_to_skip_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routine_30Seconds.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_30Seconds.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_30Seconds" ---
    for thisComponent in routine_30Seconds.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_30Seconds
    routine_30Seconds.tStop = globalClock.getTime(format='float')
    routine_30Seconds.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_30Seconds.stopped', routine_30Seconds.tStop)
    # check responses
    if debugging_press_enter_to_skip_6.keys in ['', [], None]:  # No response was made
        debugging_press_enter_to_skip_6.keys = None
    thisExp.addData('debugging_press_enter_to_skip_6.keys',debugging_press_enter_to_skip_6.keys)
    if debugging_press_enter_to_skip_6.keys != None:  # we had a response
        thisExp.addData('debugging_press_enter_to_skip_6.rt', debugging_press_enter_to_skip_6.rt)
        thisExp.addData('debugging_press_enter_to_skip_6.duration', debugging_press_enter_to_skip_6.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_30Seconds.maxDurationReached:
        routineTimer.addTime(-routine_30Seconds.maxDuration)
    elif routine_30Seconds.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "start_test" ---
    # create an object to store info about Routine start_test
    start_test = data.Routine(
        name='start_test',
        components=[textWelcome, key_resp_11],
    )
    start_test.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_11
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # store start times for start_test
    start_test.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    start_test.tStart = globalClock.getTime(format='float')
    start_test.status = STARTED
    thisExp.addData('start_test.started', start_test.tStart)
    start_test.maxDuration = None
    # keep track of which components have finished
    start_testComponents = start_test.components
    for thisComponent in start_test.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start_test" ---
    start_test.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        
        # if textWelcome is starting this frame...
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.started')
            # update status
            textWelcome.status = STARTED
            textWelcome.setAutoDraw(True)
        
        # if textWelcome is active this frame...
        if textWelcome.status == STARTED:
            # update params
            pass
        
        # *key_resp_11* updates
        waitOnFlip = False
        
        # if key_resp_11 is starting this frame...
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_11.started')
            # update status
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                key_resp_11.duration = _key_resp_11_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            start_test.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_test.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start_test" ---
    for thisComponent in start_test.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for start_test
    start_test.tStop = globalClock.getTime(format='float')
    start_test.tStopRefresh = tThisFlipGlobal
    thisExp.addData('start_test.stopped', start_test.tStop)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    thisExp.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        thisExp.addData('key_resp_11.rt', key_resp_11.rt)
        thisExp.addData('key_resp_11.duration', key_resp_11.duration)
    thisExp.nextEntry()
    # the Routine "start_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testSet2 = data.TrialHandler2(
        name='testSet2',
        nReps=12.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(testSet2)  # add the loop to the experiment
    thisTestSet2 = testSet2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestSet2.rgb)
    if thisTestSet2 != None:
        for paramName in thisTestSet2:
            globals()[paramName] = thisTestSet2[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTestSet2 in testSet2:
        currentLoop = testSet2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTestSet2.rgb)
        if thisTestSet2 != None:
            for paramName in thisTestSet2:
                globals()[paramName] = thisTestSet2[paramName]
        
        # --- Prepare to start Routine "test2_NEW" ---
        # create an object to store info about Routine test2_NEW
        test2_NEW = data.Routine(
            name='test2_NEW',
            components=[textAmharic_6, textOptionA_6, textOptionB_6, textOptionC_6, textOptionD_6, textDiamond_5, key_resp_6, debugging_press_enter_to_skip_20],
        )
        test2_NEW.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeSymbol_6
        #incraments item counter by one
        curr_item2 += 1
        
        correct_word2 = word_list2[curr_item2] #THIS IS THE RIGHT ANSWER   
        amharic2 = amharic_list2[curr_item2]
        
        #preparing answer choices 
        lottery_list2 = []
        
        #add the right answer
        lottery_list2.append(correct_word2)
        
        #add 3 more non repeating answers
        copied_word2_list2 = []
        copied_word2_list2 = word_list2.copy() #copy word list
        copied_word2_list2.remove(correct_word2) #remove the right answer
        shuffle(copied_word2_list2) #shuffle up the copied list
        
        for x in range(0,3):    #add 3 from the shuffled list
            lottery_list2.append(copied_word2_list2[x])
        
        random.shuffle(lottery_list2)  #mix up the answer choices
        
        index_of_correct_answer2 = lottery_list2.index(correct_word2) #index of the correct word
        
        correctAns2 = index_to_button[index_of_correct_answer2] #correct answer in key form
        
        textAmharic_6.setText(amharic2)
        textOptionA_6.setText(lottery_list2[0]
        
        )
        textOptionB_6.setText(lottery_list2[1])
        textOptionC_6.setText(lottery_list2[2])
        textOptionD_6.setText(lottery_list2[3])
        textDiamond_5.setText(f"     {lottery_list2[0]}\n   {lottery_list2[1]}   {lottery_list2[2]}\n     {lottery_list2[3]}")
        # create starting attributes for key_resp_6
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # create starting attributes for debugging_press_enter_to_skip_20
        debugging_press_enter_to_skip_20.keys = []
        debugging_press_enter_to_skip_20.rt = []
        _debugging_press_enter_to_skip_20_allKeys = []
        # store start times for test2_NEW
        test2_NEW.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        test2_NEW.tStart = globalClock.getTime(format='float')
        test2_NEW.status = STARTED
        thisExp.addData('test2_NEW.started', test2_NEW.tStart)
        test2_NEW.maxDuration = None
        # keep track of which components have finished
        test2_NEWComponents = test2_NEW.components
        for thisComponent in test2_NEW.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test2_NEW" ---
        # if trial has changed, end Routine now
        if isinstance(testSet2, data.TrialHandler2) and thisTestSet2.thisN != testSet2.thisTrial.thisN:
            continueRoutine = False
        test2_NEW.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textAmharic_6* updates
            
            # if textAmharic_6 is starting this frame...
            if textAmharic_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textAmharic_6.frameNStart = frameN  # exact frame index
                textAmharic_6.tStart = t  # local t and not account for scr refresh
                textAmharic_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textAmharic_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textAmharic_6.started')
                # update status
                textAmharic_6.status = STARTED
                textAmharic_6.setAutoDraw(True)
            
            # if textAmharic_6 is active this frame...
            if textAmharic_6.status == STARTED:
                # update params
                pass
            
            # *textOptionA_6* updates
            
            # if textOptionA_6 is starting this frame...
            if textOptionA_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionA_6.frameNStart = frameN  # exact frame index
                textOptionA_6.tStart = t  # local t and not account for scr refresh
                textOptionA_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionA_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionA_6.started')
                # update status
                textOptionA_6.status = STARTED
                textOptionA_6.setAutoDraw(True)
            
            # if textOptionA_6 is active this frame...
            if textOptionA_6.status == STARTED:
                # update params
                pass
            
            # if textOptionA_6 is stopping this frame...
            if textOptionA_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionA_6.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionA_6.tStop = t  # not accounting for scr refresh
                    textOptionA_6.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionA_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionA_6.stopped')
                    # update status
                    textOptionA_6.status = FINISHED
                    textOptionA_6.setAutoDraw(False)
            
            # *textOptionB_6* updates
            
            # if textOptionB_6 is starting this frame...
            if textOptionB_6.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionB_6.frameNStart = frameN  # exact frame index
                textOptionB_6.tStart = t  # local t and not account for scr refresh
                textOptionB_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionB_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionB_6.started')
                # update status
                textOptionB_6.status = STARTED
                textOptionB_6.setAutoDraw(True)
            
            # if textOptionB_6 is active this frame...
            if textOptionB_6.status == STARTED:
                # update params
                pass
            
            # if textOptionB_6 is stopping this frame...
            if textOptionB_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionB_6.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionB_6.tStop = t  # not accounting for scr refresh
                    textOptionB_6.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionB_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionB_6.stopped')
                    # update status
                    textOptionB_6.status = FINISHED
                    textOptionB_6.setAutoDraw(False)
            
            # *textOptionC_6* updates
            
            # if textOptionC_6 is starting this frame...
            if textOptionC_6.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionC_6.frameNStart = frameN  # exact frame index
                textOptionC_6.tStart = t  # local t and not account for scr refresh
                textOptionC_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionC_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionC_6.started')
                # update status
                textOptionC_6.status = STARTED
                textOptionC_6.setAutoDraw(True)
            
            # if textOptionC_6 is active this frame...
            if textOptionC_6.status == STARTED:
                # update params
                pass
            
            # if textOptionC_6 is stopping this frame...
            if textOptionC_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionC_6.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionC_6.tStop = t  # not accounting for scr refresh
                    textOptionC_6.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionC_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionC_6.stopped')
                    # update status
                    textOptionC_6.status = FINISHED
                    textOptionC_6.setAutoDraw(False)
            
            # *textOptionD_6* updates
            
            # if textOptionD_6 is starting this frame...
            if textOptionD_6.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionD_6.frameNStart = frameN  # exact frame index
                textOptionD_6.tStart = t  # local t and not account for scr refresh
                textOptionD_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionD_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionD_6.started')
                # update status
                textOptionD_6.status = STARTED
                textOptionD_6.setAutoDraw(True)
            
            # if textOptionD_6 is active this frame...
            if textOptionD_6.status == STARTED:
                # update params
                pass
            
            # if textOptionD_6 is stopping this frame...
            if textOptionD_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionD_6.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionD_6.tStop = t  # not accounting for scr refresh
                    textOptionD_6.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionD_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionD_6.stopped')
                    # update status
                    textOptionD_6.status = FINISHED
                    textOptionD_6.setAutoDraw(False)
            
            # *textDiamond_5* updates
            
            # if textDiamond_5 is starting this frame...
            if textDiamond_5.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                textDiamond_5.frameNStart = frameN  # exact frame index
                textDiamond_5.tStart = t  # local t and not account for scr refresh
                textDiamond_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textDiamond_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textDiamond_5.started')
                # update status
                textDiamond_5.status = STARTED
                textDiamond_5.setAutoDraw(True)
            
            # if textDiamond_5 is active this frame...
            if textDiamond_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_6* updates
            waitOnFlip = False
            
            # if key_resp_6 is starting this frame...
            if key_resp_6.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_6.started')
                # update status
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['right','up','left','down'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_6.keys == str(correctAns2)) or (key_resp_6.keys == correctAns2):
                        key_resp_6.corr = 1
                    else:
                        key_resp_6.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *debugging_press_enter_to_skip_20* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_20 is starting this frame...
            if debugging_press_enter_to_skip_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_20.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_20.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_20, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_20.started')
                # update status
                debugging_press_enter_to_skip_20.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_20.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if debugging_press_enter_to_skip_20.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_20.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_20_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_20_allKeys):
                    debugging_press_enter_to_skip_20.keys = _debugging_press_enter_to_skip_20_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_20.rt = _debugging_press_enter_to_skip_20_allKeys[-1].rt
                    debugging_press_enter_to_skip_20.duration = _debugging_press_enter_to_skip_20_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                test2_NEW.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test2_NEW.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test2_NEW" ---
        for thisComponent in test2_NEW.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for test2_NEW
        test2_NEW.tStop = globalClock.getTime(format='float')
        test2_NEW.tStopRefresh = tThisFlipGlobal
        thisExp.addData('test2_NEW.stopped', test2_NEW.tStop)
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
            # was no response the correct answer?!
            if str(correctAns2).lower() == 'none':
               key_resp_6.corr = 1;  # correct non-response
            else:
               key_resp_6.corr = 0;  # failed to respond (incorrectly)
        # store data for testSet2 (TrialHandler)
        testSet2.addData('key_resp_6.keys',key_resp_6.keys)
        testSet2.addData('key_resp_6.corr', key_resp_6.corr)
        if key_resp_6.keys != None:  # we had a response
            testSet2.addData('key_resp_6.rt', key_resp_6.rt)
            testSet2.addData('key_resp_6.duration', key_resp_6.duration)
        # check responses
        if debugging_press_enter_to_skip_20.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_20.keys = None
        testSet2.addData('debugging_press_enter_to_skip_20.keys',debugging_press_enter_to_skip_20.keys)
        if debugging_press_enter_to_skip_20.keys != None:  # we had a response
            testSet2.addData('debugging_press_enter_to_skip_20.rt', debugging_press_enter_to_skip_20.rt)
            testSet2.addData('debugging_press_enter_to_skip_20.duration', debugging_press_enter_to_skip_20.duration)
        # the Routine "test2_NEW" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "checkForCorr_2" ---
        # create an object to store info about Routine checkForCorr_2
        checkForCorr_2 = data.Routine(
            name='checkForCorr_2',
            components=[],
        )
        checkForCorr_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        if key_resp_6.corr == 1:
            checkmark_reps = 1
            xmark_reps = 0
        if key_resp_6.corr == 0:
            checkmark_reps = 0
            xmark_reps = 1
        # store start times for checkForCorr_2
        checkForCorr_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        checkForCorr_2.tStart = globalClock.getTime(format='float')
        checkForCorr_2.status = STARTED
        thisExp.addData('checkForCorr_2.started', checkForCorr_2.tStart)
        checkForCorr_2.maxDuration = None
        # keep track of which components have finished
        checkForCorr_2Components = checkForCorr_2.components
        for thisComponent in checkForCorr_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "checkForCorr_2" ---
        # if trial has changed, end Routine now
        if isinstance(testSet2, data.TrialHandler2) and thisTestSet2.thisN != testSet2.thisTrial.thisN:
            continueRoutine = False
        checkForCorr_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                checkForCorr_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in checkForCorr_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "checkForCorr_2" ---
        for thisComponent in checkForCorr_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for checkForCorr_2
        checkForCorr_2.tStop = globalClock.getTime(format='float')
        checkForCorr_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('checkForCorr_2.stopped', checkForCorr_2.tStop)
        # the Routine "checkForCorr_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        checkloop2 = data.TrialHandler2(
            name='checkloop2',
            nReps=checkmark_reps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(checkloop2)  # add the loop to the experiment
        thisCheckloop2 = checkloop2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisCheckloop2.rgb)
        if thisCheckloop2 != None:
            for paramName in thisCheckloop2:
                globals()[paramName] = thisCheckloop2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisCheckloop2 in checkloop2:
            currentLoop = checkloop2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisCheckloop2.rgb)
            if thisCheckloop2 != None:
                for paramName in thisCheckloop2:
                    globals()[paramName] = thisCheckloop2[paramName]
            
            # --- Prepare to start Routine "checkmark" ---
            # create an object to store info about Routine checkmark
            checkmark = data.Routine(
                name='checkmark',
                components=[textCheck, debugging_press_enter_to_skip_7],
            )
            checkmark.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textCheck.setText(markers[0])
            # create starting attributes for debugging_press_enter_to_skip_7
            debugging_press_enter_to_skip_7.keys = []
            debugging_press_enter_to_skip_7.rt = []
            _debugging_press_enter_to_skip_7_allKeys = []
            # store start times for checkmark
            checkmark.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            checkmark.tStart = globalClock.getTime(format='float')
            checkmark.status = STARTED
            thisExp.addData('checkmark.started', checkmark.tStart)
            checkmark.maxDuration = None
            # keep track of which components have finished
            checkmarkComponents = checkmark.components
            for thisComponent in checkmark.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "checkmark" ---
            # if trial has changed, end Routine now
            if isinstance(checkloop2, data.TrialHandler2) and thisCheckloop2.thisN != checkloop2.thisTrial.thisN:
                continueRoutine = False
            checkmark.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textCheck* updates
                
                # if textCheck is starting this frame...
                if textCheck.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textCheck.frameNStart = frameN  # exact frame index
                    textCheck.tStart = t  # local t and not account for scr refresh
                    textCheck.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textCheck, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textCheck.started')
                    # update status
                    textCheck.status = STARTED
                    textCheck.setAutoDraw(True)
                
                # if textCheck is active this frame...
                if textCheck.status == STARTED:
                    # update params
                    pass
                
                # if textCheck is stopping this frame...
                if textCheck.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textCheck.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textCheck.tStop = t  # not accounting for scr refresh
                        textCheck.tStopRefresh = tThisFlipGlobal  # on global time
                        textCheck.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textCheck.stopped')
                        # update status
                        textCheck.status = FINISHED
                        textCheck.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_7* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_7 is starting this frame...
                if debugging_press_enter_to_skip_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_7.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_7.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_7.started')
                    # update status
                    debugging_press_enter_to_skip_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_7.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_7 is stopping this frame...
                if debugging_press_enter_to_skip_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_7.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_7.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_7.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_7.stopped')
                        # update status
                        debugging_press_enter_to_skip_7.status = FINISHED
                        debugging_press_enter_to_skip_7.status = FINISHED
                if debugging_press_enter_to_skip_7.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_7.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_7_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_7_allKeys):
                        debugging_press_enter_to_skip_7.keys = _debugging_press_enter_to_skip_7_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_7.rt = _debugging_press_enter_to_skip_7_allKeys[-1].rt
                        debugging_press_enter_to_skip_7.duration = _debugging_press_enter_to_skip_7_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    checkmark.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in checkmark.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "checkmark" ---
            for thisComponent in checkmark.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for checkmark
            checkmark.tStop = globalClock.getTime(format='float')
            checkmark.tStopRefresh = tThisFlipGlobal
            thisExp.addData('checkmark.stopped', checkmark.tStop)
            # check responses
            if debugging_press_enter_to_skip_7.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_7.keys = None
            checkloop2.addData('debugging_press_enter_to_skip_7.keys',debugging_press_enter_to_skip_7.keys)
            if debugging_press_enter_to_skip_7.keys != None:  # we had a response
                checkloop2.addData('debugging_press_enter_to_skip_7.rt', debugging_press_enter_to_skip_7.rt)
                checkloop2.addData('debugging_press_enter_to_skip_7.duration', debugging_press_enter_to_skip_7.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if checkmark.maxDurationReached:
                routineTimer.addTime(-checkmark.maxDuration)
            elif checkmark.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed checkmark_reps repeats of 'checkloop2'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        xmark2 = data.TrialHandler2(
            name='xmark2',
            nReps=xmark_reps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(xmark2)  # add the loop to the experiment
        thisXmark2 = xmark2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisXmark2.rgb)
        if thisXmark2 != None:
            for paramName in thisXmark2:
                globals()[paramName] = thisXmark2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisXmark2 in xmark2:
            currentLoop = xmark2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisXmark2.rgb)
            if thisXmark2 != None:
                for paramName in thisXmark2:
                    globals()[paramName] = thisXmark2[paramName]
            
            # --- Prepare to start Routine "xmark" ---
            # create an object to store info about Routine xmark
            xmark = data.Routine(
                name='xmark',
                components=[textXmark, debugging_press_enter_to_skip_26],
            )
            xmark.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textXmark.setText(markers[1])
            # create starting attributes for debugging_press_enter_to_skip_26
            debugging_press_enter_to_skip_26.keys = []
            debugging_press_enter_to_skip_26.rt = []
            _debugging_press_enter_to_skip_26_allKeys = []
            # store start times for xmark
            xmark.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            xmark.tStart = globalClock.getTime(format='float')
            xmark.status = STARTED
            thisExp.addData('xmark.started', xmark.tStart)
            xmark.maxDuration = None
            # keep track of which components have finished
            xmarkComponents = xmark.components
            for thisComponent in xmark.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "xmark" ---
            # if trial has changed, end Routine now
            if isinstance(xmark2, data.TrialHandler2) and thisXmark2.thisN != xmark2.thisTrial.thisN:
                continueRoutine = False
            xmark.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textXmark* updates
                
                # if textXmark is starting this frame...
                if textXmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textXmark.frameNStart = frameN  # exact frame index
                    textXmark.tStart = t  # local t and not account for scr refresh
                    textXmark.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textXmark, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textXmark.started')
                    # update status
                    textXmark.status = STARTED
                    textXmark.setAutoDraw(True)
                
                # if textXmark is active this frame...
                if textXmark.status == STARTED:
                    # update params
                    pass
                
                # if textXmark is stopping this frame...
                if textXmark.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textXmark.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textXmark.tStop = t  # not accounting for scr refresh
                        textXmark.tStopRefresh = tThisFlipGlobal  # on global time
                        textXmark.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textXmark.stopped')
                        # update status
                        textXmark.status = FINISHED
                        textXmark.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_26* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_26 is starting this frame...
                if debugging_press_enter_to_skip_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_26.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_26.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_26, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_26.started')
                    # update status
                    debugging_press_enter_to_skip_26.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_26.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_26 is stopping this frame...
                if debugging_press_enter_to_skip_26.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_26.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_26.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_26.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_26.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_26.stopped')
                        # update status
                        debugging_press_enter_to_skip_26.status = FINISHED
                        debugging_press_enter_to_skip_26.status = FINISHED
                if debugging_press_enter_to_skip_26.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_26.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_26_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_26_allKeys):
                        debugging_press_enter_to_skip_26.keys = _debugging_press_enter_to_skip_26_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_26.rt = _debugging_press_enter_to_skip_26_allKeys[-1].rt
                        debugging_press_enter_to_skip_26.duration = _debugging_press_enter_to_skip_26_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    xmark.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in xmark.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "xmark" ---
            for thisComponent in xmark.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for xmark
            xmark.tStop = globalClock.getTime(format='float')
            xmark.tStopRefresh = tThisFlipGlobal
            thisExp.addData('xmark.stopped', xmark.tStop)
            # check responses
            if debugging_press_enter_to_skip_26.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_26.keys = None
            xmark2.addData('debugging_press_enter_to_skip_26.keys',debugging_press_enter_to_skip_26.keys)
            if debugging_press_enter_to_skip_26.keys != None:  # we had a response
                xmark2.addData('debugging_press_enter_to_skip_26.rt', debugging_press_enter_to_skip_26.rt)
                xmark2.addData('debugging_press_enter_to_skip_26.duration', debugging_press_enter_to_skip_26.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if xmark.maxDurationReached:
                routineTimer.addTime(-xmark.maxDuration)
            elif xmark.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed xmark_reps repeats of 'xmark2'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "resetReps" ---
        # create an object to store info about Routine resetReps
        resetReps = data.Routine(
            name='resetReps',
            components=[],
        )
        resetReps.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for resetReps
        resetReps.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        resetReps.tStart = globalClock.getTime(format='float')
        resetReps.status = STARTED
        thisExp.addData('resetReps.started', resetReps.tStart)
        resetReps.maxDuration = None
        # keep track of which components have finished
        resetRepsComponents = resetReps.components
        for thisComponent in resetReps.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "resetReps" ---
        # if trial has changed, end Routine now
        if isinstance(testSet2, data.TrialHandler2) and thisTestSet2.thisN != testSet2.thisTrial.thisN:
            continueRoutine = False
        resetReps.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                resetReps.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in resetReps.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "resetReps" ---
        for thisComponent in resetReps.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for resetReps
        resetReps.tStop = globalClock.getTime(format='float')
        resetReps.tStopRefresh = tThisFlipGlobal
        thisExp.addData('resetReps.stopped', resetReps.tStop)
        # the Routine "resetReps" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        # create an object to store info about Routine blank500
        blank500 = data.Routine(
            name='blank500',
            components=[text_2, debugging_press_enter_to_skip_15],
        )
        blank500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_2.setText('')
        # create starting attributes for debugging_press_enter_to_skip_15
        debugging_press_enter_to_skip_15.keys = []
        debugging_press_enter_to_skip_15.rt = []
        _debugging_press_enter_to_skip_15_allKeys = []
        # store start times for blank500
        blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank500.tStart = globalClock.getTime(format='float')
        blank500.status = STARTED
        thisExp.addData('blank500.started', blank500.tStart)
        blank500.maxDuration = None
        # keep track of which components have finished
        blank500Components = blank500.components
        for thisComponent in blank500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        # if trial has changed, end Routine now
        if isinstance(testSet2, data.TrialHandler2) and thisTestSet2.thisN != testSet2.thisTrial.thisN:
            continueRoutine = False
        blank500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # *debugging_press_enter_to_skip_15* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_15 is starting this frame...
            if debugging_press_enter_to_skip_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_15.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_15.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_15.started')
                # update status
                debugging_press_enter_to_skip_15.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_15.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if debugging_press_enter_to_skip_15 is stopping this frame...
            if debugging_press_enter_to_skip_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > debugging_press_enter_to_skip_15.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    debugging_press_enter_to_skip_15.tStop = t  # not accounting for scr refresh
                    debugging_press_enter_to_skip_15.tStopRefresh = tThisFlipGlobal  # on global time
                    debugging_press_enter_to_skip_15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_15.stopped')
                    # update status
                    debugging_press_enter_to_skip_15.status = FINISHED
                    debugging_press_enter_to_skip_15.status = FINISHED
            if debugging_press_enter_to_skip_15.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_15.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_15_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_15_allKeys):
                    debugging_press_enter_to_skip_15.keys = _debugging_press_enter_to_skip_15_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_15.rt = _debugging_press_enter_to_skip_15_allKeys[-1].rt
                    debugging_press_enter_to_skip_15.duration = _debugging_press_enter_to_skip_15_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank500
        blank500.tStop = globalClock.getTime(format='float')
        blank500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank500.stopped', blank500.tStop)
        # check responses
        if debugging_press_enter_to_skip_15.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_15.keys = None
        testSet2.addData('debugging_press_enter_to_skip_15.keys',debugging_press_enter_to_skip_15.keys)
        if debugging_press_enter_to_skip_15.keys != None:  # we had a response
            testSet2.addData('debugging_press_enter_to_skip_15.rt', debugging_press_enter_to_skip_15.rt)
            testSet2.addData('debugging_press_enter_to_skip_15.duration', debugging_press_enter_to_skip_15.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank500.maxDurationReached:
            routineTimer.addTime(-blank500.maxDuration)
        elif blank500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed 12.0 repeats of 'testSet2'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "breakBetweenSets" ---
    # create an object to store info about Routine breakBetweenSets
    breakBetweenSets = data.Routine(
        name='breakBetweenSets',
        components=[cross, debugging_press_enter_to_skip_8],
    )
    breakBetweenSets.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for debugging_press_enter_to_skip_8
    debugging_press_enter_to_skip_8.keys = []
    debugging_press_enter_to_skip_8.rt = []
    _debugging_press_enter_to_skip_8_allKeys = []
    # store start times for breakBetweenSets
    breakBetweenSets.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    breakBetweenSets.tStart = globalClock.getTime(format='float')
    breakBetweenSets.status = STARTED
    thisExp.addData('breakBetweenSets.started', breakBetweenSets.tStart)
    breakBetweenSets.maxDuration = None
    # keep track of which components have finished
    breakBetweenSetsComponents = breakBetweenSets.components
    for thisComponent in breakBetweenSets.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "breakBetweenSets" ---
    breakBetweenSets.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.tStopRefresh = tThisFlipGlobal  # on global time
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # *debugging_press_enter_to_skip_8* updates
        waitOnFlip = False
        
        # if debugging_press_enter_to_skip_8 is starting this frame...
        if debugging_press_enter_to_skip_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debugging_press_enter_to_skip_8.frameNStart = frameN  # exact frame index
            debugging_press_enter_to_skip_8.tStart = t  # local t and not account for scr refresh
            debugging_press_enter_to_skip_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debugging_press_enter_to_skip_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_8.started')
            # update status
            debugging_press_enter_to_skip_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(debugging_press_enter_to_skip_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(debugging_press_enter_to_skip_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if debugging_press_enter_to_skip_8 is stopping this frame...
        if debugging_press_enter_to_skip_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > debugging_press_enter_to_skip_8.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                debugging_press_enter_to_skip_8.tStop = t  # not accounting for scr refresh
                debugging_press_enter_to_skip_8.tStopRefresh = tThisFlipGlobal  # on global time
                debugging_press_enter_to_skip_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_8.stopped')
                # update status
                debugging_press_enter_to_skip_8.status = FINISHED
                debugging_press_enter_to_skip_8.status = FINISHED
        if debugging_press_enter_to_skip_8.status == STARTED and not waitOnFlip:
            theseKeys = debugging_press_enter_to_skip_8.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _debugging_press_enter_to_skip_8_allKeys.extend(theseKeys)
            if len(_debugging_press_enter_to_skip_8_allKeys):
                debugging_press_enter_to_skip_8.keys = _debugging_press_enter_to_skip_8_allKeys[-1].name  # just the last key pressed
                debugging_press_enter_to_skip_8.rt = _debugging_press_enter_to_skip_8_allKeys[-1].rt
                debugging_press_enter_to_skip_8.duration = _debugging_press_enter_to_skip_8_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            breakBetweenSets.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breakBetweenSets.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "breakBetweenSets" ---
    for thisComponent in breakBetweenSets.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for breakBetweenSets
    breakBetweenSets.tStop = globalClock.getTime(format='float')
    breakBetweenSets.tStopRefresh = tThisFlipGlobal
    thisExp.addData('breakBetweenSets.stopped', breakBetweenSets.tStop)
    # check responses
    if debugging_press_enter_to_skip_8.keys in ['', [], None]:  # No response was made
        debugging_press_enter_to_skip_8.keys = None
    thisExp.addData('debugging_press_enter_to_skip_8.keys',debugging_press_enter_to_skip_8.keys)
    if debugging_press_enter_to_skip_8.keys != None:  # we had a response
        thisExp.addData('debugging_press_enter_to_skip_8.rt', debugging_press_enter_to_skip_8.rt)
        thisExp.addData('debugging_press_enter_to_skip_8.duration', debugging_press_enter_to_skip_8.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if breakBetweenSets.maxDurationReached:
        routineTimer.addTime(-breakBetweenSets.maxDuration)
    elif breakBetweenSets.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    LearningSetThree = data.TrialHandler2(
        name='LearningSetThree',
        nReps=numReps, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(LearningSetThree)  # add the loop to the experiment
    thisLearningSetThree = LearningSetThree.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLearningSetThree.rgb)
    if thisLearningSetThree != None:
        for paramName in thisLearningSetThree:
            globals()[paramName] = thisLearningSetThree[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLearningSetThree in LearningSetThree:
        currentLoop = LearningSetThree
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLearningSetThree.rgb)
        if thisLearningSetThree != None:
            for paramName in thisLearningSetThree:
                globals()[paramName] = thisLearningSetThree[paramName]
        
        # --- Prepare to start Routine "randomize_set" ---
        # create an object to store info about Routine randomize_set
        randomize_set = data.Routine(
            name='randomize_set',
            components=[],
        )
        randomize_set.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from randomize_learning_set
        keys = list(range(12))
        random.shuffle(keys)
        print("learning set order: " + str(keys))
        
        practice_keys = list(range(6))
        random.shuffle(practice_keys)
        print("learning set order: " + str(keys))
        
        practice_keys2 = list(range(6,12))
        random.shuffle(practice_keys2)
        print("learning set order: " + str(keys))
        # store start times for randomize_set
        randomize_set.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        randomize_set.tStart = globalClock.getTime(format='float')
        randomize_set.status = STARTED
        thisExp.addData('randomize_set.started', randomize_set.tStart)
        randomize_set.maxDuration = None
        # keep track of which components have finished
        randomize_setComponents = randomize_set.components
        for thisComponent in randomize_set.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "randomize_set" ---
        # if trial has changed, end Routine now
        if isinstance(LearningSetThree, data.TrialHandler2) and thisLearningSetThree.thisN != LearningSetThree.thisTrial.thisN:
            continueRoutine = False
        randomize_set.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                randomize_set.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in randomize_set.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "randomize_set" ---
        for thisComponent in randomize_set.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for randomize_set
        randomize_set.tStop = globalClock.getTime(format='float')
        randomize_set.tStopRefresh = tThisFlipGlobal
        thisExp.addData('randomize_set.stopped', randomize_set.tStop)
        # the Routine "randomize_set" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        setThree = data.TrialHandler2(
            name='setThree',
            nReps=12.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(setThree)  # add the loop to the experiment
        thisSetThree = setThree.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSetThree.rgb)
        if thisSetThree != None:
            for paramName in thisSetThree:
                globals()[paramName] = thisSetThree[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisSetThree in setThree:
            currentLoop = setThree
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisSetThree.rgb)
            if thisSetThree != None:
                for paramName in thisSetThree:
                    globals()[paramName] = thisSetThree[paramName]
            
            # --- Prepare to start Routine "Increment" ---
            # create an object to store info about Routine Increment
            Increment = data.Routine(
                name='Increment',
                components=[],
            )
            Increment.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from increment_index
            learning_index += 1
            learning_index %= len(keys)
            
            practice_index += 1
            practice_index %= len(practice_keys)
            # store start times for Increment
            Increment.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Increment.tStart = globalClock.getTime(format='float')
            Increment.status = STARTED
            thisExp.addData('Increment.started', Increment.tStart)
            Increment.maxDuration = None
            # keep track of which components have finished
            IncrementComponents = Increment.components
            for thisComponent in Increment.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Increment" ---
            # if trial has changed, end Routine now
            if isinstance(setThree, data.TrialHandler2) and thisSetThree.thisN != setThree.thisTrial.thisN:
                continueRoutine = False
            Increment.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Increment.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Increment.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Increment" ---
            for thisComponent in Increment.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Increment
            Increment.tStop = globalClock.getTime(format='float')
            Increment.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Increment.stopped', Increment.tStop)
            # the Routine "Increment" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            nreps_A3 = data.TrialHandler2(
                name='nreps_A3',
                nReps=nreps_A, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(nreps_A3)  # add the loop to the experiment
            thisNreps_A3 = nreps_A3.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisNreps_A3.rgb)
            if thisNreps_A3 != None:
                for paramName in thisNreps_A3:
                    globals()[paramName] = thisNreps_A3[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisNreps_A3 in nreps_A3:
                currentLoop = nreps_A3
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisNreps_A3.rgb)
                if thisNreps_A3 != None:
                    for paramName in thisNreps_A3:
                        globals()[paramName] = thisNreps_A3[paramName]
                
                # --- Prepare to start Routine "amharic3_A" ---
                # create an object to store info about Routine amharic3_A
                amharic3_A = data.Routine(
                    name='amharic3_A',
                    components=[amharics3, words3_image, debugging_press_enter_to_skip_11],
                )
                amharic3_A.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                amharics3.setText(amharic_word_list3[keys[learning_index]][0])
                words3_image.setImage(amharic_word_list3[keys[learning_index]][2])
                # Run 'Begin Routine' code from code3
                print("Index: " + str(keys[learning_index]) + 
                      "\n Character: " + str(amharic_word_list3[keys[learning_index]][0]) + 
                      "\n Meaning: " + str(amharic_word_list3[keys[learning_index]][1]) + 
                      "\n Image Path: " + str(amharic_word_list3[keys[learning_index]][2]))
                # create starting attributes for debugging_press_enter_to_skip_11
                debugging_press_enter_to_skip_11.keys = []
                debugging_press_enter_to_skip_11.rt = []
                _debugging_press_enter_to_skip_11_allKeys = []
                # store start times for amharic3_A
                amharic3_A.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                amharic3_A.tStart = globalClock.getTime(format='float')
                amharic3_A.status = STARTED
                thisExp.addData('amharic3_A.started', amharic3_A.tStart)
                amharic3_A.maxDuration = None
                # keep track of which components have finished
                amharic3_AComponents = amharic3_A.components
                for thisComponent in amharic3_A.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "amharic3_A" ---
                # if trial has changed, end Routine now
                if isinstance(nreps_A3, data.TrialHandler2) and thisNreps_A3.thisN != nreps_A3.thisTrial.thisN:
                    continueRoutine = False
                amharic3_A.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *amharics3* updates
                    
                    # if amharics3 is starting this frame...
                    if amharics3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        amharics3.frameNStart = frameN  # exact frame index
                        amharics3.tStart = t  # local t and not account for scr refresh
                        amharics3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(amharics3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'amharics3.started')
                        # update status
                        amharics3.status = STARTED
                        amharics3.setAutoDraw(True)
                    
                    # if amharics3 is active this frame...
                    if amharics3.status == STARTED:
                        # update params
                        pass
                    
                    # if amharics3 is stopping this frame...
                    if amharics3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > amharics3.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            amharics3.tStop = t  # not accounting for scr refresh
                            amharics3.tStopRefresh = tThisFlipGlobal  # on global time
                            amharics3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'amharics3.stopped')
                            # update status
                            amharics3.status = FINISHED
                            amharics3.setAutoDraw(False)
                    
                    # *words3_image* updates
                    
                    # if words3_image is starting this frame...
                    if words3_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        words3_image.frameNStart = frameN  # exact frame index
                        words3_image.tStart = t  # local t and not account for scr refresh
                        words3_image.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(words3_image, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'words3_image.started')
                        # update status
                        words3_image.status = STARTED
                        words3_image.setAutoDraw(True)
                    
                    # if words3_image is active this frame...
                    if words3_image.status == STARTED:
                        # update params
                        pass
                    
                    # if words3_image is stopping this frame...
                    if words3_image.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > words3_image.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            words3_image.tStop = t  # not accounting for scr refresh
                            words3_image.tStopRefresh = tThisFlipGlobal  # on global time
                            words3_image.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'words3_image.stopped')
                            # update status
                            words3_image.status = FINISHED
                            words3_image.setAutoDraw(False)
                    
                    # *debugging_press_enter_to_skip_11* updates
                    waitOnFlip = False
                    
                    # if debugging_press_enter_to_skip_11 is starting this frame...
                    if debugging_press_enter_to_skip_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        debugging_press_enter_to_skip_11.frameNStart = frameN  # exact frame index
                        debugging_press_enter_to_skip_11.tStart = t  # local t and not account for scr refresh
                        debugging_press_enter_to_skip_11.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(debugging_press_enter_to_skip_11, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_11.started')
                        # update status
                        debugging_press_enter_to_skip_11.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(debugging_press_enter_to_skip_11.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(debugging_press_enter_to_skip_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if debugging_press_enter_to_skip_11 is stopping this frame...
                    if debugging_press_enter_to_skip_11.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > debugging_press_enter_to_skip_11.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            debugging_press_enter_to_skip_11.tStop = t  # not accounting for scr refresh
                            debugging_press_enter_to_skip_11.tStopRefresh = tThisFlipGlobal  # on global time
                            debugging_press_enter_to_skip_11.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_11.stopped')
                            # update status
                            debugging_press_enter_to_skip_11.status = FINISHED
                            debugging_press_enter_to_skip_11.status = FINISHED
                    if debugging_press_enter_to_skip_11.status == STARTED and not waitOnFlip:
                        theseKeys = debugging_press_enter_to_skip_11.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                        _debugging_press_enter_to_skip_11_allKeys.extend(theseKeys)
                        if len(_debugging_press_enter_to_skip_11_allKeys):
                            debugging_press_enter_to_skip_11.keys = _debugging_press_enter_to_skip_11_allKeys[-1].name  # just the last key pressed
                            debugging_press_enter_to_skip_11.rt = _debugging_press_enter_to_skip_11_allKeys[-1].rt
                            debugging_press_enter_to_skip_11.duration = _debugging_press_enter_to_skip_11_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        amharic3_A.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in amharic3_A.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "amharic3_A" ---
                for thisComponent in amharic3_A.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for amharic3_A
                amharic3_A.tStop = globalClock.getTime(format='float')
                amharic3_A.tStopRefresh = tThisFlipGlobal
                thisExp.addData('amharic3_A.stopped', amharic3_A.tStop)
                # check responses
                if debugging_press_enter_to_skip_11.keys in ['', [], None]:  # No response was made
                    debugging_press_enter_to_skip_11.keys = None
                nreps_A3.addData('debugging_press_enter_to_skip_11.keys',debugging_press_enter_to_skip_11.keys)
                if debugging_press_enter_to_skip_11.keys != None:  # we had a response
                    nreps_A3.addData('debugging_press_enter_to_skip_11.rt', debugging_press_enter_to_skip_11.rt)
                    nreps_A3.addData('debugging_press_enter_to_skip_11.duration', debugging_press_enter_to_skip_11.duration)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if amharic3_A.maxDurationReached:
                    routineTimer.addTime(-amharic3_A.maxDuration)
                elif amharic3_A.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
            # completed nreps_A repeats of 'nreps_A3'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # set up handler to look after randomisation of conditions etc
            nreps_B3 = data.TrialHandler2(
                name='nreps_B3',
                nReps=nreps_B, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(nreps_B3)  # add the loop to the experiment
            thisNreps_B3 = nreps_B3.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisNreps_B3.rgb)
            if thisNreps_B3 != None:
                for paramName in thisNreps_B3:
                    globals()[paramName] = thisNreps_B3[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisNreps_B3 in nreps_B3:
                currentLoop = nreps_B3
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisNreps_B3.rgb)
                if thisNreps_B3 != None:
                    for paramName in thisNreps_B3:
                        globals()[paramName] = thisNreps_B3[paramName]
                
                # --- Prepare to start Routine "amharic3_B" ---
                # create an object to store info about Routine amharic3_B
                amharic3_B = data.Routine(
                    name='amharic3_B',
                    components=[amharics3_2, words3_2, debugging_press_enter_to_skip_12],
                )
                amharic3_B.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                amharics3_2.setText(amharic_word_list3[keys[learning_index]][0])
                words3_2.setText(amharic_word_list3[keys[learning_index]][1])
                # Run 'Begin Routine' code from code3_2
                print("Index: " + str(keys[learning_index]) + 
                      "\n Character: " + str(amharic_word_list3[keys[learning_index]][0]) + 
                      "\n Meaning: " + str(amharic_word_list3[keys[learning_index]][1]) + 
                      "\n Image Path: " + str(amharic_word_list3[keys[learning_index]][2]))
                # create starting attributes for debugging_press_enter_to_skip_12
                debugging_press_enter_to_skip_12.keys = []
                debugging_press_enter_to_skip_12.rt = []
                _debugging_press_enter_to_skip_12_allKeys = []
                # store start times for amharic3_B
                amharic3_B.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                amharic3_B.tStart = globalClock.getTime(format='float')
                amharic3_B.status = STARTED
                thisExp.addData('amharic3_B.started', amharic3_B.tStart)
                amharic3_B.maxDuration = None
                # keep track of which components have finished
                amharic3_BComponents = amharic3_B.components
                for thisComponent in amharic3_B.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "amharic3_B" ---
                # if trial has changed, end Routine now
                if isinstance(nreps_B3, data.TrialHandler2) and thisNreps_B3.thisN != nreps_B3.thisTrial.thisN:
                    continueRoutine = False
                amharic3_B.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *amharics3_2* updates
                    
                    # if amharics3_2 is starting this frame...
                    if amharics3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        amharics3_2.frameNStart = frameN  # exact frame index
                        amharics3_2.tStart = t  # local t and not account for scr refresh
                        amharics3_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(amharics3_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'amharics3_2.started')
                        # update status
                        amharics3_2.status = STARTED
                        amharics3_2.setAutoDraw(True)
                    
                    # if amharics3_2 is active this frame...
                    if amharics3_2.status == STARTED:
                        # update params
                        pass
                    
                    # if amharics3_2 is stopping this frame...
                    if amharics3_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > amharics3_2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            amharics3_2.tStop = t  # not accounting for scr refresh
                            amharics3_2.tStopRefresh = tThisFlipGlobal  # on global time
                            amharics3_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'amharics3_2.stopped')
                            # update status
                            amharics3_2.status = FINISHED
                            amharics3_2.setAutoDraw(False)
                    
                    # *words3_2* updates
                    
                    # if words3_2 is starting this frame...
                    if words3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        words3_2.frameNStart = frameN  # exact frame index
                        words3_2.tStart = t  # local t and not account for scr refresh
                        words3_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(words3_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'words3_2.started')
                        # update status
                        words3_2.status = STARTED
                        words3_2.setAutoDraw(True)
                    
                    # if words3_2 is active this frame...
                    if words3_2.status == STARTED:
                        # update params
                        pass
                    
                    # if words3_2 is stopping this frame...
                    if words3_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > words3_2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            words3_2.tStop = t  # not accounting for scr refresh
                            words3_2.tStopRefresh = tThisFlipGlobal  # on global time
                            words3_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'words3_2.stopped')
                            # update status
                            words3_2.status = FINISHED
                            words3_2.setAutoDraw(False)
                    
                    # *debugging_press_enter_to_skip_12* updates
                    waitOnFlip = False
                    
                    # if debugging_press_enter_to_skip_12 is starting this frame...
                    if debugging_press_enter_to_skip_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        debugging_press_enter_to_skip_12.frameNStart = frameN  # exact frame index
                        debugging_press_enter_to_skip_12.tStart = t  # local t and not account for scr refresh
                        debugging_press_enter_to_skip_12.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(debugging_press_enter_to_skip_12, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_12.started')
                        # update status
                        debugging_press_enter_to_skip_12.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(debugging_press_enter_to_skip_12.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(debugging_press_enter_to_skip_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if debugging_press_enter_to_skip_12 is stopping this frame...
                    if debugging_press_enter_to_skip_12.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > debugging_press_enter_to_skip_12.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            debugging_press_enter_to_skip_12.tStop = t  # not accounting for scr refresh
                            debugging_press_enter_to_skip_12.tStopRefresh = tThisFlipGlobal  # on global time
                            debugging_press_enter_to_skip_12.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_12.stopped')
                            # update status
                            debugging_press_enter_to_skip_12.status = FINISHED
                            debugging_press_enter_to_skip_12.status = FINISHED
                    if debugging_press_enter_to_skip_12.status == STARTED and not waitOnFlip:
                        theseKeys = debugging_press_enter_to_skip_12.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                        _debugging_press_enter_to_skip_12_allKeys.extend(theseKeys)
                        if len(_debugging_press_enter_to_skip_12_allKeys):
                            debugging_press_enter_to_skip_12.keys = _debugging_press_enter_to_skip_12_allKeys[-1].name  # just the last key pressed
                            debugging_press_enter_to_skip_12.rt = _debugging_press_enter_to_skip_12_allKeys[-1].rt
                            debugging_press_enter_to_skip_12.duration = _debugging_press_enter_to_skip_12_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        amharic3_B.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in amharic3_B.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "amharic3_B" ---
                for thisComponent in amharic3_B.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for amharic3_B
                amharic3_B.tStop = globalClock.getTime(format='float')
                amharic3_B.tStopRefresh = tThisFlipGlobal
                thisExp.addData('amharic3_B.stopped', amharic3_B.tStop)
                # check responses
                if debugging_press_enter_to_skip_12.keys in ['', [], None]:  # No response was made
                    debugging_press_enter_to_skip_12.keys = None
                nreps_B3.addData('debugging_press_enter_to_skip_12.keys',debugging_press_enter_to_skip_12.keys)
                if debugging_press_enter_to_skip_12.keys != None:  # we had a response
                    nreps_B3.addData('debugging_press_enter_to_skip_12.rt', debugging_press_enter_to_skip_12.rt)
                    nreps_B3.addData('debugging_press_enter_to_skip_12.duration', debugging_press_enter_to_skip_12.duration)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if amharic3_B.maxDurationReached:
                    routineTimer.addTime(-amharic3_B.maxDuration)
                elif amharic3_B.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
            # completed nreps_B repeats of 'nreps_B3'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # --- Prepare to start Routine "plusBetween" ---
            # create an object to store info about Routine plusBetween
            plusBetween = data.Routine(
                name='plusBetween',
                components=[plus, debugging_press_enter_to_skip_4],
            )
            plusBetween.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            plus.setText('+')
            # create starting attributes for debugging_press_enter_to_skip_4
            debugging_press_enter_to_skip_4.keys = []
            debugging_press_enter_to_skip_4.rt = []
            _debugging_press_enter_to_skip_4_allKeys = []
            # store start times for plusBetween
            plusBetween.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            plusBetween.tStart = globalClock.getTime(format='float')
            plusBetween.status = STARTED
            thisExp.addData('plusBetween.started', plusBetween.tStart)
            plusBetween.maxDuration = None
            # keep track of which components have finished
            plusBetweenComponents = plusBetween.components
            for thisComponent in plusBetween.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "plusBetween" ---
            # if trial has changed, end Routine now
            if isinstance(setThree, data.TrialHandler2) and thisSetThree.thisN != setThree.thisTrial.thisN:
                continueRoutine = False
            plusBetween.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *plus* updates
                
                # if plus is starting this frame...
                if plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    plus.frameNStart = frameN  # exact frame index
                    plus.tStart = t  # local t and not account for scr refresh
                    plus.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(plus, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'plus.started')
                    # update status
                    plus.status = STARTED
                    plus.setAutoDraw(True)
                
                # if plus is active this frame...
                if plus.status == STARTED:
                    # update params
                    pass
                
                # if plus is stopping this frame...
                if plus.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > plus.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        plus.tStop = t  # not accounting for scr refresh
                        plus.tStopRefresh = tThisFlipGlobal  # on global time
                        plus.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'plus.stopped')
                        # update status
                        plus.status = FINISHED
                        plus.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_4* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_4 is starting this frame...
                if debugging_press_enter_to_skip_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_4.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_4.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.started')
                    # update status
                    debugging_press_enter_to_skip_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_4 is stopping this frame...
                if debugging_press_enter_to_skip_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_4.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_4.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_4.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.stopped')
                        # update status
                        debugging_press_enter_to_skip_4.status = FINISHED
                        debugging_press_enter_to_skip_4.status = FINISHED
                if debugging_press_enter_to_skip_4.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_4.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_4_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_4_allKeys):
                        debugging_press_enter_to_skip_4.keys = _debugging_press_enter_to_skip_4_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_4.rt = _debugging_press_enter_to_skip_4_allKeys[-1].rt
                        debugging_press_enter_to_skip_4.duration = _debugging_press_enter_to_skip_4_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    plusBetween.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in plusBetween.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "plusBetween" ---
            for thisComponent in plusBetween.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for plusBetween
            plusBetween.tStop = globalClock.getTime(format='float')
            plusBetween.tStopRefresh = tThisFlipGlobal
            thisExp.addData('plusBetween.stopped', plusBetween.tStop)
            # check responses
            if debugging_press_enter_to_skip_4.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_4.keys = None
            setThree.addData('debugging_press_enter_to_skip_4.keys',debugging_press_enter_to_skip_4.keys)
            if debugging_press_enter_to_skip_4.keys != None:  # we had a response
                setThree.addData('debugging_press_enter_to_skip_4.rt', debugging_press_enter_to_skip_4.rt)
                setThree.addData('debugging_press_enter_to_skip_4.duration', debugging_press_enter_to_skip_4.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if plusBetween.maxDurationReached:
                routineTimer.addTime(-plusBetween.maxDuration)
            elif plusBetween.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 12.0 repeats of 'setThree'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "breakBetweenRepeats" ---
        # create an object to store info about Routine breakBetweenRepeats
        breakBetweenRepeats = data.Routine(
            name='breakBetweenRepeats',
            components=[five_seconds, maybe_a_beep, debugging_press_enter_to_skip_5],
        )
        breakBetweenRepeats.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        maybe_a_beep.setSound('A', secs=1.0, hamming=True)
        maybe_a_beep.setVolume(1.0, log=False)
        maybe_a_beep.seek(0)
        # create starting attributes for debugging_press_enter_to_skip_5
        debugging_press_enter_to_skip_5.keys = []
        debugging_press_enter_to_skip_5.rt = []
        _debugging_press_enter_to_skip_5_allKeys = []
        # store start times for breakBetweenRepeats
        breakBetweenRepeats.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        breakBetweenRepeats.tStart = globalClock.getTime(format='float')
        breakBetweenRepeats.status = STARTED
        thisExp.addData('breakBetweenRepeats.started', breakBetweenRepeats.tStart)
        breakBetweenRepeats.maxDuration = None
        # keep track of which components have finished
        breakBetweenRepeatsComponents = breakBetweenRepeats.components
        for thisComponent in breakBetweenRepeats.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "breakBetweenRepeats" ---
        # if trial has changed, end Routine now
        if isinstance(LearningSetThree, data.TrialHandler2) and thisLearningSetThree.thisN != LearningSetThree.thisTrial.thisN:
            continueRoutine = False
        breakBetweenRepeats.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *five_seconds* updates
            
            # if five_seconds is starting this frame...
            if five_seconds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                five_seconds.frameNStart = frameN  # exact frame index
                five_seconds.tStart = t  # local t and not account for scr refresh
                five_seconds.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(five_seconds, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'five_seconds.started')
                # update status
                five_seconds.status = STARTED
                five_seconds.setAutoDraw(True)
            
            # if five_seconds is active this frame...
            if five_seconds.status == STARTED:
                # update params
                pass
            
            # if five_seconds is stopping this frame...
            if five_seconds.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > five_seconds.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    five_seconds.tStop = t  # not accounting for scr refresh
                    five_seconds.tStopRefresh = tThisFlipGlobal  # on global time
                    five_seconds.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'five_seconds.stopped')
                    # update status
                    five_seconds.status = FINISHED
                    five_seconds.setAutoDraw(False)
            
            # *maybe_a_beep* updates
            
            # if maybe_a_beep is starting this frame...
            if maybe_a_beep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                maybe_a_beep.frameNStart = frameN  # exact frame index
                maybe_a_beep.tStart = t  # local t and not account for scr refresh
                maybe_a_beep.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('maybe_a_beep.started', tThisFlipGlobal)
                # update status
                maybe_a_beep.status = STARTED
                maybe_a_beep.play(when=win)  # sync with win flip
            
            # if maybe_a_beep is stopping this frame...
            if maybe_a_beep.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > maybe_a_beep.tStartRefresh + 1.0-frameTolerance or maybe_a_beep.isFinished:
                    # keep track of stop time/frame for later
                    maybe_a_beep.tStop = t  # not accounting for scr refresh
                    maybe_a_beep.tStopRefresh = tThisFlipGlobal  # on global time
                    maybe_a_beep.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'maybe_a_beep.stopped')
                    # update status
                    maybe_a_beep.status = FINISHED
                    maybe_a_beep.stop()
            
            # *debugging_press_enter_to_skip_5* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_5 is starting this frame...
            if debugging_press_enter_to_skip_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_5.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_5.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.started')
                # update status
                debugging_press_enter_to_skip_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if debugging_press_enter_to_skip_5 is stopping this frame...
            if debugging_press_enter_to_skip_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > debugging_press_enter_to_skip_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    debugging_press_enter_to_skip_5.tStop = t  # not accounting for scr refresh
                    debugging_press_enter_to_skip_5.tStopRefresh = tThisFlipGlobal  # on global time
                    debugging_press_enter_to_skip_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.stopped')
                    # update status
                    debugging_press_enter_to_skip_5.status = FINISHED
                    debugging_press_enter_to_skip_5.status = FINISHED
            if debugging_press_enter_to_skip_5.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_5.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_5_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_5_allKeys):
                    debugging_press_enter_to_skip_5.keys = _debugging_press_enter_to_skip_5_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_5.rt = _debugging_press_enter_to_skip_5_allKeys[-1].rt
                    debugging_press_enter_to_skip_5.duration = _debugging_press_enter_to_skip_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[maybe_a_beep]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                breakBetweenRepeats.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in breakBetweenRepeats.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "breakBetweenRepeats" ---
        for thisComponent in breakBetweenRepeats.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for breakBetweenRepeats
        breakBetweenRepeats.tStop = globalClock.getTime(format='float')
        breakBetweenRepeats.tStopRefresh = tThisFlipGlobal
        thisExp.addData('breakBetweenRepeats.stopped', breakBetweenRepeats.tStop)
        maybe_a_beep.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if debugging_press_enter_to_skip_5.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_5.keys = None
        LearningSetThree.addData('debugging_press_enter_to_skip_5.keys',debugging_press_enter_to_skip_5.keys)
        if debugging_press_enter_to_skip_5.keys != None:  # we had a response
            LearningSetThree.addData('debugging_press_enter_to_skip_5.rt', debugging_press_enter_to_skip_5.rt)
            LearningSetThree.addData('debugging_press_enter_to_skip_5.duration', debugging_press_enter_to_skip_5.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if breakBetweenRepeats.maxDurationReached:
            routineTimer.addTime(-breakBetweenRepeats.maxDuration)
        elif breakBetweenRepeats.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed numReps repeats of 'LearningSetThree'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "routine_30Seconds" ---
    # create an object to store info about Routine routine_30Seconds
    routine_30Seconds = data.Routine(
        name='routine_30Seconds',
        components=[thirtySeconds, debugging_press_enter_to_skip_6],
    )
    routine_30Seconds.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for debugging_press_enter_to_skip_6
    debugging_press_enter_to_skip_6.keys = []
    debugging_press_enter_to_skip_6.rt = []
    _debugging_press_enter_to_skip_6_allKeys = []
    # store start times for routine_30Seconds
    routine_30Seconds.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_30Seconds.tStart = globalClock.getTime(format='float')
    routine_30Seconds.status = STARTED
    thisExp.addData('routine_30Seconds.started', routine_30Seconds.tStart)
    routine_30Seconds.maxDuration = None
    # keep track of which components have finished
    routine_30SecondsComponents = routine_30Seconds.components
    for thisComponent in routine_30Seconds.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_30Seconds" ---
    routine_30Seconds.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thirtySeconds* updates
        
        # if thirtySeconds is starting this frame...
        if thirtySeconds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thirtySeconds.frameNStart = frameN  # exact frame index
            thirtySeconds.tStart = t  # local t and not account for scr refresh
            thirtySeconds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thirtySeconds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thirtySeconds.started')
            # update status
            thirtySeconds.status = STARTED
            thirtySeconds.setAutoDraw(True)
        
        # if thirtySeconds is active this frame...
        if thirtySeconds.status == STARTED:
            # update params
            pass
        
        # if thirtySeconds is stopping this frame...
        if thirtySeconds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > thirtySeconds.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                thirtySeconds.tStop = t  # not accounting for scr refresh
                thirtySeconds.tStopRefresh = tThisFlipGlobal  # on global time
                thirtySeconds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'thirtySeconds.stopped')
                # update status
                thirtySeconds.status = FINISHED
                thirtySeconds.setAutoDraw(False)
        
        # *debugging_press_enter_to_skip_6* updates
        waitOnFlip = False
        
        # if debugging_press_enter_to_skip_6 is starting this frame...
        if debugging_press_enter_to_skip_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debugging_press_enter_to_skip_6.frameNStart = frameN  # exact frame index
            debugging_press_enter_to_skip_6.tStart = t  # local t and not account for scr refresh
            debugging_press_enter_to_skip_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debugging_press_enter_to_skip_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_6.started')
            # update status
            debugging_press_enter_to_skip_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(debugging_press_enter_to_skip_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(debugging_press_enter_to_skip_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if debugging_press_enter_to_skip_6 is stopping this frame...
        if debugging_press_enter_to_skip_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > debugging_press_enter_to_skip_6.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                debugging_press_enter_to_skip_6.tStop = t  # not accounting for scr refresh
                debugging_press_enter_to_skip_6.tStopRefresh = tThisFlipGlobal  # on global time
                debugging_press_enter_to_skip_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_6.stopped')
                # update status
                debugging_press_enter_to_skip_6.status = FINISHED
                debugging_press_enter_to_skip_6.status = FINISHED
        if debugging_press_enter_to_skip_6.status == STARTED and not waitOnFlip:
            theseKeys = debugging_press_enter_to_skip_6.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _debugging_press_enter_to_skip_6_allKeys.extend(theseKeys)
            if len(_debugging_press_enter_to_skip_6_allKeys):
                debugging_press_enter_to_skip_6.keys = _debugging_press_enter_to_skip_6_allKeys[-1].name  # just the last key pressed
                debugging_press_enter_to_skip_6.rt = _debugging_press_enter_to_skip_6_allKeys[-1].rt
                debugging_press_enter_to_skip_6.duration = _debugging_press_enter_to_skip_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routine_30Seconds.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_30Seconds.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_30Seconds" ---
    for thisComponent in routine_30Seconds.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_30Seconds
    routine_30Seconds.tStop = globalClock.getTime(format='float')
    routine_30Seconds.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_30Seconds.stopped', routine_30Seconds.tStop)
    # check responses
    if debugging_press_enter_to_skip_6.keys in ['', [], None]:  # No response was made
        debugging_press_enter_to_skip_6.keys = None
    thisExp.addData('debugging_press_enter_to_skip_6.keys',debugging_press_enter_to_skip_6.keys)
    if debugging_press_enter_to_skip_6.keys != None:  # we had a response
        thisExp.addData('debugging_press_enter_to_skip_6.rt', debugging_press_enter_to_skip_6.rt)
        thisExp.addData('debugging_press_enter_to_skip_6.duration', debugging_press_enter_to_skip_6.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_30Seconds.maxDurationReached:
        routineTimer.addTime(-routine_30Seconds.maxDuration)
    elif routine_30Seconds.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "start_test" ---
    # create an object to store info about Routine start_test
    start_test = data.Routine(
        name='start_test',
        components=[textWelcome, key_resp_11],
    )
    start_test.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_11
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # store start times for start_test
    start_test.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    start_test.tStart = globalClock.getTime(format='float')
    start_test.status = STARTED
    thisExp.addData('start_test.started', start_test.tStart)
    start_test.maxDuration = None
    # keep track of which components have finished
    start_testComponents = start_test.components
    for thisComponent in start_test.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start_test" ---
    start_test.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        
        # if textWelcome is starting this frame...
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.started')
            # update status
            textWelcome.status = STARTED
            textWelcome.setAutoDraw(True)
        
        # if textWelcome is active this frame...
        if textWelcome.status == STARTED:
            # update params
            pass
        
        # *key_resp_11* updates
        waitOnFlip = False
        
        # if key_resp_11 is starting this frame...
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_11.started')
            # update status
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                key_resp_11.duration = _key_resp_11_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            start_test.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_test.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start_test" ---
    for thisComponent in start_test.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for start_test
    start_test.tStop = globalClock.getTime(format='float')
    start_test.tStopRefresh = tThisFlipGlobal
    thisExp.addData('start_test.stopped', start_test.tStop)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    thisExp.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        thisExp.addData('key_resp_11.rt', key_resp_11.rt)
        thisExp.addData('key_resp_11.duration', key_resp_11.duration)
    thisExp.nextEntry()
    # the Routine "start_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testSet3 = data.TrialHandler2(
        name='testSet3',
        nReps=12.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(testSet3)  # add the loop to the experiment
    thisTestSet3 = testSet3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestSet3.rgb)
    if thisTestSet3 != None:
        for paramName in thisTestSet3:
            globals()[paramName] = thisTestSet3[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTestSet3 in testSet3:
        currentLoop = testSet3
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTestSet3.rgb)
        if thisTestSet3 != None:
            for paramName in thisTestSet3:
                globals()[paramName] = thisTestSet3[paramName]
        
        # --- Prepare to start Routine "test3_NEW" ---
        # create an object to store info about Routine test3_NEW
        test3_NEW = data.Routine(
            name='test3_NEW',
            components=[textAmharic_7, textOptionA_7, textOptionB_7, textOptionC_7, textOptionD_7, textDiamond_6, key_resp_7, debugging_press_enter_to_skip_21],
        )
        test3_NEW.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeSymbol_7
        #incraments item counter by one
        curr_item3 += 1
        
        correct_word3 = word_list3[curr_item3] #THIS IS THE RIGHT ANSWER   
        amharic3 = amharic_list3[curr_item3]
        
        #preparing answer choices 
        lottery_list3 = []
        
        #add the right answer
        lottery_list3.append(correct_word3)
        
        #add 3 more non repeating answers
        copied_word3_list3 = []
        copied_word3_list3 = word_list3.copy() #copy word list
        copied_word3_list3.remove(correct_word3) #remove the right answer
        shuffle(copied_word3_list3) #shuffle up the copied list
        
        for x in range(0,3):    #add 3 from the shuffled list
            lottery_list3.append(copied_word3_list3[x])
        
        random.shuffle(lottery_list3)  #mix up the answer choices
        
        index_of_correct_answer3 = lottery_list3.index(correct_word3) #index of the correct word
        
        correctAns3 = index_to_button[index_of_correct_answer3] #correct answer in key form
        textAmharic_7.setText(amharic3)
        textOptionA_7.setText(lottery_list3[0]
        
        )
        textOptionB_7.setText(lottery_list3[1])
        textOptionC_7.setText(lottery_list3[2])
        textOptionD_7.setText(lottery_list3[3])
        textDiamond_6.setText(f"     {lottery_list3[0]}\n   {lottery_list3[1]}   {lottery_list3[2]}\n     {lottery_list3[3]}")
        # create starting attributes for key_resp_7
        key_resp_7.keys = []
        key_resp_7.rt = []
        _key_resp_7_allKeys = []
        # create starting attributes for debugging_press_enter_to_skip_21
        debugging_press_enter_to_skip_21.keys = []
        debugging_press_enter_to_skip_21.rt = []
        _debugging_press_enter_to_skip_21_allKeys = []
        # store start times for test3_NEW
        test3_NEW.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        test3_NEW.tStart = globalClock.getTime(format='float')
        test3_NEW.status = STARTED
        thisExp.addData('test3_NEW.started', test3_NEW.tStart)
        test3_NEW.maxDuration = None
        # keep track of which components have finished
        test3_NEWComponents = test3_NEW.components
        for thisComponent in test3_NEW.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test3_NEW" ---
        # if trial has changed, end Routine now
        if isinstance(testSet3, data.TrialHandler2) and thisTestSet3.thisN != testSet3.thisTrial.thisN:
            continueRoutine = False
        test3_NEW.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textAmharic_7* updates
            
            # if textAmharic_7 is starting this frame...
            if textAmharic_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textAmharic_7.frameNStart = frameN  # exact frame index
                textAmharic_7.tStart = t  # local t and not account for scr refresh
                textAmharic_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textAmharic_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textAmharic_7.started')
                # update status
                textAmharic_7.status = STARTED
                textAmharic_7.setAutoDraw(True)
            
            # if textAmharic_7 is active this frame...
            if textAmharic_7.status == STARTED:
                # update params
                pass
            
            # *textOptionA_7* updates
            
            # if textOptionA_7 is starting this frame...
            if textOptionA_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionA_7.frameNStart = frameN  # exact frame index
                textOptionA_7.tStart = t  # local t and not account for scr refresh
                textOptionA_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionA_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionA_7.started')
                # update status
                textOptionA_7.status = STARTED
                textOptionA_7.setAutoDraw(True)
            
            # if textOptionA_7 is active this frame...
            if textOptionA_7.status == STARTED:
                # update params
                pass
            
            # if textOptionA_7 is stopping this frame...
            if textOptionA_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionA_7.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionA_7.tStop = t  # not accounting for scr refresh
                    textOptionA_7.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionA_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionA_7.stopped')
                    # update status
                    textOptionA_7.status = FINISHED
                    textOptionA_7.setAutoDraw(False)
            
            # *textOptionB_7* updates
            
            # if textOptionB_7 is starting this frame...
            if textOptionB_7.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionB_7.frameNStart = frameN  # exact frame index
                textOptionB_7.tStart = t  # local t and not account for scr refresh
                textOptionB_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionB_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionB_7.started')
                # update status
                textOptionB_7.status = STARTED
                textOptionB_7.setAutoDraw(True)
            
            # if textOptionB_7 is active this frame...
            if textOptionB_7.status == STARTED:
                # update params
                pass
            
            # if textOptionB_7 is stopping this frame...
            if textOptionB_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionB_7.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionB_7.tStop = t  # not accounting for scr refresh
                    textOptionB_7.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionB_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionB_7.stopped')
                    # update status
                    textOptionB_7.status = FINISHED
                    textOptionB_7.setAutoDraw(False)
            
            # *textOptionC_7* updates
            
            # if textOptionC_7 is starting this frame...
            if textOptionC_7.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionC_7.frameNStart = frameN  # exact frame index
                textOptionC_7.tStart = t  # local t and not account for scr refresh
                textOptionC_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionC_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionC_7.started')
                # update status
                textOptionC_7.status = STARTED
                textOptionC_7.setAutoDraw(True)
            
            # if textOptionC_7 is active this frame...
            if textOptionC_7.status == STARTED:
                # update params
                pass
            
            # if textOptionC_7 is stopping this frame...
            if textOptionC_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionC_7.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionC_7.tStop = t  # not accounting for scr refresh
                    textOptionC_7.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionC_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionC_7.stopped')
                    # update status
                    textOptionC_7.status = FINISHED
                    textOptionC_7.setAutoDraw(False)
            
            # *textOptionD_7* updates
            
            # if textOptionD_7 is starting this frame...
            if textOptionD_7.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionD_7.frameNStart = frameN  # exact frame index
                textOptionD_7.tStart = t  # local t and not account for scr refresh
                textOptionD_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionD_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionD_7.started')
                # update status
                textOptionD_7.status = STARTED
                textOptionD_7.setAutoDraw(True)
            
            # if textOptionD_7 is active this frame...
            if textOptionD_7.status == STARTED:
                # update params
                pass
            
            # if textOptionD_7 is stopping this frame...
            if textOptionD_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionD_7.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionD_7.tStop = t  # not accounting for scr refresh
                    textOptionD_7.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionD_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionD_7.stopped')
                    # update status
                    textOptionD_7.status = FINISHED
                    textOptionD_7.setAutoDraw(False)
            
            # *textDiamond_6* updates
            
            # if textDiamond_6 is starting this frame...
            if textDiamond_6.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                textDiamond_6.frameNStart = frameN  # exact frame index
                textDiamond_6.tStart = t  # local t and not account for scr refresh
                textDiamond_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textDiamond_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textDiamond_6.started')
                # update status
                textDiamond_6.status = STARTED
                textDiamond_6.setAutoDraw(True)
            
            # if textDiamond_6 is active this frame...
            if textDiamond_6.status == STARTED:
                # update params
                pass
            
            # *key_resp_7* updates
            waitOnFlip = False
            
            # if key_resp_7 is starting this frame...
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_7.started')
                # update status
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['right','up','left','down', 'space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_7.keys == str(correctAns3)) or (key_resp_7.keys == correctAns3):
                        key_resp_7.corr = 1
                    else:
                        key_resp_7.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *debugging_press_enter_to_skip_21* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_21 is starting this frame...
            if debugging_press_enter_to_skip_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_21.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_21.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_21, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_21.started')
                # update status
                debugging_press_enter_to_skip_21.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_21.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_21.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if debugging_press_enter_to_skip_21.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_21.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_21_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_21_allKeys):
                    debugging_press_enter_to_skip_21.keys = _debugging_press_enter_to_skip_21_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_21.rt = _debugging_press_enter_to_skip_21_allKeys[-1].rt
                    debugging_press_enter_to_skip_21.duration = _debugging_press_enter_to_skip_21_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                test3_NEW.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test3_NEW.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test3_NEW" ---
        for thisComponent in test3_NEW.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for test3_NEW
        test3_NEW.tStop = globalClock.getTime(format='float')
        test3_NEW.tStopRefresh = tThisFlipGlobal
        thisExp.addData('test3_NEW.stopped', test3_NEW.tStop)
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
            # was no response the correct answer?!
            if str(correctAns3).lower() == 'none':
               key_resp_7.corr = 1;  # correct non-response
            else:
               key_resp_7.corr = 0;  # failed to respond (incorrectly)
        # store data for testSet3 (TrialHandler)
        testSet3.addData('key_resp_7.keys',key_resp_7.keys)
        testSet3.addData('key_resp_7.corr', key_resp_7.corr)
        if key_resp_7.keys != None:  # we had a response
            testSet3.addData('key_resp_7.rt', key_resp_7.rt)
            testSet3.addData('key_resp_7.duration', key_resp_7.duration)
        # check responses
        if debugging_press_enter_to_skip_21.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_21.keys = None
        testSet3.addData('debugging_press_enter_to_skip_21.keys',debugging_press_enter_to_skip_21.keys)
        if debugging_press_enter_to_skip_21.keys != None:  # we had a response
            testSet3.addData('debugging_press_enter_to_skip_21.rt', debugging_press_enter_to_skip_21.rt)
            testSet3.addData('debugging_press_enter_to_skip_21.duration', debugging_press_enter_to_skip_21.duration)
        # the Routine "test3_NEW" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "checkForCorr_3" ---
        # create an object to store info about Routine checkForCorr_3
        checkForCorr_3 = data.Routine(
            name='checkForCorr_3',
            components=[],
        )
        checkForCorr_3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_4
        if key_resp_7.corr == 1:
            checkmark_reps = 1
            xmark_reps = 0
        if key_resp_7.corr == 0:
            checkmark_reps = 0
            xmark_reps = 1
        # store start times for checkForCorr_3
        checkForCorr_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        checkForCorr_3.tStart = globalClock.getTime(format='float')
        checkForCorr_3.status = STARTED
        thisExp.addData('checkForCorr_3.started', checkForCorr_3.tStart)
        checkForCorr_3.maxDuration = None
        # keep track of which components have finished
        checkForCorr_3Components = checkForCorr_3.components
        for thisComponent in checkForCorr_3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "checkForCorr_3" ---
        # if trial has changed, end Routine now
        if isinstance(testSet3, data.TrialHandler2) and thisTestSet3.thisN != testSet3.thisTrial.thisN:
            continueRoutine = False
        checkForCorr_3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                checkForCorr_3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in checkForCorr_3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "checkForCorr_3" ---
        for thisComponent in checkForCorr_3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for checkForCorr_3
        checkForCorr_3.tStop = globalClock.getTime(format='float')
        checkForCorr_3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('checkForCorr_3.stopped', checkForCorr_3.tStop)
        # the Routine "checkForCorr_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        checkloops3 = data.TrialHandler2(
            name='checkloops3',
            nReps=checkmark_reps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(checkloops3)  # add the loop to the experiment
        thisCheckloops3 = checkloops3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisCheckloops3.rgb)
        if thisCheckloops3 != None:
            for paramName in thisCheckloops3:
                globals()[paramName] = thisCheckloops3[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisCheckloops3 in checkloops3:
            currentLoop = checkloops3
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisCheckloops3.rgb)
            if thisCheckloops3 != None:
                for paramName in thisCheckloops3:
                    globals()[paramName] = thisCheckloops3[paramName]
            
            # --- Prepare to start Routine "checkmark" ---
            # create an object to store info about Routine checkmark
            checkmark = data.Routine(
                name='checkmark',
                components=[textCheck, debugging_press_enter_to_skip_7],
            )
            checkmark.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textCheck.setText(markers[0])
            # create starting attributes for debugging_press_enter_to_skip_7
            debugging_press_enter_to_skip_7.keys = []
            debugging_press_enter_to_skip_7.rt = []
            _debugging_press_enter_to_skip_7_allKeys = []
            # store start times for checkmark
            checkmark.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            checkmark.tStart = globalClock.getTime(format='float')
            checkmark.status = STARTED
            thisExp.addData('checkmark.started', checkmark.tStart)
            checkmark.maxDuration = None
            # keep track of which components have finished
            checkmarkComponents = checkmark.components
            for thisComponent in checkmark.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "checkmark" ---
            # if trial has changed, end Routine now
            if isinstance(checkloops3, data.TrialHandler2) and thisCheckloops3.thisN != checkloops3.thisTrial.thisN:
                continueRoutine = False
            checkmark.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textCheck* updates
                
                # if textCheck is starting this frame...
                if textCheck.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textCheck.frameNStart = frameN  # exact frame index
                    textCheck.tStart = t  # local t and not account for scr refresh
                    textCheck.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textCheck, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textCheck.started')
                    # update status
                    textCheck.status = STARTED
                    textCheck.setAutoDraw(True)
                
                # if textCheck is active this frame...
                if textCheck.status == STARTED:
                    # update params
                    pass
                
                # if textCheck is stopping this frame...
                if textCheck.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textCheck.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textCheck.tStop = t  # not accounting for scr refresh
                        textCheck.tStopRefresh = tThisFlipGlobal  # on global time
                        textCheck.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textCheck.stopped')
                        # update status
                        textCheck.status = FINISHED
                        textCheck.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_7* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_7 is starting this frame...
                if debugging_press_enter_to_skip_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_7.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_7.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_7.started')
                    # update status
                    debugging_press_enter_to_skip_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_7.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_7 is stopping this frame...
                if debugging_press_enter_to_skip_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_7.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_7.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_7.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_7.stopped')
                        # update status
                        debugging_press_enter_to_skip_7.status = FINISHED
                        debugging_press_enter_to_skip_7.status = FINISHED
                if debugging_press_enter_to_skip_7.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_7.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_7_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_7_allKeys):
                        debugging_press_enter_to_skip_7.keys = _debugging_press_enter_to_skip_7_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_7.rt = _debugging_press_enter_to_skip_7_allKeys[-1].rt
                        debugging_press_enter_to_skip_7.duration = _debugging_press_enter_to_skip_7_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    checkmark.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in checkmark.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "checkmark" ---
            for thisComponent in checkmark.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for checkmark
            checkmark.tStop = globalClock.getTime(format='float')
            checkmark.tStopRefresh = tThisFlipGlobal
            thisExp.addData('checkmark.stopped', checkmark.tStop)
            # check responses
            if debugging_press_enter_to_skip_7.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_7.keys = None
            checkloops3.addData('debugging_press_enter_to_skip_7.keys',debugging_press_enter_to_skip_7.keys)
            if debugging_press_enter_to_skip_7.keys != None:  # we had a response
                checkloops3.addData('debugging_press_enter_to_skip_7.rt', debugging_press_enter_to_skip_7.rt)
                checkloops3.addData('debugging_press_enter_to_skip_7.duration', debugging_press_enter_to_skip_7.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if checkmark.maxDurationReached:
                routineTimer.addTime(-checkmark.maxDuration)
            elif checkmark.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed checkmark_reps repeats of 'checkloops3'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        xmarkloops3 = data.TrialHandler2(
            name='xmarkloops3',
            nReps=xmark_reps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(xmarkloops3)  # add the loop to the experiment
        thisXmarkloops3 = xmarkloops3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisXmarkloops3.rgb)
        if thisXmarkloops3 != None:
            for paramName in thisXmarkloops3:
                globals()[paramName] = thisXmarkloops3[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisXmarkloops3 in xmarkloops3:
            currentLoop = xmarkloops3
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisXmarkloops3.rgb)
            if thisXmarkloops3 != None:
                for paramName in thisXmarkloops3:
                    globals()[paramName] = thisXmarkloops3[paramName]
            
            # --- Prepare to start Routine "xmark" ---
            # create an object to store info about Routine xmark
            xmark = data.Routine(
                name='xmark',
                components=[textXmark, debugging_press_enter_to_skip_26],
            )
            xmark.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textXmark.setText(markers[1])
            # create starting attributes for debugging_press_enter_to_skip_26
            debugging_press_enter_to_skip_26.keys = []
            debugging_press_enter_to_skip_26.rt = []
            _debugging_press_enter_to_skip_26_allKeys = []
            # store start times for xmark
            xmark.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            xmark.tStart = globalClock.getTime(format='float')
            xmark.status = STARTED
            thisExp.addData('xmark.started', xmark.tStart)
            xmark.maxDuration = None
            # keep track of which components have finished
            xmarkComponents = xmark.components
            for thisComponent in xmark.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "xmark" ---
            # if trial has changed, end Routine now
            if isinstance(xmarkloops3, data.TrialHandler2) and thisXmarkloops3.thisN != xmarkloops3.thisTrial.thisN:
                continueRoutine = False
            xmark.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textXmark* updates
                
                # if textXmark is starting this frame...
                if textXmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textXmark.frameNStart = frameN  # exact frame index
                    textXmark.tStart = t  # local t and not account for scr refresh
                    textXmark.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textXmark, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textXmark.started')
                    # update status
                    textXmark.status = STARTED
                    textXmark.setAutoDraw(True)
                
                # if textXmark is active this frame...
                if textXmark.status == STARTED:
                    # update params
                    pass
                
                # if textXmark is stopping this frame...
                if textXmark.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textXmark.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textXmark.tStop = t  # not accounting for scr refresh
                        textXmark.tStopRefresh = tThisFlipGlobal  # on global time
                        textXmark.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textXmark.stopped')
                        # update status
                        textXmark.status = FINISHED
                        textXmark.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_26* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_26 is starting this frame...
                if debugging_press_enter_to_skip_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_26.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_26.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_26, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_26.started')
                    # update status
                    debugging_press_enter_to_skip_26.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_26.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_26 is stopping this frame...
                if debugging_press_enter_to_skip_26.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_26.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_26.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_26.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_26.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_26.stopped')
                        # update status
                        debugging_press_enter_to_skip_26.status = FINISHED
                        debugging_press_enter_to_skip_26.status = FINISHED
                if debugging_press_enter_to_skip_26.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_26.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_26_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_26_allKeys):
                        debugging_press_enter_to_skip_26.keys = _debugging_press_enter_to_skip_26_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_26.rt = _debugging_press_enter_to_skip_26_allKeys[-1].rt
                        debugging_press_enter_to_skip_26.duration = _debugging_press_enter_to_skip_26_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    xmark.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in xmark.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "xmark" ---
            for thisComponent in xmark.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for xmark
            xmark.tStop = globalClock.getTime(format='float')
            xmark.tStopRefresh = tThisFlipGlobal
            thisExp.addData('xmark.stopped', xmark.tStop)
            # check responses
            if debugging_press_enter_to_skip_26.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_26.keys = None
            xmarkloops3.addData('debugging_press_enter_to_skip_26.keys',debugging_press_enter_to_skip_26.keys)
            if debugging_press_enter_to_skip_26.keys != None:  # we had a response
                xmarkloops3.addData('debugging_press_enter_to_skip_26.rt', debugging_press_enter_to_skip_26.rt)
                xmarkloops3.addData('debugging_press_enter_to_skip_26.duration', debugging_press_enter_to_skip_26.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if xmark.maxDurationReached:
                routineTimer.addTime(-xmark.maxDuration)
            elif xmark.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed xmark_reps repeats of 'xmarkloops3'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "resetReps" ---
        # create an object to store info about Routine resetReps
        resetReps = data.Routine(
            name='resetReps',
            components=[],
        )
        resetReps.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for resetReps
        resetReps.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        resetReps.tStart = globalClock.getTime(format='float')
        resetReps.status = STARTED
        thisExp.addData('resetReps.started', resetReps.tStart)
        resetReps.maxDuration = None
        # keep track of which components have finished
        resetRepsComponents = resetReps.components
        for thisComponent in resetReps.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "resetReps" ---
        # if trial has changed, end Routine now
        if isinstance(testSet3, data.TrialHandler2) and thisTestSet3.thisN != testSet3.thisTrial.thisN:
            continueRoutine = False
        resetReps.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                resetReps.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in resetReps.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "resetReps" ---
        for thisComponent in resetReps.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for resetReps
        resetReps.tStop = globalClock.getTime(format='float')
        resetReps.tStopRefresh = tThisFlipGlobal
        thisExp.addData('resetReps.stopped', resetReps.tStop)
        # the Routine "resetReps" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        # create an object to store info about Routine blank500
        blank500 = data.Routine(
            name='blank500',
            components=[text_2, debugging_press_enter_to_skip_15],
        )
        blank500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_2.setText('')
        # create starting attributes for debugging_press_enter_to_skip_15
        debugging_press_enter_to_skip_15.keys = []
        debugging_press_enter_to_skip_15.rt = []
        _debugging_press_enter_to_skip_15_allKeys = []
        # store start times for blank500
        blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank500.tStart = globalClock.getTime(format='float')
        blank500.status = STARTED
        thisExp.addData('blank500.started', blank500.tStart)
        blank500.maxDuration = None
        # keep track of which components have finished
        blank500Components = blank500.components
        for thisComponent in blank500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        # if trial has changed, end Routine now
        if isinstance(testSet3, data.TrialHandler2) and thisTestSet3.thisN != testSet3.thisTrial.thisN:
            continueRoutine = False
        blank500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # *debugging_press_enter_to_skip_15* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_15 is starting this frame...
            if debugging_press_enter_to_skip_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_15.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_15.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_15.started')
                # update status
                debugging_press_enter_to_skip_15.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_15.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if debugging_press_enter_to_skip_15 is stopping this frame...
            if debugging_press_enter_to_skip_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > debugging_press_enter_to_skip_15.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    debugging_press_enter_to_skip_15.tStop = t  # not accounting for scr refresh
                    debugging_press_enter_to_skip_15.tStopRefresh = tThisFlipGlobal  # on global time
                    debugging_press_enter_to_skip_15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_15.stopped')
                    # update status
                    debugging_press_enter_to_skip_15.status = FINISHED
                    debugging_press_enter_to_skip_15.status = FINISHED
            if debugging_press_enter_to_skip_15.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_15.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_15_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_15_allKeys):
                    debugging_press_enter_to_skip_15.keys = _debugging_press_enter_to_skip_15_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_15.rt = _debugging_press_enter_to_skip_15_allKeys[-1].rt
                    debugging_press_enter_to_skip_15.duration = _debugging_press_enter_to_skip_15_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank500
        blank500.tStop = globalClock.getTime(format='float')
        blank500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank500.stopped', blank500.tStop)
        # check responses
        if debugging_press_enter_to_skip_15.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_15.keys = None
        testSet3.addData('debugging_press_enter_to_skip_15.keys',debugging_press_enter_to_skip_15.keys)
        if debugging_press_enter_to_skip_15.keys != None:  # we had a response
            testSet3.addData('debugging_press_enter_to_skip_15.rt', debugging_press_enter_to_skip_15.rt)
            testSet3.addData('debugging_press_enter_to_skip_15.duration', debugging_press_enter_to_skip_15.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank500.maxDurationReached:
            routineTimer.addTime(-blank500.maxDuration)
        elif blank500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed 12.0 repeats of 'testSet3'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "breakBetweenSets" ---
    # create an object to store info about Routine breakBetweenSets
    breakBetweenSets = data.Routine(
        name='breakBetweenSets',
        components=[cross, debugging_press_enter_to_skip_8],
    )
    breakBetweenSets.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for debugging_press_enter_to_skip_8
    debugging_press_enter_to_skip_8.keys = []
    debugging_press_enter_to_skip_8.rt = []
    _debugging_press_enter_to_skip_8_allKeys = []
    # store start times for breakBetweenSets
    breakBetweenSets.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    breakBetweenSets.tStart = globalClock.getTime(format='float')
    breakBetweenSets.status = STARTED
    thisExp.addData('breakBetweenSets.started', breakBetweenSets.tStart)
    breakBetweenSets.maxDuration = None
    # keep track of which components have finished
    breakBetweenSetsComponents = breakBetweenSets.components
    for thisComponent in breakBetweenSets.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "breakBetweenSets" ---
    breakBetweenSets.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.tStopRefresh = tThisFlipGlobal  # on global time
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # *debugging_press_enter_to_skip_8* updates
        waitOnFlip = False
        
        # if debugging_press_enter_to_skip_8 is starting this frame...
        if debugging_press_enter_to_skip_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debugging_press_enter_to_skip_8.frameNStart = frameN  # exact frame index
            debugging_press_enter_to_skip_8.tStart = t  # local t and not account for scr refresh
            debugging_press_enter_to_skip_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debugging_press_enter_to_skip_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_8.started')
            # update status
            debugging_press_enter_to_skip_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(debugging_press_enter_to_skip_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(debugging_press_enter_to_skip_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if debugging_press_enter_to_skip_8 is stopping this frame...
        if debugging_press_enter_to_skip_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > debugging_press_enter_to_skip_8.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                debugging_press_enter_to_skip_8.tStop = t  # not accounting for scr refresh
                debugging_press_enter_to_skip_8.tStopRefresh = tThisFlipGlobal  # on global time
                debugging_press_enter_to_skip_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_8.stopped')
                # update status
                debugging_press_enter_to_skip_8.status = FINISHED
                debugging_press_enter_to_skip_8.status = FINISHED
        if debugging_press_enter_to_skip_8.status == STARTED and not waitOnFlip:
            theseKeys = debugging_press_enter_to_skip_8.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _debugging_press_enter_to_skip_8_allKeys.extend(theseKeys)
            if len(_debugging_press_enter_to_skip_8_allKeys):
                debugging_press_enter_to_skip_8.keys = _debugging_press_enter_to_skip_8_allKeys[-1].name  # just the last key pressed
                debugging_press_enter_to_skip_8.rt = _debugging_press_enter_to_skip_8_allKeys[-1].rt
                debugging_press_enter_to_skip_8.duration = _debugging_press_enter_to_skip_8_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            breakBetweenSets.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breakBetweenSets.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "breakBetweenSets" ---
    for thisComponent in breakBetweenSets.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for breakBetweenSets
    breakBetweenSets.tStop = globalClock.getTime(format='float')
    breakBetweenSets.tStopRefresh = tThisFlipGlobal
    thisExp.addData('breakBetweenSets.stopped', breakBetweenSets.tStop)
    # check responses
    if debugging_press_enter_to_skip_8.keys in ['', [], None]:  # No response was made
        debugging_press_enter_to_skip_8.keys = None
    thisExp.addData('debugging_press_enter_to_skip_8.keys',debugging_press_enter_to_skip_8.keys)
    if debugging_press_enter_to_skip_8.keys != None:  # we had a response
        thisExp.addData('debugging_press_enter_to_skip_8.rt', debugging_press_enter_to_skip_8.rt)
        thisExp.addData('debugging_press_enter_to_skip_8.duration', debugging_press_enter_to_skip_8.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if breakBetweenSets.maxDurationReached:
        routineTimer.addTime(-breakBetweenSets.maxDuration)
    elif breakBetweenSets.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    LearningSetFour = data.TrialHandler2(
        name='LearningSetFour',
        nReps=numReps, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(LearningSetFour)  # add the loop to the experiment
    thisLearningSetFour = LearningSetFour.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLearningSetFour.rgb)
    if thisLearningSetFour != None:
        for paramName in thisLearningSetFour:
            globals()[paramName] = thisLearningSetFour[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLearningSetFour in LearningSetFour:
        currentLoop = LearningSetFour
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLearningSetFour.rgb)
        if thisLearningSetFour != None:
            for paramName in thisLearningSetFour:
                globals()[paramName] = thisLearningSetFour[paramName]
        
        # --- Prepare to start Routine "randomize_set" ---
        # create an object to store info about Routine randomize_set
        randomize_set = data.Routine(
            name='randomize_set',
            components=[],
        )
        randomize_set.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from randomize_learning_set
        keys = list(range(12))
        random.shuffle(keys)
        print("learning set order: " + str(keys))
        
        practice_keys = list(range(6))
        random.shuffle(practice_keys)
        print("learning set order: " + str(keys))
        
        practice_keys2 = list(range(6,12))
        random.shuffle(practice_keys2)
        print("learning set order: " + str(keys))
        # store start times for randomize_set
        randomize_set.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        randomize_set.tStart = globalClock.getTime(format='float')
        randomize_set.status = STARTED
        thisExp.addData('randomize_set.started', randomize_set.tStart)
        randomize_set.maxDuration = None
        # keep track of which components have finished
        randomize_setComponents = randomize_set.components
        for thisComponent in randomize_set.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "randomize_set" ---
        # if trial has changed, end Routine now
        if isinstance(LearningSetFour, data.TrialHandler2) and thisLearningSetFour.thisN != LearningSetFour.thisTrial.thisN:
            continueRoutine = False
        randomize_set.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                randomize_set.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in randomize_set.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "randomize_set" ---
        for thisComponent in randomize_set.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for randomize_set
        randomize_set.tStop = globalClock.getTime(format='float')
        randomize_set.tStopRefresh = tThisFlipGlobal
        thisExp.addData('randomize_set.stopped', randomize_set.tStop)
        # the Routine "randomize_set" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        setFour = data.TrialHandler2(
            name='setFour',
            nReps=12.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(setFour)  # add the loop to the experiment
        thisSetFour = setFour.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSetFour.rgb)
        if thisSetFour != None:
            for paramName in thisSetFour:
                globals()[paramName] = thisSetFour[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisSetFour in setFour:
            currentLoop = setFour
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisSetFour.rgb)
            if thisSetFour != None:
                for paramName in thisSetFour:
                    globals()[paramName] = thisSetFour[paramName]
            
            # --- Prepare to start Routine "Increment" ---
            # create an object to store info about Routine Increment
            Increment = data.Routine(
                name='Increment',
                components=[],
            )
            Increment.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from increment_index
            learning_index += 1
            learning_index %= len(keys)
            
            practice_index += 1
            practice_index %= len(practice_keys)
            # store start times for Increment
            Increment.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Increment.tStart = globalClock.getTime(format='float')
            Increment.status = STARTED
            thisExp.addData('Increment.started', Increment.tStart)
            Increment.maxDuration = None
            # keep track of which components have finished
            IncrementComponents = Increment.components
            for thisComponent in Increment.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Increment" ---
            # if trial has changed, end Routine now
            if isinstance(setFour, data.TrialHandler2) and thisSetFour.thisN != setFour.thisTrial.thisN:
                continueRoutine = False
            Increment.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Increment.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Increment.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Increment" ---
            for thisComponent in Increment.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Increment
            Increment.tStop = globalClock.getTime(format='float')
            Increment.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Increment.stopped', Increment.tStop)
            # the Routine "Increment" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            nreps_A4 = data.TrialHandler2(
                name='nreps_A4',
                nReps=nreps_A, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(nreps_A4)  # add the loop to the experiment
            thisNreps_A4 = nreps_A4.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisNreps_A4.rgb)
            if thisNreps_A4 != None:
                for paramName in thisNreps_A4:
                    globals()[paramName] = thisNreps_A4[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisNreps_A4 in nreps_A4:
                currentLoop = nreps_A4
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisNreps_A4.rgb)
                if thisNreps_A4 != None:
                    for paramName in thisNreps_A4:
                        globals()[paramName] = thisNreps_A4[paramName]
                
                # --- Prepare to start Routine "amharic4_A" ---
                # create an object to store info about Routine amharic4_A
                amharic4_A = data.Routine(
                    name='amharic4_A',
                    components=[amharics4, words4_image, debugging_press_enter_to_skip_13],
                )
                amharic4_A.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                amharics4.setText(amharic_word_list4[keys[learning_index]][0])
                words4_image.setImage(amharic_word_list4[keys[learning_index]][2])
                # Run 'Begin Routine' code from code4
                print("Index: " + str(keys[learning_index]) + 
                      "\n Character: " + str(amharic_word_list4[keys[learning_index]][0]) + 
                      "\n Meaning: " + str(amharic_word_list4[keys[learning_index]][1]) + 
                      "\n Image Path: " + str(amharic_word_list4[keys[learning_index]][2]))
                # create starting attributes for debugging_press_enter_to_skip_13
                debugging_press_enter_to_skip_13.keys = []
                debugging_press_enter_to_skip_13.rt = []
                _debugging_press_enter_to_skip_13_allKeys = []
                # store start times for amharic4_A
                amharic4_A.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                amharic4_A.tStart = globalClock.getTime(format='float')
                amharic4_A.status = STARTED
                thisExp.addData('amharic4_A.started', amharic4_A.tStart)
                amharic4_A.maxDuration = None
                # keep track of which components have finished
                amharic4_AComponents = amharic4_A.components
                for thisComponent in amharic4_A.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "amharic4_A" ---
                # if trial has changed, end Routine now
                if isinstance(nreps_A4, data.TrialHandler2) and thisNreps_A4.thisN != nreps_A4.thisTrial.thisN:
                    continueRoutine = False
                amharic4_A.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *amharics4* updates
                    
                    # if amharics4 is starting this frame...
                    if amharics4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        amharics4.frameNStart = frameN  # exact frame index
                        amharics4.tStart = t  # local t and not account for scr refresh
                        amharics4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(amharics4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'amharics4.started')
                        # update status
                        amharics4.status = STARTED
                        amharics4.setAutoDraw(True)
                    
                    # if amharics4 is active this frame...
                    if amharics4.status == STARTED:
                        # update params
                        pass
                    
                    # if amharics4 is stopping this frame...
                    if amharics4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > amharics4.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            amharics4.tStop = t  # not accounting for scr refresh
                            amharics4.tStopRefresh = tThisFlipGlobal  # on global time
                            amharics4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'amharics4.stopped')
                            # update status
                            amharics4.status = FINISHED
                            amharics4.setAutoDraw(False)
                    
                    # *words4_image* updates
                    
                    # if words4_image is starting this frame...
                    if words4_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        words4_image.frameNStart = frameN  # exact frame index
                        words4_image.tStart = t  # local t and not account for scr refresh
                        words4_image.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(words4_image, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'words4_image.started')
                        # update status
                        words4_image.status = STARTED
                        words4_image.setAutoDraw(True)
                    
                    # if words4_image is active this frame...
                    if words4_image.status == STARTED:
                        # update params
                        pass
                    
                    # if words4_image is stopping this frame...
                    if words4_image.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > words4_image.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            words4_image.tStop = t  # not accounting for scr refresh
                            words4_image.tStopRefresh = tThisFlipGlobal  # on global time
                            words4_image.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'words4_image.stopped')
                            # update status
                            words4_image.status = FINISHED
                            words4_image.setAutoDraw(False)
                    
                    # *debugging_press_enter_to_skip_13* updates
                    waitOnFlip = False
                    
                    # if debugging_press_enter_to_skip_13 is starting this frame...
                    if debugging_press_enter_to_skip_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        debugging_press_enter_to_skip_13.frameNStart = frameN  # exact frame index
                        debugging_press_enter_to_skip_13.tStart = t  # local t and not account for scr refresh
                        debugging_press_enter_to_skip_13.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(debugging_press_enter_to_skip_13, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_13.started')
                        # update status
                        debugging_press_enter_to_skip_13.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(debugging_press_enter_to_skip_13.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(debugging_press_enter_to_skip_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if debugging_press_enter_to_skip_13 is stopping this frame...
                    if debugging_press_enter_to_skip_13.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > debugging_press_enter_to_skip_13.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            debugging_press_enter_to_skip_13.tStop = t  # not accounting for scr refresh
                            debugging_press_enter_to_skip_13.tStopRefresh = tThisFlipGlobal  # on global time
                            debugging_press_enter_to_skip_13.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_13.stopped')
                            # update status
                            debugging_press_enter_to_skip_13.status = FINISHED
                            debugging_press_enter_to_skip_13.status = FINISHED
                    if debugging_press_enter_to_skip_13.status == STARTED and not waitOnFlip:
                        theseKeys = debugging_press_enter_to_skip_13.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                        _debugging_press_enter_to_skip_13_allKeys.extend(theseKeys)
                        if len(_debugging_press_enter_to_skip_13_allKeys):
                            debugging_press_enter_to_skip_13.keys = _debugging_press_enter_to_skip_13_allKeys[-1].name  # just the last key pressed
                            debugging_press_enter_to_skip_13.rt = _debugging_press_enter_to_skip_13_allKeys[-1].rt
                            debugging_press_enter_to_skip_13.duration = _debugging_press_enter_to_skip_13_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        amharic4_A.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in amharic4_A.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "amharic4_A" ---
                for thisComponent in amharic4_A.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for amharic4_A
                amharic4_A.tStop = globalClock.getTime(format='float')
                amharic4_A.tStopRefresh = tThisFlipGlobal
                thisExp.addData('amharic4_A.stopped', amharic4_A.tStop)
                # check responses
                if debugging_press_enter_to_skip_13.keys in ['', [], None]:  # No response was made
                    debugging_press_enter_to_skip_13.keys = None
                nreps_A4.addData('debugging_press_enter_to_skip_13.keys',debugging_press_enter_to_skip_13.keys)
                if debugging_press_enter_to_skip_13.keys != None:  # we had a response
                    nreps_A4.addData('debugging_press_enter_to_skip_13.rt', debugging_press_enter_to_skip_13.rt)
                    nreps_A4.addData('debugging_press_enter_to_skip_13.duration', debugging_press_enter_to_skip_13.duration)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if amharic4_A.maxDurationReached:
                    routineTimer.addTime(-amharic4_A.maxDuration)
                elif amharic4_A.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
            # completed nreps_A repeats of 'nreps_A4'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # set up handler to look after randomisation of conditions etc
            nreps_B4 = data.TrialHandler2(
                name='nreps_B4',
                nReps=nreps_B, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(nreps_B4)  # add the loop to the experiment
            thisNreps_B4 = nreps_B4.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisNreps_B4.rgb)
            if thisNreps_B4 != None:
                for paramName in thisNreps_B4:
                    globals()[paramName] = thisNreps_B4[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisNreps_B4 in nreps_B4:
                currentLoop = nreps_B4
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisNreps_B4.rgb)
                if thisNreps_B4 != None:
                    for paramName in thisNreps_B4:
                        globals()[paramName] = thisNreps_B4[paramName]
                
                # --- Prepare to start Routine "amharic4_B" ---
                # create an object to store info about Routine amharic4_B
                amharic4_B = data.Routine(
                    name='amharic4_B',
                    components=[amharics4_2, words4_2, debugging_press_enter_to_skip_14],
                )
                amharic4_B.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                amharics4_2.setText(amharic_word_list4[keys[learning_index]][0])
                words4_2.setText(amharic_word_list4[keys[learning_index]][1])
                # Run 'Begin Routine' code from code4_2
                print("Index: " + str(keys[learning_index]) + 
                      "\n Character: " + str(amharic_word_list4[keys[learning_index]][0]) + 
                      "\n Meaning: " + str(amharic_word_list4[keys[learning_index]][1]) + 
                      "\n Image Path: " + str(amharic_word_list4[keys[learning_index]][2]))
                # create starting attributes for debugging_press_enter_to_skip_14
                debugging_press_enter_to_skip_14.keys = []
                debugging_press_enter_to_skip_14.rt = []
                _debugging_press_enter_to_skip_14_allKeys = []
                # store start times for amharic4_B
                amharic4_B.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                amharic4_B.tStart = globalClock.getTime(format='float')
                amharic4_B.status = STARTED
                thisExp.addData('amharic4_B.started', amharic4_B.tStart)
                amharic4_B.maxDuration = None
                # keep track of which components have finished
                amharic4_BComponents = amharic4_B.components
                for thisComponent in amharic4_B.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "amharic4_B" ---
                # if trial has changed, end Routine now
                if isinstance(nreps_B4, data.TrialHandler2) and thisNreps_B4.thisN != nreps_B4.thisTrial.thisN:
                    continueRoutine = False
                amharic4_B.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *amharics4_2* updates
                    
                    # if amharics4_2 is starting this frame...
                    if amharics4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        amharics4_2.frameNStart = frameN  # exact frame index
                        amharics4_2.tStart = t  # local t and not account for scr refresh
                        amharics4_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(amharics4_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'amharics4_2.started')
                        # update status
                        amharics4_2.status = STARTED
                        amharics4_2.setAutoDraw(True)
                    
                    # if amharics4_2 is active this frame...
                    if amharics4_2.status == STARTED:
                        # update params
                        pass
                    
                    # if amharics4_2 is stopping this frame...
                    if amharics4_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > amharics4_2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            amharics4_2.tStop = t  # not accounting for scr refresh
                            amharics4_2.tStopRefresh = tThisFlipGlobal  # on global time
                            amharics4_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'amharics4_2.stopped')
                            # update status
                            amharics4_2.status = FINISHED
                            amharics4_2.setAutoDraw(False)
                    
                    # *words4_2* updates
                    
                    # if words4_2 is starting this frame...
                    if words4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        words4_2.frameNStart = frameN  # exact frame index
                        words4_2.tStart = t  # local t and not account for scr refresh
                        words4_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(words4_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'words4_2.started')
                        # update status
                        words4_2.status = STARTED
                        words4_2.setAutoDraw(True)
                    
                    # if words4_2 is active this frame...
                    if words4_2.status == STARTED:
                        # update params
                        pass
                    
                    # if words4_2 is stopping this frame...
                    if words4_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > words4_2.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            words4_2.tStop = t  # not accounting for scr refresh
                            words4_2.tStopRefresh = tThisFlipGlobal  # on global time
                            words4_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'words4_2.stopped')
                            # update status
                            words4_2.status = FINISHED
                            words4_2.setAutoDraw(False)
                    
                    # *debugging_press_enter_to_skip_14* updates
                    waitOnFlip = False
                    
                    # if debugging_press_enter_to_skip_14 is starting this frame...
                    if debugging_press_enter_to_skip_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        debugging_press_enter_to_skip_14.frameNStart = frameN  # exact frame index
                        debugging_press_enter_to_skip_14.tStart = t  # local t and not account for scr refresh
                        debugging_press_enter_to_skip_14.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(debugging_press_enter_to_skip_14, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_14.started')
                        # update status
                        debugging_press_enter_to_skip_14.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(debugging_press_enter_to_skip_14.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(debugging_press_enter_to_skip_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if debugging_press_enter_to_skip_14 is stopping this frame...
                    if debugging_press_enter_to_skip_14.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > debugging_press_enter_to_skip_14.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            debugging_press_enter_to_skip_14.tStop = t  # not accounting for scr refresh
                            debugging_press_enter_to_skip_14.tStopRefresh = tThisFlipGlobal  # on global time
                            debugging_press_enter_to_skip_14.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_14.stopped')
                            # update status
                            debugging_press_enter_to_skip_14.status = FINISHED
                            debugging_press_enter_to_skip_14.status = FINISHED
                    if debugging_press_enter_to_skip_14.status == STARTED and not waitOnFlip:
                        theseKeys = debugging_press_enter_to_skip_14.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                        _debugging_press_enter_to_skip_14_allKeys.extend(theseKeys)
                        if len(_debugging_press_enter_to_skip_14_allKeys):
                            debugging_press_enter_to_skip_14.keys = _debugging_press_enter_to_skip_14_allKeys[-1].name  # just the last key pressed
                            debugging_press_enter_to_skip_14.rt = _debugging_press_enter_to_skip_14_allKeys[-1].rt
                            debugging_press_enter_to_skip_14.duration = _debugging_press_enter_to_skip_14_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        amharic4_B.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in amharic4_B.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "amharic4_B" ---
                for thisComponent in amharic4_B.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for amharic4_B
                amharic4_B.tStop = globalClock.getTime(format='float')
                amharic4_B.tStopRefresh = tThisFlipGlobal
                thisExp.addData('amharic4_B.stopped', amharic4_B.tStop)
                # check responses
                if debugging_press_enter_to_skip_14.keys in ['', [], None]:  # No response was made
                    debugging_press_enter_to_skip_14.keys = None
                nreps_B4.addData('debugging_press_enter_to_skip_14.keys',debugging_press_enter_to_skip_14.keys)
                if debugging_press_enter_to_skip_14.keys != None:  # we had a response
                    nreps_B4.addData('debugging_press_enter_to_skip_14.rt', debugging_press_enter_to_skip_14.rt)
                    nreps_B4.addData('debugging_press_enter_to_skip_14.duration', debugging_press_enter_to_skip_14.duration)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if amharic4_B.maxDurationReached:
                    routineTimer.addTime(-amharic4_B.maxDuration)
                elif amharic4_B.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
            # completed nreps_B repeats of 'nreps_B4'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # --- Prepare to start Routine "plusBetween" ---
            # create an object to store info about Routine plusBetween
            plusBetween = data.Routine(
                name='plusBetween',
                components=[plus, debugging_press_enter_to_skip_4],
            )
            plusBetween.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            plus.setText('+')
            # create starting attributes for debugging_press_enter_to_skip_4
            debugging_press_enter_to_skip_4.keys = []
            debugging_press_enter_to_skip_4.rt = []
            _debugging_press_enter_to_skip_4_allKeys = []
            # store start times for plusBetween
            plusBetween.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            plusBetween.tStart = globalClock.getTime(format='float')
            plusBetween.status = STARTED
            thisExp.addData('plusBetween.started', plusBetween.tStart)
            plusBetween.maxDuration = None
            # keep track of which components have finished
            plusBetweenComponents = plusBetween.components
            for thisComponent in plusBetween.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "plusBetween" ---
            # if trial has changed, end Routine now
            if isinstance(setFour, data.TrialHandler2) and thisSetFour.thisN != setFour.thisTrial.thisN:
                continueRoutine = False
            plusBetween.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *plus* updates
                
                # if plus is starting this frame...
                if plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    plus.frameNStart = frameN  # exact frame index
                    plus.tStart = t  # local t and not account for scr refresh
                    plus.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(plus, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'plus.started')
                    # update status
                    plus.status = STARTED
                    plus.setAutoDraw(True)
                
                # if plus is active this frame...
                if plus.status == STARTED:
                    # update params
                    pass
                
                # if plus is stopping this frame...
                if plus.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > plus.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        plus.tStop = t  # not accounting for scr refresh
                        plus.tStopRefresh = tThisFlipGlobal  # on global time
                        plus.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'plus.stopped')
                        # update status
                        plus.status = FINISHED
                        plus.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_4* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_4 is starting this frame...
                if debugging_press_enter_to_skip_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_4.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_4.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.started')
                    # update status
                    debugging_press_enter_to_skip_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_4.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_4 is stopping this frame...
                if debugging_press_enter_to_skip_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_4.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_4.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_4.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_4.stopped')
                        # update status
                        debugging_press_enter_to_skip_4.status = FINISHED
                        debugging_press_enter_to_skip_4.status = FINISHED
                if debugging_press_enter_to_skip_4.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_4.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_4_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_4_allKeys):
                        debugging_press_enter_to_skip_4.keys = _debugging_press_enter_to_skip_4_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_4.rt = _debugging_press_enter_to_skip_4_allKeys[-1].rt
                        debugging_press_enter_to_skip_4.duration = _debugging_press_enter_to_skip_4_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    plusBetween.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in plusBetween.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "plusBetween" ---
            for thisComponent in plusBetween.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for plusBetween
            plusBetween.tStop = globalClock.getTime(format='float')
            plusBetween.tStopRefresh = tThisFlipGlobal
            thisExp.addData('plusBetween.stopped', plusBetween.tStop)
            # check responses
            if debugging_press_enter_to_skip_4.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_4.keys = None
            setFour.addData('debugging_press_enter_to_skip_4.keys',debugging_press_enter_to_skip_4.keys)
            if debugging_press_enter_to_skip_4.keys != None:  # we had a response
                setFour.addData('debugging_press_enter_to_skip_4.rt', debugging_press_enter_to_skip_4.rt)
                setFour.addData('debugging_press_enter_to_skip_4.duration', debugging_press_enter_to_skip_4.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if plusBetween.maxDurationReached:
                routineTimer.addTime(-plusBetween.maxDuration)
            elif plusBetween.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 12.0 repeats of 'setFour'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "breakBetweenRepeats" ---
        # create an object to store info about Routine breakBetweenRepeats
        breakBetweenRepeats = data.Routine(
            name='breakBetweenRepeats',
            components=[five_seconds, maybe_a_beep, debugging_press_enter_to_skip_5],
        )
        breakBetweenRepeats.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        maybe_a_beep.setSound('A', secs=1.0, hamming=True)
        maybe_a_beep.setVolume(1.0, log=False)
        maybe_a_beep.seek(0)
        # create starting attributes for debugging_press_enter_to_skip_5
        debugging_press_enter_to_skip_5.keys = []
        debugging_press_enter_to_skip_5.rt = []
        _debugging_press_enter_to_skip_5_allKeys = []
        # store start times for breakBetweenRepeats
        breakBetweenRepeats.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        breakBetweenRepeats.tStart = globalClock.getTime(format='float')
        breakBetweenRepeats.status = STARTED
        thisExp.addData('breakBetweenRepeats.started', breakBetweenRepeats.tStart)
        breakBetweenRepeats.maxDuration = None
        # keep track of which components have finished
        breakBetweenRepeatsComponents = breakBetweenRepeats.components
        for thisComponent in breakBetweenRepeats.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "breakBetweenRepeats" ---
        # if trial has changed, end Routine now
        if isinstance(LearningSetFour, data.TrialHandler2) and thisLearningSetFour.thisN != LearningSetFour.thisTrial.thisN:
            continueRoutine = False
        breakBetweenRepeats.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *five_seconds* updates
            
            # if five_seconds is starting this frame...
            if five_seconds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                five_seconds.frameNStart = frameN  # exact frame index
                five_seconds.tStart = t  # local t and not account for scr refresh
                five_seconds.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(five_seconds, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'five_seconds.started')
                # update status
                five_seconds.status = STARTED
                five_seconds.setAutoDraw(True)
            
            # if five_seconds is active this frame...
            if five_seconds.status == STARTED:
                # update params
                pass
            
            # if five_seconds is stopping this frame...
            if five_seconds.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > five_seconds.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    five_seconds.tStop = t  # not accounting for scr refresh
                    five_seconds.tStopRefresh = tThisFlipGlobal  # on global time
                    five_seconds.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'five_seconds.stopped')
                    # update status
                    five_seconds.status = FINISHED
                    five_seconds.setAutoDraw(False)
            
            # *maybe_a_beep* updates
            
            # if maybe_a_beep is starting this frame...
            if maybe_a_beep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                maybe_a_beep.frameNStart = frameN  # exact frame index
                maybe_a_beep.tStart = t  # local t and not account for scr refresh
                maybe_a_beep.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('maybe_a_beep.started', tThisFlipGlobal)
                # update status
                maybe_a_beep.status = STARTED
                maybe_a_beep.play(when=win)  # sync with win flip
            
            # if maybe_a_beep is stopping this frame...
            if maybe_a_beep.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > maybe_a_beep.tStartRefresh + 1.0-frameTolerance or maybe_a_beep.isFinished:
                    # keep track of stop time/frame for later
                    maybe_a_beep.tStop = t  # not accounting for scr refresh
                    maybe_a_beep.tStopRefresh = tThisFlipGlobal  # on global time
                    maybe_a_beep.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'maybe_a_beep.stopped')
                    # update status
                    maybe_a_beep.status = FINISHED
                    maybe_a_beep.stop()
            
            # *debugging_press_enter_to_skip_5* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_5 is starting this frame...
            if debugging_press_enter_to_skip_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_5.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_5.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.started')
                # update status
                debugging_press_enter_to_skip_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if debugging_press_enter_to_skip_5 is stopping this frame...
            if debugging_press_enter_to_skip_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > debugging_press_enter_to_skip_5.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    debugging_press_enter_to_skip_5.tStop = t  # not accounting for scr refresh
                    debugging_press_enter_to_skip_5.tStopRefresh = tThisFlipGlobal  # on global time
                    debugging_press_enter_to_skip_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_5.stopped')
                    # update status
                    debugging_press_enter_to_skip_5.status = FINISHED
                    debugging_press_enter_to_skip_5.status = FINISHED
            if debugging_press_enter_to_skip_5.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_5.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_5_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_5_allKeys):
                    debugging_press_enter_to_skip_5.keys = _debugging_press_enter_to_skip_5_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_5.rt = _debugging_press_enter_to_skip_5_allKeys[-1].rt
                    debugging_press_enter_to_skip_5.duration = _debugging_press_enter_to_skip_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[maybe_a_beep]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                breakBetweenRepeats.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in breakBetweenRepeats.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "breakBetweenRepeats" ---
        for thisComponent in breakBetweenRepeats.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for breakBetweenRepeats
        breakBetweenRepeats.tStop = globalClock.getTime(format='float')
        breakBetweenRepeats.tStopRefresh = tThisFlipGlobal
        thisExp.addData('breakBetweenRepeats.stopped', breakBetweenRepeats.tStop)
        maybe_a_beep.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if debugging_press_enter_to_skip_5.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_5.keys = None
        LearningSetFour.addData('debugging_press_enter_to_skip_5.keys',debugging_press_enter_to_skip_5.keys)
        if debugging_press_enter_to_skip_5.keys != None:  # we had a response
            LearningSetFour.addData('debugging_press_enter_to_skip_5.rt', debugging_press_enter_to_skip_5.rt)
            LearningSetFour.addData('debugging_press_enter_to_skip_5.duration', debugging_press_enter_to_skip_5.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if breakBetweenRepeats.maxDurationReached:
            routineTimer.addTime(-breakBetweenRepeats.maxDuration)
        elif breakBetweenRepeats.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed numReps repeats of 'LearningSetFour'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "routine_30Seconds" ---
    # create an object to store info about Routine routine_30Seconds
    routine_30Seconds = data.Routine(
        name='routine_30Seconds',
        components=[thirtySeconds, debugging_press_enter_to_skip_6],
    )
    routine_30Seconds.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for debugging_press_enter_to_skip_6
    debugging_press_enter_to_skip_6.keys = []
    debugging_press_enter_to_skip_6.rt = []
    _debugging_press_enter_to_skip_6_allKeys = []
    # store start times for routine_30Seconds
    routine_30Seconds.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    routine_30Seconds.tStart = globalClock.getTime(format='float')
    routine_30Seconds.status = STARTED
    thisExp.addData('routine_30Seconds.started', routine_30Seconds.tStart)
    routine_30Seconds.maxDuration = None
    # keep track of which components have finished
    routine_30SecondsComponents = routine_30Seconds.components
    for thisComponent in routine_30Seconds.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_30Seconds" ---
    routine_30Seconds.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thirtySeconds* updates
        
        # if thirtySeconds is starting this frame...
        if thirtySeconds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thirtySeconds.frameNStart = frameN  # exact frame index
            thirtySeconds.tStart = t  # local t and not account for scr refresh
            thirtySeconds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thirtySeconds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thirtySeconds.started')
            # update status
            thirtySeconds.status = STARTED
            thirtySeconds.setAutoDraw(True)
        
        # if thirtySeconds is active this frame...
        if thirtySeconds.status == STARTED:
            # update params
            pass
        
        # if thirtySeconds is stopping this frame...
        if thirtySeconds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > thirtySeconds.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                thirtySeconds.tStop = t  # not accounting for scr refresh
                thirtySeconds.tStopRefresh = tThisFlipGlobal  # on global time
                thirtySeconds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'thirtySeconds.stopped')
                # update status
                thirtySeconds.status = FINISHED
                thirtySeconds.setAutoDraw(False)
        
        # *debugging_press_enter_to_skip_6* updates
        waitOnFlip = False
        
        # if debugging_press_enter_to_skip_6 is starting this frame...
        if debugging_press_enter_to_skip_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debugging_press_enter_to_skip_6.frameNStart = frameN  # exact frame index
            debugging_press_enter_to_skip_6.tStart = t  # local t and not account for scr refresh
            debugging_press_enter_to_skip_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debugging_press_enter_to_skip_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_6.started')
            # update status
            debugging_press_enter_to_skip_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(debugging_press_enter_to_skip_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(debugging_press_enter_to_skip_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if debugging_press_enter_to_skip_6 is stopping this frame...
        if debugging_press_enter_to_skip_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > debugging_press_enter_to_skip_6.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                debugging_press_enter_to_skip_6.tStop = t  # not accounting for scr refresh
                debugging_press_enter_to_skip_6.tStopRefresh = tThisFlipGlobal  # on global time
                debugging_press_enter_to_skip_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_6.stopped')
                # update status
                debugging_press_enter_to_skip_6.status = FINISHED
                debugging_press_enter_to_skip_6.status = FINISHED
        if debugging_press_enter_to_skip_6.status == STARTED and not waitOnFlip:
            theseKeys = debugging_press_enter_to_skip_6.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _debugging_press_enter_to_skip_6_allKeys.extend(theseKeys)
            if len(_debugging_press_enter_to_skip_6_allKeys):
                debugging_press_enter_to_skip_6.keys = _debugging_press_enter_to_skip_6_allKeys[-1].name  # just the last key pressed
                debugging_press_enter_to_skip_6.rt = _debugging_press_enter_to_skip_6_allKeys[-1].rt
                debugging_press_enter_to_skip_6.duration = _debugging_press_enter_to_skip_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routine_30Seconds.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_30Seconds.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_30Seconds" ---
    for thisComponent in routine_30Seconds.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for routine_30Seconds
    routine_30Seconds.tStop = globalClock.getTime(format='float')
    routine_30Seconds.tStopRefresh = tThisFlipGlobal
    thisExp.addData('routine_30Seconds.stopped', routine_30Seconds.tStop)
    # check responses
    if debugging_press_enter_to_skip_6.keys in ['', [], None]:  # No response was made
        debugging_press_enter_to_skip_6.keys = None
    thisExp.addData('debugging_press_enter_to_skip_6.keys',debugging_press_enter_to_skip_6.keys)
    if debugging_press_enter_to_skip_6.keys != None:  # we had a response
        thisExp.addData('debugging_press_enter_to_skip_6.rt', debugging_press_enter_to_skip_6.rt)
        thisExp.addData('debugging_press_enter_to_skip_6.duration', debugging_press_enter_to_skip_6.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routine_30Seconds.maxDurationReached:
        routineTimer.addTime(-routine_30Seconds.maxDuration)
    elif routine_30Seconds.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "start_test" ---
    # create an object to store info about Routine start_test
    start_test = data.Routine(
        name='start_test',
        components=[textWelcome, key_resp_11],
    )
    start_test.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_11
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # store start times for start_test
    start_test.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    start_test.tStart = globalClock.getTime(format='float')
    start_test.status = STARTED
    thisExp.addData('start_test.started', start_test.tStart)
    start_test.maxDuration = None
    # keep track of which components have finished
    start_testComponents = start_test.components
    for thisComponent in start_test.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start_test" ---
    start_test.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        
        # if textWelcome is starting this frame...
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.started')
            # update status
            textWelcome.status = STARTED
            textWelcome.setAutoDraw(True)
        
        # if textWelcome is active this frame...
        if textWelcome.status == STARTED:
            # update params
            pass
        
        # *key_resp_11* updates
        waitOnFlip = False
        
        # if key_resp_11 is starting this frame...
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_11.started')
            # update status
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                key_resp_11.duration = _key_resp_11_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            start_test.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_test.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start_test" ---
    for thisComponent in start_test.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for start_test
    start_test.tStop = globalClock.getTime(format='float')
    start_test.tStopRefresh = tThisFlipGlobal
    thisExp.addData('start_test.stopped', start_test.tStop)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    thisExp.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        thisExp.addData('key_resp_11.rt', key_resp_11.rt)
        thisExp.addData('key_resp_11.duration', key_resp_11.duration)
    thisExp.nextEntry()
    # the Routine "start_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testSet4 = data.TrialHandler2(
        name='testSet4',
        nReps=12.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(testSet4)  # add the loop to the experiment
    thisTestSet4 = testSet4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestSet4.rgb)
    if thisTestSet4 != None:
        for paramName in thisTestSet4:
            globals()[paramName] = thisTestSet4[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTestSet4 in testSet4:
        currentLoop = testSet4
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTestSet4.rgb)
        if thisTestSet4 != None:
            for paramName in thisTestSet4:
                globals()[paramName] = thisTestSet4[paramName]
        
        # --- Prepare to start Routine "test4_NEW" ---
        # create an object to store info about Routine test4_NEW
        test4_NEW = data.Routine(
            name='test4_NEW',
            components=[textAmharic_8, textOptionA_8, textOptionB_8, textOptionC_8, textOptionD_8, textDiamond_7, key_resp_8, debugging_press_enter_to_skip_22],
        )
        test4_NEW.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeSymbol_8
        #incraments item counter by one
        curr_item4 += 1
        
        correct_word4 = word_list4[curr_item4] #THIS IS THE RIGHT ANSWER   
        amharic4 = amharic_list4[curr_item4]
        
        #preparing answer choices 
        lottery_list4 = []
        
        #add the right answer
        lottery_list4.append(correct_word4)
        
        #add 3 more non repeating answers
        copied_word4_list4 = []
        copied_word4_list4 = word_list4.copy() #copy word list
        copied_word4_list4.remove(correct_word4) #remove the right answer
        shuffle(copied_word4_list4) #shuffle up the copied list
        
        for x in range(0,3):    #add 3 from the shuffled list
            lottery_list4.append(copied_word4_list4[x])
        
        random.shuffle(lottery_list4)  #mix up the answer choices
        
        index_of_correct_answer4 = lottery_list4.index(correct_word4) #index of the correct word
        
        correctAns4 = index_to_button[index_of_correct_answer4] #correct answer in key form
        textAmharic_8.setText(amharic4)
        textOptionA_8.setText(lottery_list4[0]
        
        )
        textOptionB_8.setText(lottery_list4[1])
        textOptionC_8.setText(lottery_list4[2])
        textOptionD_8.setText(lottery_list4[3])
        textDiamond_7.setText(f"     {lottery_list4[0]}\n   {lottery_list4[1]}   {lottery_list4[2]}\n     {lottery_list4[3]}")
        # create starting attributes for key_resp_8
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        # create starting attributes for debugging_press_enter_to_skip_22
        debugging_press_enter_to_skip_22.keys = []
        debugging_press_enter_to_skip_22.rt = []
        _debugging_press_enter_to_skip_22_allKeys = []
        # store start times for test4_NEW
        test4_NEW.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        test4_NEW.tStart = globalClock.getTime(format='float')
        test4_NEW.status = STARTED
        thisExp.addData('test4_NEW.started', test4_NEW.tStart)
        test4_NEW.maxDuration = None
        # keep track of which components have finished
        test4_NEWComponents = test4_NEW.components
        for thisComponent in test4_NEW.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test4_NEW" ---
        # if trial has changed, end Routine now
        if isinstance(testSet4, data.TrialHandler2) and thisTestSet4.thisN != testSet4.thisTrial.thisN:
            continueRoutine = False
        test4_NEW.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textAmharic_8* updates
            
            # if textAmharic_8 is starting this frame...
            if textAmharic_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textAmharic_8.frameNStart = frameN  # exact frame index
                textAmharic_8.tStart = t  # local t and not account for scr refresh
                textAmharic_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textAmharic_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textAmharic_8.started')
                # update status
                textAmharic_8.status = STARTED
                textAmharic_8.setAutoDraw(True)
            
            # if textAmharic_8 is active this frame...
            if textAmharic_8.status == STARTED:
                # update params
                pass
            
            # *textOptionA_8* updates
            
            # if textOptionA_8 is starting this frame...
            if textOptionA_8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionA_8.frameNStart = frameN  # exact frame index
                textOptionA_8.tStart = t  # local t and not account for scr refresh
                textOptionA_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionA_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionA_8.started')
                # update status
                textOptionA_8.status = STARTED
                textOptionA_8.setAutoDraw(True)
            
            # if textOptionA_8 is active this frame...
            if textOptionA_8.status == STARTED:
                # update params
                pass
            
            # if textOptionA_8 is stopping this frame...
            if textOptionA_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionA_8.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionA_8.tStop = t  # not accounting for scr refresh
                    textOptionA_8.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionA_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionA_8.stopped')
                    # update status
                    textOptionA_8.status = FINISHED
                    textOptionA_8.setAutoDraw(False)
            
            # *textOptionB_8* updates
            
            # if textOptionB_8 is starting this frame...
            if textOptionB_8.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionB_8.frameNStart = frameN  # exact frame index
                textOptionB_8.tStart = t  # local t and not account for scr refresh
                textOptionB_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionB_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionB_8.started')
                # update status
                textOptionB_8.status = STARTED
                textOptionB_8.setAutoDraw(True)
            
            # if textOptionB_8 is active this frame...
            if textOptionB_8.status == STARTED:
                # update params
                pass
            
            # if textOptionB_8 is stopping this frame...
            if textOptionB_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionB_8.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionB_8.tStop = t  # not accounting for scr refresh
                    textOptionB_8.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionB_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionB_8.stopped')
                    # update status
                    textOptionB_8.status = FINISHED
                    textOptionB_8.setAutoDraw(False)
            
            # *textOptionC_8* updates
            
            # if textOptionC_8 is starting this frame...
            if textOptionC_8.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionC_8.frameNStart = frameN  # exact frame index
                textOptionC_8.tStart = t  # local t and not account for scr refresh
                textOptionC_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionC_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionC_8.started')
                # update status
                textOptionC_8.status = STARTED
                textOptionC_8.setAutoDraw(True)
            
            # if textOptionC_8 is active this frame...
            if textOptionC_8.status == STARTED:
                # update params
                pass
            
            # if textOptionC_8 is stopping this frame...
            if textOptionC_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionC_8.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionC_8.tStop = t  # not accounting for scr refresh
                    textOptionC_8.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionC_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionC_8.stopped')
                    # update status
                    textOptionC_8.status = FINISHED
                    textOptionC_8.setAutoDraw(False)
            
            # *textOptionD_8* updates
            
            # if textOptionD_8 is starting this frame...
            if textOptionD_8.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                textOptionD_8.frameNStart = frameN  # exact frame index
                textOptionD_8.tStart = t  # local t and not account for scr refresh
                textOptionD_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textOptionD_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textOptionD_8.started')
                # update status
                textOptionD_8.status = STARTED
                textOptionD_8.setAutoDraw(True)
            
            # if textOptionD_8 is active this frame...
            if textOptionD_8.status == STARTED:
                # update params
                pass
            
            # if textOptionD_8 is stopping this frame...
            if textOptionD_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textOptionD_8.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    textOptionD_8.tStop = t  # not accounting for scr refresh
                    textOptionD_8.tStopRefresh = tThisFlipGlobal  # on global time
                    textOptionD_8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textOptionD_8.stopped')
                    # update status
                    textOptionD_8.status = FINISHED
                    textOptionD_8.setAutoDraw(False)
            
            # *textDiamond_7* updates
            
            # if textDiamond_7 is starting this frame...
            if textDiamond_7.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                textDiamond_7.frameNStart = frameN  # exact frame index
                textDiamond_7.tStart = t  # local t and not account for scr refresh
                textDiamond_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textDiamond_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textDiamond_7.started')
                # update status
                textDiamond_7.status = STARTED
                textDiamond_7.setAutoDraw(True)
            
            # if textDiamond_7 is active this frame...
            if textDiamond_7.status == STARTED:
                # update params
                pass
            
            # *key_resp_8* updates
            waitOnFlip = False
            
            # if key_resp_8 is starting this frame...
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_8.started')
                # update status
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['right','up','left','down', 'space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                    key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                    key_resp_8.duration = _key_resp_8_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_8.keys == str(correctAns4)) or (key_resp_8.keys == correctAns4):
                        key_resp_8.corr = 1
                    else:
                        key_resp_8.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *debugging_press_enter_to_skip_22* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_22 is starting this frame...
            if debugging_press_enter_to_skip_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_22.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_22.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_22, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_22.started')
                # update status
                debugging_press_enter_to_skip_22.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_22.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if debugging_press_enter_to_skip_22.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_22.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_22_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_22_allKeys):
                    debugging_press_enter_to_skip_22.keys = _debugging_press_enter_to_skip_22_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_22.rt = _debugging_press_enter_to_skip_22_allKeys[-1].rt
                    debugging_press_enter_to_skip_22.duration = _debugging_press_enter_to_skip_22_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                test4_NEW.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test4_NEW.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test4_NEW" ---
        for thisComponent in test4_NEW.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for test4_NEW
        test4_NEW.tStop = globalClock.getTime(format='float')
        test4_NEW.tStopRefresh = tThisFlipGlobal
        thisExp.addData('test4_NEW.stopped', test4_NEW.tStop)
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
            # was no response the correct answer?!
            if str(correctAns4).lower() == 'none':
               key_resp_8.corr = 1;  # correct non-response
            else:
               key_resp_8.corr = 0;  # failed to respond (incorrectly)
        # store data for testSet4 (TrialHandler)
        testSet4.addData('key_resp_8.keys',key_resp_8.keys)
        testSet4.addData('key_resp_8.corr', key_resp_8.corr)
        if key_resp_8.keys != None:  # we had a response
            testSet4.addData('key_resp_8.rt', key_resp_8.rt)
            testSet4.addData('key_resp_8.duration', key_resp_8.duration)
        # check responses
        if debugging_press_enter_to_skip_22.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_22.keys = None
        testSet4.addData('debugging_press_enter_to_skip_22.keys',debugging_press_enter_to_skip_22.keys)
        if debugging_press_enter_to_skip_22.keys != None:  # we had a response
            testSet4.addData('debugging_press_enter_to_skip_22.rt', debugging_press_enter_to_skip_22.rt)
            testSet4.addData('debugging_press_enter_to_skip_22.duration', debugging_press_enter_to_skip_22.duration)
        # the Routine "test4_NEW" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "checkForCorr_4" ---
        # create an object to store info about Routine checkForCorr_4
        checkForCorr_4 = data.Routine(
            name='checkForCorr_4',
            components=[],
        )
        checkForCorr_4.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_5
        if key_resp_8.corr == 1:
            checkmark_reps = 1
            xmark_reps = 0
        if key_resp_8.corr == 0:
            checkmark_reps = 0
            xmark_reps = 1
        # store start times for checkForCorr_4
        checkForCorr_4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        checkForCorr_4.tStart = globalClock.getTime(format='float')
        checkForCorr_4.status = STARTED
        thisExp.addData('checkForCorr_4.started', checkForCorr_4.tStart)
        checkForCorr_4.maxDuration = None
        # keep track of which components have finished
        checkForCorr_4Components = checkForCorr_4.components
        for thisComponent in checkForCorr_4.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "checkForCorr_4" ---
        # if trial has changed, end Routine now
        if isinstance(testSet4, data.TrialHandler2) and thisTestSet4.thisN != testSet4.thisTrial.thisN:
            continueRoutine = False
        checkForCorr_4.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                checkForCorr_4.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in checkForCorr_4.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "checkForCorr_4" ---
        for thisComponent in checkForCorr_4.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for checkForCorr_4
        checkForCorr_4.tStop = globalClock.getTime(format='float')
        checkForCorr_4.tStopRefresh = tThisFlipGlobal
        thisExp.addData('checkForCorr_4.stopped', checkForCorr_4.tStop)
        # the Routine "checkForCorr_4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        checkmark_loop4 = data.TrialHandler2(
            name='checkmark_loop4',
            nReps=checkmark_reps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(checkmark_loop4)  # add the loop to the experiment
        thisCheckmark_loop4 = checkmark_loop4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisCheckmark_loop4.rgb)
        if thisCheckmark_loop4 != None:
            for paramName in thisCheckmark_loop4:
                globals()[paramName] = thisCheckmark_loop4[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisCheckmark_loop4 in checkmark_loop4:
            currentLoop = checkmark_loop4
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisCheckmark_loop4.rgb)
            if thisCheckmark_loop4 != None:
                for paramName in thisCheckmark_loop4:
                    globals()[paramName] = thisCheckmark_loop4[paramName]
            
            # --- Prepare to start Routine "checkmark" ---
            # create an object to store info about Routine checkmark
            checkmark = data.Routine(
                name='checkmark',
                components=[textCheck, debugging_press_enter_to_skip_7],
            )
            checkmark.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textCheck.setText(markers[0])
            # create starting attributes for debugging_press_enter_to_skip_7
            debugging_press_enter_to_skip_7.keys = []
            debugging_press_enter_to_skip_7.rt = []
            _debugging_press_enter_to_skip_7_allKeys = []
            # store start times for checkmark
            checkmark.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            checkmark.tStart = globalClock.getTime(format='float')
            checkmark.status = STARTED
            thisExp.addData('checkmark.started', checkmark.tStart)
            checkmark.maxDuration = None
            # keep track of which components have finished
            checkmarkComponents = checkmark.components
            for thisComponent in checkmark.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "checkmark" ---
            # if trial has changed, end Routine now
            if isinstance(checkmark_loop4, data.TrialHandler2) and thisCheckmark_loop4.thisN != checkmark_loop4.thisTrial.thisN:
                continueRoutine = False
            checkmark.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textCheck* updates
                
                # if textCheck is starting this frame...
                if textCheck.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textCheck.frameNStart = frameN  # exact frame index
                    textCheck.tStart = t  # local t and not account for scr refresh
                    textCheck.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textCheck, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textCheck.started')
                    # update status
                    textCheck.status = STARTED
                    textCheck.setAutoDraw(True)
                
                # if textCheck is active this frame...
                if textCheck.status == STARTED:
                    # update params
                    pass
                
                # if textCheck is stopping this frame...
                if textCheck.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textCheck.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textCheck.tStop = t  # not accounting for scr refresh
                        textCheck.tStopRefresh = tThisFlipGlobal  # on global time
                        textCheck.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textCheck.stopped')
                        # update status
                        textCheck.status = FINISHED
                        textCheck.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_7* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_7 is starting this frame...
                if debugging_press_enter_to_skip_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_7.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_7.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_7.started')
                    # update status
                    debugging_press_enter_to_skip_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_7.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_7 is stopping this frame...
                if debugging_press_enter_to_skip_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_7.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_7.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_7.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_7.stopped')
                        # update status
                        debugging_press_enter_to_skip_7.status = FINISHED
                        debugging_press_enter_to_skip_7.status = FINISHED
                if debugging_press_enter_to_skip_7.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_7.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_7_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_7_allKeys):
                        debugging_press_enter_to_skip_7.keys = _debugging_press_enter_to_skip_7_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_7.rt = _debugging_press_enter_to_skip_7_allKeys[-1].rt
                        debugging_press_enter_to_skip_7.duration = _debugging_press_enter_to_skip_7_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    checkmark.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in checkmark.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "checkmark" ---
            for thisComponent in checkmark.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for checkmark
            checkmark.tStop = globalClock.getTime(format='float')
            checkmark.tStopRefresh = tThisFlipGlobal
            thisExp.addData('checkmark.stopped', checkmark.tStop)
            # check responses
            if debugging_press_enter_to_skip_7.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_7.keys = None
            checkmark_loop4.addData('debugging_press_enter_to_skip_7.keys',debugging_press_enter_to_skip_7.keys)
            if debugging_press_enter_to_skip_7.keys != None:  # we had a response
                checkmark_loop4.addData('debugging_press_enter_to_skip_7.rt', debugging_press_enter_to_skip_7.rt)
                checkmark_loop4.addData('debugging_press_enter_to_skip_7.duration', debugging_press_enter_to_skip_7.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if checkmark.maxDurationReached:
                routineTimer.addTime(-checkmark.maxDuration)
            elif checkmark.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed checkmark_reps repeats of 'checkmark_loop4'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        xmark_loop4 = data.TrialHandler2(
            name='xmark_loop4',
            nReps=xmark_reps, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(xmark_loop4)  # add the loop to the experiment
        thisXmark_loop4 = xmark_loop4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisXmark_loop4.rgb)
        if thisXmark_loop4 != None:
            for paramName in thisXmark_loop4:
                globals()[paramName] = thisXmark_loop4[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisXmark_loop4 in xmark_loop4:
            currentLoop = xmark_loop4
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisXmark_loop4.rgb)
            if thisXmark_loop4 != None:
                for paramName in thisXmark_loop4:
                    globals()[paramName] = thisXmark_loop4[paramName]
            
            # --- Prepare to start Routine "xmark" ---
            # create an object to store info about Routine xmark
            xmark = data.Routine(
                name='xmark',
                components=[textXmark, debugging_press_enter_to_skip_26],
            )
            xmark.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textXmark.setText(markers[1])
            # create starting attributes for debugging_press_enter_to_skip_26
            debugging_press_enter_to_skip_26.keys = []
            debugging_press_enter_to_skip_26.rt = []
            _debugging_press_enter_to_skip_26_allKeys = []
            # store start times for xmark
            xmark.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            xmark.tStart = globalClock.getTime(format='float')
            xmark.status = STARTED
            thisExp.addData('xmark.started', xmark.tStart)
            xmark.maxDuration = None
            # keep track of which components have finished
            xmarkComponents = xmark.components
            for thisComponent in xmark.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "xmark" ---
            # if trial has changed, end Routine now
            if isinstance(xmark_loop4, data.TrialHandler2) and thisXmark_loop4.thisN != xmark_loop4.thisTrial.thisN:
                continueRoutine = False
            xmark.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textXmark* updates
                
                # if textXmark is starting this frame...
                if textXmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textXmark.frameNStart = frameN  # exact frame index
                    textXmark.tStart = t  # local t and not account for scr refresh
                    textXmark.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textXmark, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textXmark.started')
                    # update status
                    textXmark.status = STARTED
                    textXmark.setAutoDraw(True)
                
                # if textXmark is active this frame...
                if textXmark.status == STARTED:
                    # update params
                    pass
                
                # if textXmark is stopping this frame...
                if textXmark.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textXmark.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        textXmark.tStop = t  # not accounting for scr refresh
                        textXmark.tStopRefresh = tThisFlipGlobal  # on global time
                        textXmark.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textXmark.stopped')
                        # update status
                        textXmark.status = FINISHED
                        textXmark.setAutoDraw(False)
                
                # *debugging_press_enter_to_skip_26* updates
                waitOnFlip = False
                
                # if debugging_press_enter_to_skip_26 is starting this frame...
                if debugging_press_enter_to_skip_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    debugging_press_enter_to_skip_26.frameNStart = frameN  # exact frame index
                    debugging_press_enter_to_skip_26.tStart = t  # local t and not account for scr refresh
                    debugging_press_enter_to_skip_26.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(debugging_press_enter_to_skip_26, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_26.started')
                    # update status
                    debugging_press_enter_to_skip_26.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(debugging_press_enter_to_skip_26.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(debugging_press_enter_to_skip_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if debugging_press_enter_to_skip_26 is stopping this frame...
                if debugging_press_enter_to_skip_26.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > debugging_press_enter_to_skip_26.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        debugging_press_enter_to_skip_26.tStop = t  # not accounting for scr refresh
                        debugging_press_enter_to_skip_26.tStopRefresh = tThisFlipGlobal  # on global time
                        debugging_press_enter_to_skip_26.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_26.stopped')
                        # update status
                        debugging_press_enter_to_skip_26.status = FINISHED
                        debugging_press_enter_to_skip_26.status = FINISHED
                if debugging_press_enter_to_skip_26.status == STARTED and not waitOnFlip:
                    theseKeys = debugging_press_enter_to_skip_26.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                    _debugging_press_enter_to_skip_26_allKeys.extend(theseKeys)
                    if len(_debugging_press_enter_to_skip_26_allKeys):
                        debugging_press_enter_to_skip_26.keys = _debugging_press_enter_to_skip_26_allKeys[-1].name  # just the last key pressed
                        debugging_press_enter_to_skip_26.rt = _debugging_press_enter_to_skip_26_allKeys[-1].rt
                        debugging_press_enter_to_skip_26.duration = _debugging_press_enter_to_skip_26_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    xmark.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in xmark.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "xmark" ---
            for thisComponent in xmark.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for xmark
            xmark.tStop = globalClock.getTime(format='float')
            xmark.tStopRefresh = tThisFlipGlobal
            thisExp.addData('xmark.stopped', xmark.tStop)
            # check responses
            if debugging_press_enter_to_skip_26.keys in ['', [], None]:  # No response was made
                debugging_press_enter_to_skip_26.keys = None
            xmark_loop4.addData('debugging_press_enter_to_skip_26.keys',debugging_press_enter_to_skip_26.keys)
            if debugging_press_enter_to_skip_26.keys != None:  # we had a response
                xmark_loop4.addData('debugging_press_enter_to_skip_26.rt', debugging_press_enter_to_skip_26.rt)
                xmark_loop4.addData('debugging_press_enter_to_skip_26.duration', debugging_press_enter_to_skip_26.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if xmark.maxDurationReached:
                routineTimer.addTime(-xmark.maxDuration)
            elif xmark.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed xmark_reps repeats of 'xmark_loop4'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "resetReps" ---
        # create an object to store info about Routine resetReps
        resetReps = data.Routine(
            name='resetReps',
            components=[],
        )
        resetReps.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for resetReps
        resetReps.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        resetReps.tStart = globalClock.getTime(format='float')
        resetReps.status = STARTED
        thisExp.addData('resetReps.started', resetReps.tStart)
        resetReps.maxDuration = None
        # keep track of which components have finished
        resetRepsComponents = resetReps.components
        for thisComponent in resetReps.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "resetReps" ---
        # if trial has changed, end Routine now
        if isinstance(testSet4, data.TrialHandler2) and thisTestSet4.thisN != testSet4.thisTrial.thisN:
            continueRoutine = False
        resetReps.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                resetReps.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in resetReps.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "resetReps" ---
        for thisComponent in resetReps.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for resetReps
        resetReps.tStop = globalClock.getTime(format='float')
        resetReps.tStopRefresh = tThisFlipGlobal
        thisExp.addData('resetReps.stopped', resetReps.tStop)
        # the Routine "resetReps" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        # create an object to store info about Routine blank500
        blank500 = data.Routine(
            name='blank500',
            components=[text_2, debugging_press_enter_to_skip_15],
        )
        blank500.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_2.setText('')
        # create starting attributes for debugging_press_enter_to_skip_15
        debugging_press_enter_to_skip_15.keys = []
        debugging_press_enter_to_skip_15.rt = []
        _debugging_press_enter_to_skip_15_allKeys = []
        # store start times for blank500
        blank500.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank500.tStart = globalClock.getTime(format='float')
        blank500.status = STARTED
        thisExp.addData('blank500.started', blank500.tStart)
        blank500.maxDuration = None
        # keep track of which components have finished
        blank500Components = blank500.components
        for thisComponent in blank500.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        # if trial has changed, end Routine now
        if isinstance(testSet4, data.TrialHandler2) and thisTestSet4.thisN != testSet4.thisTrial.thisN:
            continueRoutine = False
        blank500.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # *debugging_press_enter_to_skip_15* updates
            waitOnFlip = False
            
            # if debugging_press_enter_to_skip_15 is starting this frame...
            if debugging_press_enter_to_skip_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                debugging_press_enter_to_skip_15.frameNStart = frameN  # exact frame index
                debugging_press_enter_to_skip_15.tStart = t  # local t and not account for scr refresh
                debugging_press_enter_to_skip_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(debugging_press_enter_to_skip_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_15.started')
                # update status
                debugging_press_enter_to_skip_15.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(debugging_press_enter_to_skip_15.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(debugging_press_enter_to_skip_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if debugging_press_enter_to_skip_15 is stopping this frame...
            if debugging_press_enter_to_skip_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > debugging_press_enter_to_skip_15.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    debugging_press_enter_to_skip_15.tStop = t  # not accounting for scr refresh
                    debugging_press_enter_to_skip_15.tStopRefresh = tThisFlipGlobal  # on global time
                    debugging_press_enter_to_skip_15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_15.stopped')
                    # update status
                    debugging_press_enter_to_skip_15.status = FINISHED
                    debugging_press_enter_to_skip_15.status = FINISHED
            if debugging_press_enter_to_skip_15.status == STARTED and not waitOnFlip:
                theseKeys = debugging_press_enter_to_skip_15.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _debugging_press_enter_to_skip_15_allKeys.extend(theseKeys)
                if len(_debugging_press_enter_to_skip_15_allKeys):
                    debugging_press_enter_to_skip_15.keys = _debugging_press_enter_to_skip_15_allKeys[-1].name  # just the last key pressed
                    debugging_press_enter_to_skip_15.rt = _debugging_press_enter_to_skip_15_allKeys[-1].rt
                    debugging_press_enter_to_skip_15.duration = _debugging_press_enter_to_skip_15_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank500.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank500
        blank500.tStop = globalClock.getTime(format='float')
        blank500.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank500.stopped', blank500.tStop)
        # check responses
        if debugging_press_enter_to_skip_15.keys in ['', [], None]:  # No response was made
            debugging_press_enter_to_skip_15.keys = None
        testSet4.addData('debugging_press_enter_to_skip_15.keys',debugging_press_enter_to_skip_15.keys)
        if debugging_press_enter_to_skip_15.keys != None:  # we had a response
            testSet4.addData('debugging_press_enter_to_skip_15.rt', debugging_press_enter_to_skip_15.rt)
            testSet4.addData('debugging_press_enter_to_skip_15.duration', debugging_press_enter_to_skip_15.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank500.maxDurationReached:
            routineTimer.addTime(-blank500.maxDuration)
        elif blank500.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed 12.0 repeats of 'testSet4'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "breakBetweenSets" ---
    # create an object to store info about Routine breakBetweenSets
    breakBetweenSets = data.Routine(
        name='breakBetweenSets',
        components=[cross, debugging_press_enter_to_skip_8],
    )
    breakBetweenSets.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for debugging_press_enter_to_skip_8
    debugging_press_enter_to_skip_8.keys = []
    debugging_press_enter_to_skip_8.rt = []
    _debugging_press_enter_to_skip_8_allKeys = []
    # store start times for breakBetweenSets
    breakBetweenSets.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    breakBetweenSets.tStart = globalClock.getTime(format='float')
    breakBetweenSets.status = STARTED
    thisExp.addData('breakBetweenSets.started', breakBetweenSets.tStart)
    breakBetweenSets.maxDuration = None
    # keep track of which components have finished
    breakBetweenSetsComponents = breakBetweenSets.components
    for thisComponent in breakBetweenSets.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "breakBetweenSets" ---
    breakBetweenSets.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.tStopRefresh = tThisFlipGlobal  # on global time
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # *debugging_press_enter_to_skip_8* updates
        waitOnFlip = False
        
        # if debugging_press_enter_to_skip_8 is starting this frame...
        if debugging_press_enter_to_skip_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debugging_press_enter_to_skip_8.frameNStart = frameN  # exact frame index
            debugging_press_enter_to_skip_8.tStart = t  # local t and not account for scr refresh
            debugging_press_enter_to_skip_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debugging_press_enter_to_skip_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_8.started')
            # update status
            debugging_press_enter_to_skip_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(debugging_press_enter_to_skip_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(debugging_press_enter_to_skip_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if debugging_press_enter_to_skip_8 is stopping this frame...
        if debugging_press_enter_to_skip_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > debugging_press_enter_to_skip_8.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                debugging_press_enter_to_skip_8.tStop = t  # not accounting for scr refresh
                debugging_press_enter_to_skip_8.tStopRefresh = tThisFlipGlobal  # on global time
                debugging_press_enter_to_skip_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debugging_press_enter_to_skip_8.stopped')
                # update status
                debugging_press_enter_to_skip_8.status = FINISHED
                debugging_press_enter_to_skip_8.status = FINISHED
        if debugging_press_enter_to_skip_8.status == STARTED and not waitOnFlip:
            theseKeys = debugging_press_enter_to_skip_8.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _debugging_press_enter_to_skip_8_allKeys.extend(theseKeys)
            if len(_debugging_press_enter_to_skip_8_allKeys):
                debugging_press_enter_to_skip_8.keys = _debugging_press_enter_to_skip_8_allKeys[-1].name  # just the last key pressed
                debugging_press_enter_to_skip_8.rt = _debugging_press_enter_to_skip_8_allKeys[-1].rt
                debugging_press_enter_to_skip_8.duration = _debugging_press_enter_to_skip_8_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            breakBetweenSets.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breakBetweenSets.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "breakBetweenSets" ---
    for thisComponent in breakBetweenSets.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for breakBetweenSets
    breakBetweenSets.tStop = globalClock.getTime(format='float')
    breakBetweenSets.tStopRefresh = tThisFlipGlobal
    thisExp.addData('breakBetweenSets.stopped', breakBetweenSets.tStop)
    # check responses
    if debugging_press_enter_to_skip_8.keys in ['', [], None]:  # No response was made
        debugging_press_enter_to_skip_8.keys = None
    thisExp.addData('debugging_press_enter_to_skip_8.keys',debugging_press_enter_to_skip_8.keys)
    if debugging_press_enter_to_skip_8.keys != None:  # we had a response
        thisExp.addData('debugging_press_enter_to_skip_8.rt', debugging_press_enter_to_skip_8.rt)
        thisExp.addData('debugging_press_enter_to_skip_8.duration', debugging_press_enter_to_skip_8.duration)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if breakBetweenSets.maxDurationReached:
        routineTimer.addTime(-breakBetweenSets.maxDuration)
    elif breakBetweenSets.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "WelcomeSlide" ---
    # create an object to store info about Routine WelcomeSlide
    WelcomeSlide = data.Routine(
        name='WelcomeSlide',
        components=[Welcome, goNext],
    )
    WelcomeSlide.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for goNext
    goNext.keys = []
    goNext.rt = []
    _goNext_allKeys = []
    # store start times for WelcomeSlide
    WelcomeSlide.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    WelcomeSlide.tStart = globalClock.getTime(format='float')
    WelcomeSlide.status = STARTED
    thisExp.addData('WelcomeSlide.started', WelcomeSlide.tStart)
    WelcomeSlide.maxDuration = None
    # keep track of which components have finished
    WelcomeSlideComponents = WelcomeSlide.components
    for thisComponent in WelcomeSlide.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "WelcomeSlide" ---
    WelcomeSlide.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Welcome* updates
        
        # if Welcome is starting this frame...
        if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Welcome.frameNStart = frameN  # exact frame index
            Welcome.tStart = t  # local t and not account for scr refresh
            Welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Welcome.started')
            # update status
            Welcome.status = STARTED
            Welcome.setAutoDraw(True)
        
        # if Welcome is active this frame...
        if Welcome.status == STARTED:
            # update params
            pass
        
        # *goNext* updates
        waitOnFlip = False
        
        # if goNext is starting this frame...
        if goNext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goNext.frameNStart = frameN  # exact frame index
            goNext.tStart = t  # local t and not account for scr refresh
            goNext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goNext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goNext.started')
            # update status
            goNext.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(goNext.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(goNext.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if goNext.status == STARTED and not waitOnFlip:
            theseKeys = goNext.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _goNext_allKeys.extend(theseKeys)
            if len(_goNext_allKeys):
                goNext.keys = _goNext_allKeys[-1].name  # just the last key pressed
                goNext.rt = _goNext_allKeys[-1].rt
                goNext.duration = _goNext_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            WelcomeSlide.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeSlide.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WelcomeSlide" ---
    for thisComponent in WelcomeSlide.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for WelcomeSlide
    WelcomeSlide.tStop = globalClock.getTime(format='float')
    WelcomeSlide.tStopRefresh = tThisFlipGlobal
    thisExp.addData('WelcomeSlide.stopped', WelcomeSlide.tStop)
    # check responses
    if goNext.keys in ['', [], None]:  # No response was made
        goNext.keys = None
    thisExp.addData('goNext.keys',goNext.keys)
    if goNext.keys != None:  # we had a response
        thisExp.addData('goNext.rt', goNext.rt)
        thisExp.addData('goNext.duration', goNext.duration)
    thisExp.nextEntry()
    # the Routine "WelcomeSlide" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions" ---
    # create an object to store info about Routine Instructions
    Instructions = data.Routine(
        name='Instructions',
        components=[instructions_text, goNext1],
    )
    Instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for goNext1
    goNext1.keys = []
    goNext1.rt = []
    _goNext1_allKeys = []
    # store start times for Instructions
    Instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions.tStart = globalClock.getTime(format='float')
    Instructions.status = STARTED
    thisExp.addData('Instructions.started', Instructions.tStart)
    Instructions.maxDuration = None
    # keep track of which components have finished
    InstructionsComponents = Instructions.components
    for thisComponent in Instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions" ---
    Instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_text* updates
        
        # if instructions_text is starting this frame...
        if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_text.frameNStart = frameN  # exact frame index
            instructions_text.tStart = t  # local t and not account for scr refresh
            instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions_text.started')
            # update status
            instructions_text.status = STARTED
            instructions_text.setAutoDraw(True)
        
        # if instructions_text is active this frame...
        if instructions_text.status == STARTED:
            # update params
            pass
        
        # *goNext1* updates
        waitOnFlip = False
        
        # if goNext1 is starting this frame...
        if goNext1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goNext1.frameNStart = frameN  # exact frame index
            goNext1.tStart = t  # local t and not account for scr refresh
            goNext1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goNext1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goNext1.started')
            # update status
            goNext1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(goNext1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(goNext1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if goNext1.status == STARTED and not waitOnFlip:
            theseKeys = goNext1.getKeys(keyList=['return', 'space'], ignoreKeys=["escape"], waitRelease=False)
            _goNext1_allKeys.extend(theseKeys)
            if len(_goNext1_allKeys):
                goNext1.keys = _goNext1_allKeys[-1].name  # just the last key pressed
                goNext1.rt = _goNext1_allKeys[-1].rt
                goNext1.duration = _goNext1_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions" ---
    for thisComponent in Instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions
    Instructions.tStop = globalClock.getTime(format='float')
    Instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions.stopped', Instructions.tStop)
    # check responses
    if goNext1.keys in ['', [], None]:  # No response was made
        goNext1.keys = None
    thisExp.addData('goNext1.keys',goNext1.keys)
    if goNext1.keys != None:  # we had a response
        thisExp.addData('goNext1.rt', goNext1.rt)
        thisExp.addData('goNext1.duration', goNext1.duration)
    thisExp.nextEntry()
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Trials = data.TrialHandler2(
        name='Trials',
        nReps=24.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(Trials)  # add the loop to the experiment
    thisTrial = Trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in Trials:
        currentLoop = Trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "TestQuestion" ---
        # create an object to store info about Routine TestQuestion
        TestQuestion = data.Routine(
            name='TestQuestion',
            components=[answer_box, enter, symbol],
        )
        TestQuestion.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        answer_box.reset()
        answer_box.setPlaceholder('')
        # create starting attributes for enter
        enter.keys = []
        enter.rt = []
        _enter_allKeys = []
        # Run 'Begin Routine' code from RandomQuestion
        # Makes sure we don't get key errors going past index 23
        if curr_item < 24:
            curr_item += 1
            curr_item %= 24
        
        # store start times for TestQuestion
        TestQuestion.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        TestQuestion.tStart = globalClock.getTime(format='float')
        TestQuestion.status = STARTED
        thisExp.addData('TestQuestion.started', TestQuestion.tStart)
        TestQuestion.maxDuration = None
        # keep track of which components have finished
        TestQuestionComponents = TestQuestion.components
        for thisComponent in TestQuestion.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TestQuestion" ---
        # if trial has changed, end Routine now
        if isinstance(Trials, data.TrialHandler2) and thisTrial.thisN != Trials.thisTrial.thisN:
            continueRoutine = False
        TestQuestion.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *answer_box* updates
            
            # if answer_box is starting this frame...
            if answer_box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                answer_box.frameNStart = frameN  # exact frame index
                answer_box.tStart = t  # local t and not account for scr refresh
                answer_box.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(answer_box, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'answer_box.started')
                # update status
                answer_box.status = STARTED
                answer_box.setAutoDraw(True)
            
            # if answer_box is active this frame...
            if answer_box.status == STARTED:
                # update params
                pass
            
            # *enter* updates
            waitOnFlip = False
            
            # if enter is starting this frame...
            if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                enter.frameNStart = frameN  # exact frame index
                enter.tStart = t  # local t and not account for scr refresh
                enter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(enter, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'enter.started')
                # update status
                enter.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if enter.status == STARTED and not waitOnFlip:
                theseKeys = enter.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _enter_allKeys.extend(theseKeys)
                if len(_enter_allKeys):
                    enter.keys = _enter_allKeys[-1].name  # just the last key pressed
                    enter.rt = _enter_allKeys[-1].rt
                    enter.duration = _enter_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *symbol* updates
            
            # if symbol is starting this frame...
            if symbol.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                symbol.frameNStart = frameN  # exact frame index
                symbol.tStart = t  # local t and not account for scr refresh
                symbol.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symbol, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symbol.started')
                # update status
                symbol.status = STARTED
                symbol.setAutoDraw(True)
            
            # if symbol is active this frame...
            if symbol.status == STARTED:
                # update params
                symbol.setText(test_questions[curr_item][0], log=False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                TestQuestion.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TestQuestion.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TestQuestion" ---
        for thisComponent in TestQuestion.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for TestQuestion
        TestQuestion.tStop = globalClock.getTime(format='float')
        TestQuestion.tStopRefresh = tThisFlipGlobal
        thisExp.addData('TestQuestion.stopped', TestQuestion.tStop)
        Trials.addData('answer_box.text',answer_box.text)
        # check responses
        if enter.keys in ['', [], None]:  # No response was made
            enter.keys = None
        Trials.addData('enter.keys',enter.keys)
        if enter.keys != None:  # we had a response
            Trials.addData('enter.rt', enter.rt)
            Trials.addData('enter.duration', enter.duration)
        # the Routine "TestQuestion" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Evaluate" ---
        # create an object to store info about Routine Evaluate
        Evaluate = data.Routine(
            name='Evaluate',
            components=[],
        )
        Evaluate.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from CorrectAnswers
        if answer_box.text.strip().upper() == test_questions[curr_item][1].upper():
            correct += 1
            print("Debugging: This is correct\n Correct = " + str(correct))
        # store start times for Evaluate
        Evaluate.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Evaluate.tStart = globalClock.getTime(format='float')
        Evaluate.status = STARTED
        thisExp.addData('Evaluate.started', Evaluate.tStart)
        Evaluate.maxDuration = None
        # keep track of which components have finished
        EvaluateComponents = Evaluate.components
        for thisComponent in Evaluate.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Evaluate" ---
        # if trial has changed, end Routine now
        if isinstance(Trials, data.TrialHandler2) and thisTrial.thisN != Trials.thisTrial.thisN:
            continueRoutine = False
        Evaluate.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Evaluate.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Evaluate.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Evaluate" ---
        for thisComponent in Evaluate.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Evaluate
        Evaluate.tStop = globalClock.getTime(format='float')
        Evaluate.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Evaluate.stopped', Evaluate.tStop)
        # the Routine "Evaluate" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 24.0 repeats of 'Trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "ThankYou" ---
    # create an object to store info about Routine ThankYou
    ThankYou = data.Routine(
        name='ThankYou',
        components=[text_6],
    )
    ThankYou.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Debug
    thankyoumessage = "Thank you for participating, You got " + str(correct) + " out of 24 correct"
    # store start times for ThankYou
    ThankYou.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ThankYou.tStart = globalClock.getTime(format='float')
    ThankYou.status = STARTED
    thisExp.addData('ThankYou.started', ThankYou.tStart)
    ThankYou.maxDuration = None
    # keep track of which components have finished
    ThankYouComponents = ThankYou.components
    for thisComponent in ThankYou.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ThankYou" ---
    ThankYou.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ThankYou.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ThankYou.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ThankYou" ---
    for thisComponent in ThankYou.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ThankYou
    ThankYou.tStop = globalClock.getTime(format='float')
    ThankYou.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ThankYou.stopped', ThankYou.tStop)
    thisExp.nextEntry()
    # the Routine "ThankYou" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
