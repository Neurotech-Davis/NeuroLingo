/****************** 
 * Finaltest *
 ******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'finaltest';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from Set_Counterbalance_Here
numReps = 8;

// Run 'Before Experiment' code from codeLoader
/* Syntax Error: Fix Python code */
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(COUNTERBALANCERoutineBegin());
flowScheduler.add(COUNTERBALANCERoutineEachFrame());
flowScheduler.add(COUNTERBALANCERoutineEnd());
const LoopParametersLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(LoopParametersLoopBegin(LoopParametersLoopScheduler));
flowScheduler.add(LoopParametersLoopScheduler);
flowScheduler.add(LoopParametersLoopEnd);


flowScheduler.add(RemoveNoneRoutineBegin());
flowScheduler.add(RemoveNoneRoutineEachFrame());
flowScheduler.add(RemoveNoneRoutineEnd());
flowScheduler.add(GenerateQuestionsRoutineBegin());
flowScheduler.add(GenerateQuestionsRoutineEachFrame());
flowScheduler.add(GenerateQuestionsRoutineEnd());
flowScheduler.add(practice_welcomeRoutineBegin());
flowScheduler.add(practice_welcomeRoutineEachFrame());
flowScheduler.add(practice_welcomeRoutineEnd());
const pracitce_wrdsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(pracitce_wrdsLoopBegin(pracitce_wrdsLoopScheduler));
flowScheduler.add(pracitce_wrdsLoopScheduler);
flowScheduler.add(pracitce_wrdsLoopEnd);



flowScheduler.add(breakBetweenSetsRoutineBegin());
flowScheduler.add(breakBetweenSetsRoutineEachFrame());
flowScheduler.add(breakBetweenSetsRoutineEnd());
const practice_imagessLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_imagessLoopBegin(practice_imagessLoopScheduler));
flowScheduler.add(practice_imagessLoopScheduler);
flowScheduler.add(practice_imagessLoopEnd);



const practice_testtLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_testtLoopBegin(practice_testtLoopScheduler));
flowScheduler.add(practice_testtLoopScheduler);
flowScheduler.add(practice_testtLoopEnd);











flowScheduler.add(WelcomeScreenRoutineBegin());
flowScheduler.add(WelcomeScreenRoutineEachFrame());
flowScheduler.add(WelcomeScreenRoutineEnd());
const LearningSetOneLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(LearningSetOneLoopBegin(LearningSetOneLoopScheduler));
flowScheduler.add(LearningSetOneLoopScheduler);
flowScheduler.add(LearningSetOneLoopEnd);













flowScheduler.add(routine_30SecondsRoutineBegin());
flowScheduler.add(routine_30SecondsRoutineEachFrame());
flowScheduler.add(routine_30SecondsRoutineEnd());
flowScheduler.add(start_testRoutineBegin());
flowScheduler.add(start_testRoutineEachFrame());
flowScheduler.add(start_testRoutineEnd());
const testSet1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(testSet1LoopBegin(testSet1LoopScheduler));
flowScheduler.add(testSet1LoopScheduler);
flowScheduler.add(testSet1LoopEnd);











flowScheduler.add(breakBetweenSetsRoutineBegin());
flowScheduler.add(breakBetweenSetsRoutineEachFrame());
flowScheduler.add(breakBetweenSetsRoutineEnd());
const LearningSetTwoLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(LearningSetTwoLoopBegin(LearningSetTwoLoopScheduler));
flowScheduler.add(LearningSetTwoLoopScheduler);
flowScheduler.add(LearningSetTwoLoopEnd);













flowScheduler.add(routine_30SecondsRoutineBegin());
flowScheduler.add(routine_30SecondsRoutineEachFrame());
flowScheduler.add(routine_30SecondsRoutineEnd());
flowScheduler.add(start_testRoutineBegin());
flowScheduler.add(start_testRoutineEachFrame());
flowScheduler.add(start_testRoutineEnd());
const testSet2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(testSet2LoopBegin(testSet2LoopScheduler));
flowScheduler.add(testSet2LoopScheduler);
flowScheduler.add(testSet2LoopEnd);











flowScheduler.add(breakBetweenSetsRoutineBegin());
flowScheduler.add(breakBetweenSetsRoutineEachFrame());
flowScheduler.add(breakBetweenSetsRoutineEnd());
const LearningSetThreeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(LearningSetThreeLoopBegin(LearningSetThreeLoopScheduler));
flowScheduler.add(LearningSetThreeLoopScheduler);
flowScheduler.add(LearningSetThreeLoopEnd);













flowScheduler.add(routine_30SecondsRoutineBegin());
flowScheduler.add(routine_30SecondsRoutineEachFrame());
flowScheduler.add(routine_30SecondsRoutineEnd());
flowScheduler.add(start_testRoutineBegin());
flowScheduler.add(start_testRoutineEachFrame());
flowScheduler.add(start_testRoutineEnd());
const testSet3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(testSet3LoopBegin(testSet3LoopScheduler));
flowScheduler.add(testSet3LoopScheduler);
flowScheduler.add(testSet3LoopEnd);











flowScheduler.add(breakBetweenSetsRoutineBegin());
flowScheduler.add(breakBetweenSetsRoutineEachFrame());
flowScheduler.add(breakBetweenSetsRoutineEnd());
const LearningSetFourLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(LearningSetFourLoopBegin(LearningSetFourLoopScheduler));
flowScheduler.add(LearningSetFourLoopScheduler);
flowScheduler.add(LearningSetFourLoopEnd);













flowScheduler.add(routine_30SecondsRoutineBegin());
flowScheduler.add(routine_30SecondsRoutineEachFrame());
flowScheduler.add(routine_30SecondsRoutineEnd());
flowScheduler.add(start_testRoutineBegin());
flowScheduler.add(start_testRoutineEachFrame());
flowScheduler.add(start_testRoutineEnd());
const testSet4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(testSet4LoopBegin(testSet4LoopScheduler));
flowScheduler.add(testSet4LoopScheduler);
flowScheduler.add(testSet4LoopEnd);











flowScheduler.add(breakBetweenSetsRoutineBegin());
flowScheduler.add(breakBetweenSetsRoutineEachFrame());
flowScheduler.add(breakBetweenSetsRoutineEnd());
flowScheduler.add(WelcomeSlideRoutineBegin());
flowScheduler.add(WelcomeSlideRoutineEachFrame());
flowScheduler.add(WelcomeSlideRoutineEnd());
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const TrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(TrialsLoopBegin(TrialsLoopScheduler));
flowScheduler.add(TrialsLoopScheduler);
flowScheduler.add(TrialsLoopEnd);



flowScheduler.add(ThankYouRoutineBegin());
flowScheduler.add(ThankYouRoutineEachFrame());
flowScheduler.add(ThankYouRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'testSymbols2.xlsx', 'path': 'testSymbols2.xlsx'},
    {'name': 'pictures/hike.jpg', 'path': 'pictures/hike.jpg'},
    {'name': 'pictures/I.jpg', 'path': 'pictures/I.jpg'},
    {'name': 'pictures/be.jpg', 'path': 'pictures/be.jpg'},
    {'name': 'pictures/computer.jpg', 'path': 'pictures/computer.jpg'},
    {'name': 'pictures/have.jpg', 'path': 'pictures/have.jpg'},
    {'name': 'pictures/hungry.jpg', 'path': 'pictures/hungry.jpg'},
    {'name': 'pictures/important.jpg', 'path': 'pictures/important.jpg'},
    {'name': 'pictures/library.jpg', 'path': 'pictures/library.jpg'},
    {'name': 'pictures/money.jpg', 'path': 'pictures/money.jpg'},
    {'name': 'pictures/plan.jpg', 'path': 'pictures/plan.jpg'},
    {'name': 'pictures/you.jpg', 'path': 'pictures/you.jpg'},
    {'name': 'testSymbols2.xlsx', 'path': 'testSymbols2.xlsx'},
    {'name': 'pictures/hike.jpg', 'path': 'pictures/hike.jpg'},
    {'name': 'pictures/I.jpg', 'path': 'pictures/I.jpg'},
    {'name': 'pictures/be.jpg', 'path': 'pictures/be.jpg'},
    {'name': 'pictures/computer.jpg', 'path': 'pictures/computer.jpg'},
    {'name': 'pictures/have.jpg', 'path': 'pictures/have.jpg'},
    {'name': 'pictures/hungry.jpg', 'path': 'pictures/hungry.jpg'},
    {'name': 'pictures/important.jpg', 'path': 'pictures/important.jpg'},
    {'name': 'pictures/library.jpg', 'path': 'pictures/library.jpg'},
    {'name': 'pictures/money.jpg', 'path': 'pictures/money.jpg'},
    {'name': 'pictures/plan.jpg', 'path': 'pictures/plan.jpg'},
    {'name': 'pictures/you.jpg', 'path': 'pictures/you.jpg'},
    {'name': 'testSymbols2.xlsx', 'path': 'testSymbols2.xlsx'},
    {'name': 'pictures/hike.jpg', 'path': 'pictures/hike.jpg'},
    {'name': 'pictures/I.jpg', 'path': 'pictures/I.jpg'},
    {'name': 'pictures/be.jpg', 'path': 'pictures/be.jpg'},
    {'name': 'pictures/computer.jpg', 'path': 'pictures/computer.jpg'},
    {'name': 'pictures/have.jpg', 'path': 'pictures/have.jpg'},
    {'name': 'pictures/hungry.jpg', 'path': 'pictures/hungry.jpg'},
    {'name': 'pictures/important.jpg', 'path': 'pictures/important.jpg'},
    {'name': 'pictures/library.jpg', 'path': 'pictures/library.jpg'},
    {'name': 'pictures/money.jpg', 'path': 'pictures/money.jpg'},
    {'name': 'pictures/plan.jpg', 'path': 'pictures/plan.jpg'},
    {'name': 'pictures/you.jpg', 'path': 'pictures/you.jpg'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "COUNTERBALANCE"
  COUNTERBALANCEClock = new util.Clock();
  // Run 'Begin Experiment' code from Set_Counterbalance_Here
  counterbalance = false;
  if ((counterbalance === true)) {
      nreps_A = 0;
      nreps_B = 1;
  } else {
      nreps_A = 1;
      nreps_B = 0;
  }
  
  // Initialize components for Routine "LoadCharacters"
  LoadCharactersClock = new util.Clock();
  // Run 'Begin Experiment' code from codeLoader
  word_list1 = [];
  amharic_list1 = [];
  word_list2 = [];
  amharic_list2 = [];
  word_list3 = [];
  amharic_list3 = [];
  word_list4 = [];
  amharic_list4 = [];
  markers = [];
  practice_amharic = [];
  practice_words = [];
  checkmark_reps = 0;
  xmark_reps = 0;
  
  // Initialize components for Routine "RemoveNone"
  RemoveNoneClock = new util.Clock();
  // Initialize components for Routine "GenerateQuestions"
  GenerateQuestionsClock = new util.Clock();
  // Initialize components for Routine "practice_welcome"
  practice_welcomeClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Before moving onto the proper data collection section you will be shown a short version of what the real thing will look like to better prepare you.\n\nYou will be shown 12 total symbols to learn and given an accompanying test. The real thing will follow the same procedure but differ in scale. \n\nPress space to move foward with the practice trials. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_wrdss"
  practice_wrdssClock = new util.Clock();
  practice_amharicc = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_amharicc',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  practice_wordssss = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_wordssss',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "plusBetween"
  plusBetweenClock = new util.Clock();
  plus = new visual.TextStim({
    win: psychoJS.window,
    name: 'plus',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  debugging_press_enter_to_skip_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "breakBetweenSets"
  breakBetweenSetsClock = new util.Clock();
  cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'cross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.3,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  debugging_press_enter_to_skip_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_images"
  practice_imagesClock = new util.Clock();
  amharic_practice2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'amharic_practice2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  image_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_practice', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.3, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "practice_test"
  practice_testClock = new util.Clock();
  // Run 'Begin Experiment' code from codeSymbol_9
  import * as random from 'random';
  curr_item = (- 1);
  
  textAmharic_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textAmharic_9',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], draggable: false, height: 0.3,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  textOptionA_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionA_9',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  textOptionB_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionB_9',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  textOptionC_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionC_9',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  textOptionD_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionD_9',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  textDiamond_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textDiamond_8',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  debugging_press_enter_to_skip_23 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "checkForCorr_5"
  checkForCorr_5Clock = new util.Clock();
  // Initialize components for Routine "checkmark"
  checkmarkClock = new util.Clock();
  textCheck = new visual.TextStim({
    win: psychoJS.window,
    name: 'textCheck',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "xmark"
  xmarkClock = new util.Clock();
  textXmark = new visual.TextStim({
    win: psychoJS.window,
    name: 'textXmark',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "resetReps"
  resetRepsClock = new util.Clock();
  // Run 'Begin Experiment' code from code_6
  checkmark_reps = 0;
  xmark_reps = 0;
  
  // Initialize components for Routine "blank500"
  blank500Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  debugging_press_enter_to_skip_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "WelcomeScreen"
  WelcomeScreenClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Welcome to our experiment\n\nPress SPACE when ready',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Press_Space_When_Ready = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "randomize_set"
  randomize_setClock = new util.Clock();
  // Initialize components for Routine "Increment"
  IncrementClock = new util.Clock();
  // Run 'Begin Experiment' code from increment_index
  learning_index = (- 1);
  
  // Initialize components for Routine "amharic1_A"
  amharic1_AClock = new util.Clock();
  pratice_amharic = new visual.TextStim({
    win: psychoJS.window,
    name: 'pratice_amharic',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  practice_words = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_words',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.15,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  debugging_press_enter_to_skip = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "amharic1_B"
  amharic1_BClock = new util.Clock();
  amharics1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'amharics1_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  words1_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'words1_image_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.3, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  debugging_press_enter_to_skip_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "breakBetweenRepeats"
  breakBetweenRepeatsClock = new util.Clock();
  five_seconds = new visual.TextStim({
    win: psychoJS.window,
    name: 'five_seconds',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  maybe_a_beep = new sound.Sound({
      win: psychoJS.window,
      value: 'A',
      secs: 1.0,
      });
  maybe_a_beep.setVolume(1.0);
  debugging_press_enter_to_skip_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "routine_30Seconds"
  routine_30SecondsClock = new util.Clock();
  thirtySeconds = new visual.TextStim({
    win: psychoJS.window,
    name: 'thirtySeconds',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Run 'Begin Experiment' code from var_30_secs
  console.log("30 seconds");
  
  debugging_press_enter_to_skip_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "start_test"
  start_testClock = new util.Clock();
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: 'The test phase will now begin.\n\nIf you do not know an answer do not press anything. Please avoid guessing. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  debugging_press_enter_to_skip_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "test1_NEW"
  test1_NEWClock = new util.Clock();
  // Run 'Begin Experiment' code from codeSymbol_5
  import * as random from 'random';
  curr_item = (- 1);
  
  textAmharic_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textAmharic_5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], draggable: false, height: 0.3,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  textOptionA_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionA_5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  textOptionB_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionB_5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  textOptionC_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionC_5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  textOptionD_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionD_5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  textDiamond_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textDiamond_3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  debugging_press_enter_to_skip_19 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "checkForCorr"
  checkForCorrClock = new util.Clock();
  // Initialize components for Routine "amharic2_A"
  amharic2_AClock = new util.Clock();
  amharics2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'amharics2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  words2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'words2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.15,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  debugging_press_enter_to_skip_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "amharic2_B"
  amharic2_BClock = new util.Clock();
  amharics2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'amharics2_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  words2_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'words2_image_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.3, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  debugging_press_enter_to_skip_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "test2_NEW"
  test2_NEWClock = new util.Clock();
  // Run 'Begin Experiment' code from codeSymbol_6
  import * as random from 'random';
  curr_item = (- 1);
  
  textAmharic_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textAmharic_6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], draggable: false, height: 0.3,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  textOptionA_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionA_6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  textOptionB_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionB_6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  textOptionC_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionC_6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  textOptionD_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionD_6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  textDiamond_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textDiamond_5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  debugging_press_enter_to_skip_20 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "checkForCorr_2"
  checkForCorr_2Clock = new util.Clock();
  // Initialize components for Routine "amharic3_A"
  amharic3_AClock = new util.Clock();
  amharics3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'amharics3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  words3_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'words3_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.3, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  debugging_press_enter_to_skip_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "amharic3_B"
  amharic3_BClock = new util.Clock();
  amharics3_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'amharics3_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  words3_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'words3_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.15,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  debugging_press_enter_to_skip_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "test3_NEW"
  test3_NEWClock = new util.Clock();
  // Run 'Begin Experiment' code from codeSymbol_7
  import * as random from 'random';
  curr_item = (- 1);
  
  textAmharic_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textAmharic_7',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], draggable: false, height: 0.3,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  textOptionA_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionA_7',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  textOptionB_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionB_7',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  textOptionC_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionC_7',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  textOptionD_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionD_7',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  textDiamond_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textDiamond_6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  debugging_press_enter_to_skip_21 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "checkForCorr_3"
  checkForCorr_3Clock = new util.Clock();
  // Initialize components for Routine "amharic4_A"
  amharic4_AClock = new util.Clock();
  amharics4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'amharics4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  words4_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'words4_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.3, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  debugging_press_enter_to_skip_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "amharic4_B"
  amharic4_BClock = new util.Clock();
  amharics4_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'amharics4_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), 0], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  words4_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'words4_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.15,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  debugging_press_enter_to_skip_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "test4_NEW"
  test4_NEWClock = new util.Clock();
  // Run 'Begin Experiment' code from codeSymbol_8
  import * as random from 'random';
  curr_item = (- 1);
  
  textAmharic_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textAmharic_8',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], draggable: false, height: 0.3,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  textOptionA_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionA_8',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  textOptionB_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionB_8',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  textOptionC_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionC_8',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  textOptionD_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textOptionD_8',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0.0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  textDiamond_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'textDiamond_7',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  debugging_press_enter_to_skip_22 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "checkForCorr_4"
  checkForCorr_4Clock = new util.Clock();
  // Initialize components for Routine "WelcomeSlide"
  WelcomeSlideClock = new util.Clock();
  Welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'Welcome',
    text: 'We will now begin the final part of the experiment.\n(Press ENTER to continue)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  goNext = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: 'In the next slides, you will be prompted to give the translation of a given symbol. \n\nOnce you have typed the answer, press "ENTER" to continue. If you do not remember the symbol, you can simply press "ENTER".\n\nYou have unlimited time to respond to each question. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  goNext1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "TestQuestion"
  TestQuestionClock = new util.Clock();
  answer_box = new visual.TextBox({
    win: psychoJS.window,
    name: 'answer_box',
    text: '',
    placeholder: undefined,
    font: 'Arial',
    pos: [0, (- 0.35)], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  enter = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  symbol = new visual.TextStim({
    win: psychoJS.window,
    name: 'symbol',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.5,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Run 'Begin Experiment' code from RandomQuestion
  curr_item = (- 1);
  
  // Initialize components for Routine "Evaluate"
  EvaluateClock = new util.Clock();
  // Run 'Begin Experiment' code from CorrectAnswers
  correct = 0;
  message = (("You got " + correct.toString()) + " out of 24 correct!");
  
  // Initialize components for Routine "ThankYou"
  ThankYouClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function COUNTERBALANCERoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'COUNTERBALANCE' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    COUNTERBALANCEClock.reset();
    routineTimer.reset();
    COUNTERBALANCEMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('COUNTERBALANCE.started', globalClock.getTime());
    COUNTERBALANCEMaxDuration = null
    // keep track of which components have finished
    COUNTERBALANCEComponents = [];
    
    for (const thisComponent of COUNTERBALANCEComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function COUNTERBALANCERoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'COUNTERBALANCE' ---
    // get current time
    t = COUNTERBALANCEClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of COUNTERBALANCEComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function COUNTERBALANCERoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'COUNTERBALANCE' ---
    for (const thisComponent of COUNTERBALANCEComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('COUNTERBALANCE.stopped', globalClock.getTime());
    // the Routine "COUNTERBALANCE" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function LoopParametersLoopBegin(LoopParametersLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    LoopParameters = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'testSymbols2.xlsx',
      seed: undefined, name: 'LoopParameters'
    });
    psychoJS.experiment.addLoop(LoopParameters); // add the loop to the experiment
    currentLoop = LoopParameters;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoopParameter of LoopParameters) {
      snapshot = LoopParameters.getSnapshot();
      LoopParametersLoopScheduler.add(importConditions(snapshot));
      LoopParametersLoopScheduler.add(LoadCharactersRoutineBegin(snapshot));
      LoopParametersLoopScheduler.add(LoadCharactersRoutineEachFrame());
      LoopParametersLoopScheduler.add(LoadCharactersRoutineEnd(snapshot));
      LoopParametersLoopScheduler.add(LoopParametersLoopEndIteration(LoopParametersLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function LoopParametersLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(LoopParameters);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function LoopParametersLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function pracitce_wrdsLoopBegin(pracitce_wrdsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    pracitce_wrds = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 6, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'testSymbols2.xlsx', '0:6'),
      seed: undefined, name: 'pracitce_wrds'
    });
    psychoJS.experiment.addLoop(pracitce_wrds); // add the loop to the experiment
    currentLoop = pracitce_wrds;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPracitce_wrd of pracitce_wrds) {
      snapshot = pracitce_wrds.getSnapshot();
      pracitce_wrdsLoopScheduler.add(importConditions(snapshot));
      pracitce_wrdsLoopScheduler.add(practice_wrdssRoutineBegin(snapshot));
      pracitce_wrdsLoopScheduler.add(practice_wrdssRoutineEachFrame());
      pracitce_wrdsLoopScheduler.add(practice_wrdssRoutineEnd(snapshot));
      pracitce_wrdsLoopScheduler.add(plusBetweenRoutineBegin(snapshot));
      pracitce_wrdsLoopScheduler.add(plusBetweenRoutineEachFrame());
      pracitce_wrdsLoopScheduler.add(plusBetweenRoutineEnd(snapshot));
      pracitce_wrdsLoopScheduler.add(pracitce_wrdsLoopEndIteration(pracitce_wrdsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function pracitce_wrdsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(pracitce_wrds);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function pracitce_wrdsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function practice_imagessLoopBegin(practice_imagessLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_imagess = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 6, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'testSymbols2.xlsx', '7:13'),
      seed: undefined, name: 'practice_imagess'
    });
    psychoJS.experiment.addLoop(practice_imagess); // add the loop to the experiment
    currentLoop = practice_imagess;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPractice_images of practice_imagess) {
      snapshot = practice_imagess.getSnapshot();
      practice_imagessLoopScheduler.add(importConditions(snapshot));
      practice_imagessLoopScheduler.add(practice_imagesRoutineBegin(snapshot));
      practice_imagessLoopScheduler.add(practice_imagesRoutineEachFrame());
      practice_imagessLoopScheduler.add(practice_imagesRoutineEnd(snapshot));
      practice_imagessLoopScheduler.add(plusBetweenRoutineBegin(snapshot));
      practice_imagessLoopScheduler.add(plusBetweenRoutineEachFrame());
      practice_imagessLoopScheduler.add(plusBetweenRoutineEnd(snapshot));
      practice_imagessLoopScheduler.add(practice_imagessLoopEndIteration(practice_imagessLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function practice_imagessLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_imagess);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function practice_imagessLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function practice_testtLoopBegin(practice_testtLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_testt = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 12, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'practice_testt'
    });
    psychoJS.experiment.addLoop(practice_testt); // add the loop to the experiment
    currentLoop = practice_testt;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPractice_testt of practice_testt) {
      snapshot = practice_testt.getSnapshot();
      practice_testtLoopScheduler.add(importConditions(snapshot));
      practice_testtLoopScheduler.add(practice_testRoutineBegin(snapshot));
      practice_testtLoopScheduler.add(practice_testRoutineEachFrame());
      practice_testtLoopScheduler.add(practice_testRoutineEnd(snapshot));
      practice_testtLoopScheduler.add(checkForCorr_5RoutineBegin(snapshot));
      practice_testtLoopScheduler.add(checkForCorr_5RoutineEachFrame());
      practice_testtLoopScheduler.add(checkForCorr_5RoutineEnd(snapshot));
      const checkLoopLoopScheduler = new Scheduler(psychoJS);
      practice_testtLoopScheduler.add(checkLoopLoopBegin(checkLoopLoopScheduler, snapshot));
      practice_testtLoopScheduler.add(checkLoopLoopScheduler);
      practice_testtLoopScheduler.add(checkLoopLoopEnd);
      const xmarkLoopLoopScheduler = new Scheduler(psychoJS);
      practice_testtLoopScheduler.add(xmarkLoopLoopBegin(xmarkLoopLoopScheduler, snapshot));
      practice_testtLoopScheduler.add(xmarkLoopLoopScheduler);
      practice_testtLoopScheduler.add(xmarkLoopLoopEnd);
      practice_testtLoopScheduler.add(resetRepsRoutineBegin(snapshot));
      practice_testtLoopScheduler.add(resetRepsRoutineEachFrame());
      practice_testtLoopScheduler.add(resetRepsRoutineEnd(snapshot));
      practice_testtLoopScheduler.add(blank500RoutineBegin(snapshot));
      practice_testtLoopScheduler.add(blank500RoutineEachFrame());
      practice_testtLoopScheduler.add(blank500RoutineEnd(snapshot));
      practice_testtLoopScheduler.add(practice_testtLoopEndIteration(practice_testtLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function checkLoopLoopBegin(checkLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    checkLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: checkmark_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'checkLoop'
    });
    psychoJS.experiment.addLoop(checkLoop); // add the loop to the experiment
    currentLoop = checkLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCheckLoop of checkLoop) {
      snapshot = checkLoop.getSnapshot();
      checkLoopLoopScheduler.add(importConditions(snapshot));
      checkLoopLoopScheduler.add(checkmarkRoutineBegin(snapshot));
      checkLoopLoopScheduler.add(checkmarkRoutineEachFrame());
      checkLoopLoopScheduler.add(checkmarkRoutineEnd(snapshot));
      checkLoopLoopScheduler.add(checkLoopLoopEndIteration(checkLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function checkLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(checkLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function checkLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function xmarkLoopLoopBegin(xmarkLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    xmarkLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: xmark_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'xmarkLoop'
    });
    psychoJS.experiment.addLoop(xmarkLoop); // add the loop to the experiment
    currentLoop = xmarkLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisXmarkLoop of xmarkLoop) {
      snapshot = xmarkLoop.getSnapshot();
      xmarkLoopLoopScheduler.add(importConditions(snapshot));
      xmarkLoopLoopScheduler.add(xmarkRoutineBegin(snapshot));
      xmarkLoopLoopScheduler.add(xmarkRoutineEachFrame());
      xmarkLoopLoopScheduler.add(xmarkRoutineEnd(snapshot));
      xmarkLoopLoopScheduler.add(xmarkLoopLoopEndIteration(xmarkLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function xmarkLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(xmarkLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function xmarkLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function practice_testtLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_testt);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function practice_testtLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function LearningSetOneLoopBegin(LearningSetOneLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    LearningSetOne = new TrialHandler({
      psychoJS: psychoJS,
      nReps: numReps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'LearningSetOne'
    });
    psychoJS.experiment.addLoop(LearningSetOne); // add the loop to the experiment
    currentLoop = LearningSetOne;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLearningSetOne of LearningSetOne) {
      snapshot = LearningSetOne.getSnapshot();
      LearningSetOneLoopScheduler.add(importConditions(snapshot));
      LearningSetOneLoopScheduler.add(randomize_setRoutineBegin(snapshot));
      LearningSetOneLoopScheduler.add(randomize_setRoutineEachFrame());
      LearningSetOneLoopScheduler.add(randomize_setRoutineEnd(snapshot));
      const setOneLoopScheduler = new Scheduler(psychoJS);
      LearningSetOneLoopScheduler.add(setOneLoopBegin(setOneLoopScheduler, snapshot));
      LearningSetOneLoopScheduler.add(setOneLoopScheduler);
      LearningSetOneLoopScheduler.add(setOneLoopEnd);
      LearningSetOneLoopScheduler.add(breakBetweenRepeatsRoutineBegin(snapshot));
      LearningSetOneLoopScheduler.add(breakBetweenRepeatsRoutineEachFrame());
      LearningSetOneLoopScheduler.add(breakBetweenRepeatsRoutineEnd(snapshot));
      LearningSetOneLoopScheduler.add(LearningSetOneLoopEndIteration(LearningSetOneLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function setOneLoopBegin(setOneLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    setOne = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 12, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'setOne'
    });
    psychoJS.experiment.addLoop(setOne); // add the loop to the experiment
    currentLoop = setOne;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisSetOne of setOne) {
      snapshot = setOne.getSnapshot();
      setOneLoopScheduler.add(importConditions(snapshot));
      setOneLoopScheduler.add(IncrementRoutineBegin(snapshot));
      setOneLoopScheduler.add(IncrementRoutineEachFrame());
      setOneLoopScheduler.add(IncrementRoutineEnd(snapshot));
      const nreps_A1LoopScheduler = new Scheduler(psychoJS);
      setOneLoopScheduler.add(nreps_A1LoopBegin(nreps_A1LoopScheduler, snapshot));
      setOneLoopScheduler.add(nreps_A1LoopScheduler);
      setOneLoopScheduler.add(nreps_A1LoopEnd);
      const nreps_B1LoopScheduler = new Scheduler(psychoJS);
      setOneLoopScheduler.add(nreps_B1LoopBegin(nreps_B1LoopScheduler, snapshot));
      setOneLoopScheduler.add(nreps_B1LoopScheduler);
      setOneLoopScheduler.add(nreps_B1LoopEnd);
      setOneLoopScheduler.add(plusBetweenRoutineBegin(snapshot));
      setOneLoopScheduler.add(plusBetweenRoutineEachFrame());
      setOneLoopScheduler.add(plusBetweenRoutineEnd(snapshot));
      setOneLoopScheduler.add(setOneLoopEndIteration(setOneLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function nreps_A1LoopBegin(nreps_A1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    nreps_A1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nreps_A, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'nreps_A1'
    });
    psychoJS.experiment.addLoop(nreps_A1); // add the loop to the experiment
    currentLoop = nreps_A1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNreps_A1 of nreps_A1) {
      snapshot = nreps_A1.getSnapshot();
      nreps_A1LoopScheduler.add(importConditions(snapshot));
      nreps_A1LoopScheduler.add(amharic1_ARoutineBegin(snapshot));
      nreps_A1LoopScheduler.add(amharic1_ARoutineEachFrame());
      nreps_A1LoopScheduler.add(amharic1_ARoutineEnd(snapshot));
      nreps_A1LoopScheduler.add(nreps_A1LoopEndIteration(nreps_A1LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function nreps_A1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(nreps_A1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function nreps_A1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function nreps_B1LoopBegin(nreps_B1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    nreps_B1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nreps_B, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'nreps_B1'
    });
    psychoJS.experiment.addLoop(nreps_B1); // add the loop to the experiment
    currentLoop = nreps_B1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNreps_B1 of nreps_B1) {
      snapshot = nreps_B1.getSnapshot();
      nreps_B1LoopScheduler.add(importConditions(snapshot));
      nreps_B1LoopScheduler.add(amharic1_BRoutineBegin(snapshot));
      nreps_B1LoopScheduler.add(amharic1_BRoutineEachFrame());
      nreps_B1LoopScheduler.add(amharic1_BRoutineEnd(snapshot));
      nreps_B1LoopScheduler.add(nreps_B1LoopEndIteration(nreps_B1LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function nreps_B1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(nreps_B1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function nreps_B1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function setOneLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(setOne);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function setOneLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function LearningSetOneLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(LearningSetOne);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function LearningSetOneLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function testSet1LoopBegin(testSet1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    testSet1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 12, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'testSet1'
    });
    psychoJS.experiment.addLoop(testSet1); // add the loop to the experiment
    currentLoop = testSet1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTestSet1 of testSet1) {
      snapshot = testSet1.getSnapshot();
      testSet1LoopScheduler.add(importConditions(snapshot));
      testSet1LoopScheduler.add(test1_NEWRoutineBegin(snapshot));
      testSet1LoopScheduler.add(test1_NEWRoutineEachFrame());
      testSet1LoopScheduler.add(test1_NEWRoutineEnd(snapshot));
      testSet1LoopScheduler.add(checkForCorrRoutineBegin(snapshot));
      testSet1LoopScheduler.add(checkForCorrRoutineEachFrame());
      testSet1LoopScheduler.add(checkForCorrRoutineEnd(snapshot));
      const checkloopLoopScheduler = new Scheduler(psychoJS);
      testSet1LoopScheduler.add(checkloopLoopBegin(checkloopLoopScheduler, snapshot));
      testSet1LoopScheduler.add(checkloopLoopScheduler);
      testSet1LoopScheduler.add(checkloopLoopEnd);
      const xloopLoopScheduler = new Scheduler(psychoJS);
      testSet1LoopScheduler.add(xloopLoopBegin(xloopLoopScheduler, snapshot));
      testSet1LoopScheduler.add(xloopLoopScheduler);
      testSet1LoopScheduler.add(xloopLoopEnd);
      testSet1LoopScheduler.add(resetRepsRoutineBegin(snapshot));
      testSet1LoopScheduler.add(resetRepsRoutineEachFrame());
      testSet1LoopScheduler.add(resetRepsRoutineEnd(snapshot));
      testSet1LoopScheduler.add(blank500RoutineBegin(snapshot));
      testSet1LoopScheduler.add(blank500RoutineEachFrame());
      testSet1LoopScheduler.add(blank500RoutineEnd(snapshot));
      testSet1LoopScheduler.add(testSet1LoopEndIteration(testSet1LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function checkloopLoopBegin(checkloopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    checkloop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: checkmark_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'checkloop'
    });
    psychoJS.experiment.addLoop(checkloop); // add the loop to the experiment
    currentLoop = checkloop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCheckloop of checkloop) {
      snapshot = checkloop.getSnapshot();
      checkloopLoopScheduler.add(importConditions(snapshot));
      checkloopLoopScheduler.add(checkmarkRoutineBegin(snapshot));
      checkloopLoopScheduler.add(checkmarkRoutineEachFrame());
      checkloopLoopScheduler.add(checkmarkRoutineEnd(snapshot));
      checkloopLoopScheduler.add(checkloopLoopEndIteration(checkloopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function checkloopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(checkloop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function checkloopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function xloopLoopBegin(xloopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    xloop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: xmark_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'xloop'
    });
    psychoJS.experiment.addLoop(xloop); // add the loop to the experiment
    currentLoop = xloop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisXloop of xloop) {
      snapshot = xloop.getSnapshot();
      xloopLoopScheduler.add(importConditions(snapshot));
      xloopLoopScheduler.add(xmarkRoutineBegin(snapshot));
      xloopLoopScheduler.add(xmarkRoutineEachFrame());
      xloopLoopScheduler.add(xmarkRoutineEnd(snapshot));
      xloopLoopScheduler.add(xloopLoopEndIteration(xloopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function xloopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(xloop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function xloopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function testSet1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(testSet1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function testSet1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function LearningSetTwoLoopBegin(LearningSetTwoLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    LearningSetTwo = new TrialHandler({
      psychoJS: psychoJS,
      nReps: numReps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'LearningSetTwo'
    });
    psychoJS.experiment.addLoop(LearningSetTwo); // add the loop to the experiment
    currentLoop = LearningSetTwo;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLearningSetTwo of LearningSetTwo) {
      snapshot = LearningSetTwo.getSnapshot();
      LearningSetTwoLoopScheduler.add(importConditions(snapshot));
      LearningSetTwoLoopScheduler.add(randomize_setRoutineBegin(snapshot));
      LearningSetTwoLoopScheduler.add(randomize_setRoutineEachFrame());
      LearningSetTwoLoopScheduler.add(randomize_setRoutineEnd(snapshot));
      const setTwoLoopScheduler = new Scheduler(psychoJS);
      LearningSetTwoLoopScheduler.add(setTwoLoopBegin(setTwoLoopScheduler, snapshot));
      LearningSetTwoLoopScheduler.add(setTwoLoopScheduler);
      LearningSetTwoLoopScheduler.add(setTwoLoopEnd);
      LearningSetTwoLoopScheduler.add(breakBetweenRepeatsRoutineBegin(snapshot));
      LearningSetTwoLoopScheduler.add(breakBetweenRepeatsRoutineEachFrame());
      LearningSetTwoLoopScheduler.add(breakBetweenRepeatsRoutineEnd(snapshot));
      LearningSetTwoLoopScheduler.add(LearningSetTwoLoopEndIteration(LearningSetTwoLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function setTwoLoopBegin(setTwoLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    setTwo = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 12, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'setTwo'
    });
    psychoJS.experiment.addLoop(setTwo); // add the loop to the experiment
    currentLoop = setTwo;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisSetTwo of setTwo) {
      snapshot = setTwo.getSnapshot();
      setTwoLoopScheduler.add(importConditions(snapshot));
      setTwoLoopScheduler.add(IncrementRoutineBegin(snapshot));
      setTwoLoopScheduler.add(IncrementRoutineEachFrame());
      setTwoLoopScheduler.add(IncrementRoutineEnd(snapshot));
      const nreps_A2LoopScheduler = new Scheduler(psychoJS);
      setTwoLoopScheduler.add(nreps_A2LoopBegin(nreps_A2LoopScheduler, snapshot));
      setTwoLoopScheduler.add(nreps_A2LoopScheduler);
      setTwoLoopScheduler.add(nreps_A2LoopEnd);
      const nreps_B2LoopScheduler = new Scheduler(psychoJS);
      setTwoLoopScheduler.add(nreps_B2LoopBegin(nreps_B2LoopScheduler, snapshot));
      setTwoLoopScheduler.add(nreps_B2LoopScheduler);
      setTwoLoopScheduler.add(nreps_B2LoopEnd);
      setTwoLoopScheduler.add(plusBetweenRoutineBegin(snapshot));
      setTwoLoopScheduler.add(plusBetweenRoutineEachFrame());
      setTwoLoopScheduler.add(plusBetweenRoutineEnd(snapshot));
      setTwoLoopScheduler.add(setTwoLoopEndIteration(setTwoLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function nreps_A2LoopBegin(nreps_A2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    nreps_A2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nreps_A, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'nreps_A2'
    });
    psychoJS.experiment.addLoop(nreps_A2); // add the loop to the experiment
    currentLoop = nreps_A2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNreps_A2 of nreps_A2) {
      snapshot = nreps_A2.getSnapshot();
      nreps_A2LoopScheduler.add(importConditions(snapshot));
      nreps_A2LoopScheduler.add(amharic2_ARoutineBegin(snapshot));
      nreps_A2LoopScheduler.add(amharic2_ARoutineEachFrame());
      nreps_A2LoopScheduler.add(amharic2_ARoutineEnd(snapshot));
      nreps_A2LoopScheduler.add(nreps_A2LoopEndIteration(nreps_A2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function nreps_A2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(nreps_A2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function nreps_A2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function nreps_B2LoopBegin(nreps_B2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    nreps_B2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nreps_B, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'nreps_B2'
    });
    psychoJS.experiment.addLoop(nreps_B2); // add the loop to the experiment
    currentLoop = nreps_B2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNreps_B2 of nreps_B2) {
      snapshot = nreps_B2.getSnapshot();
      nreps_B2LoopScheduler.add(importConditions(snapshot));
      nreps_B2LoopScheduler.add(amharic2_BRoutineBegin(snapshot));
      nreps_B2LoopScheduler.add(amharic2_BRoutineEachFrame());
      nreps_B2LoopScheduler.add(amharic2_BRoutineEnd(snapshot));
      nreps_B2LoopScheduler.add(nreps_B2LoopEndIteration(nreps_B2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function nreps_B2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(nreps_B2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function nreps_B2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function setTwoLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(setTwo);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function setTwoLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function LearningSetTwoLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(LearningSetTwo);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function LearningSetTwoLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function testSet2LoopBegin(testSet2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    testSet2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 12, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'testSet2'
    });
    psychoJS.experiment.addLoop(testSet2); // add the loop to the experiment
    currentLoop = testSet2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTestSet2 of testSet2) {
      snapshot = testSet2.getSnapshot();
      testSet2LoopScheduler.add(importConditions(snapshot));
      testSet2LoopScheduler.add(test2_NEWRoutineBegin(snapshot));
      testSet2LoopScheduler.add(test2_NEWRoutineEachFrame());
      testSet2LoopScheduler.add(test2_NEWRoutineEnd(snapshot));
      testSet2LoopScheduler.add(checkForCorr_2RoutineBegin(snapshot));
      testSet2LoopScheduler.add(checkForCorr_2RoutineEachFrame());
      testSet2LoopScheduler.add(checkForCorr_2RoutineEnd(snapshot));
      const checkloop2LoopScheduler = new Scheduler(psychoJS);
      testSet2LoopScheduler.add(checkloop2LoopBegin(checkloop2LoopScheduler, snapshot));
      testSet2LoopScheduler.add(checkloop2LoopScheduler);
      testSet2LoopScheduler.add(checkloop2LoopEnd);
      const xmark2LoopScheduler = new Scheduler(psychoJS);
      testSet2LoopScheduler.add(xmark2LoopBegin(xmark2LoopScheduler, snapshot));
      testSet2LoopScheduler.add(xmark2LoopScheduler);
      testSet2LoopScheduler.add(xmark2LoopEnd);
      testSet2LoopScheduler.add(resetRepsRoutineBegin(snapshot));
      testSet2LoopScheduler.add(resetRepsRoutineEachFrame());
      testSet2LoopScheduler.add(resetRepsRoutineEnd(snapshot));
      testSet2LoopScheduler.add(blank500RoutineBegin(snapshot));
      testSet2LoopScheduler.add(blank500RoutineEachFrame());
      testSet2LoopScheduler.add(blank500RoutineEnd(snapshot));
      testSet2LoopScheduler.add(testSet2LoopEndIteration(testSet2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function checkloop2LoopBegin(checkloop2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    checkloop2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: checkmark_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'checkloop2'
    });
    psychoJS.experiment.addLoop(checkloop2); // add the loop to the experiment
    currentLoop = checkloop2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCheckloop2 of checkloop2) {
      snapshot = checkloop2.getSnapshot();
      checkloop2LoopScheduler.add(importConditions(snapshot));
      checkloop2LoopScheduler.add(checkmarkRoutineBegin(snapshot));
      checkloop2LoopScheduler.add(checkmarkRoutineEachFrame());
      checkloop2LoopScheduler.add(checkmarkRoutineEnd(snapshot));
      checkloop2LoopScheduler.add(checkloop2LoopEndIteration(checkloop2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function checkloop2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(checkloop2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function checkloop2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function xmark2LoopBegin(xmark2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    xmark2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: xmark_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'xmark2'
    });
    psychoJS.experiment.addLoop(xmark2); // add the loop to the experiment
    currentLoop = xmark2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisXmark2 of xmark2) {
      snapshot = xmark2.getSnapshot();
      xmark2LoopScheduler.add(importConditions(snapshot));
      xmark2LoopScheduler.add(xmarkRoutineBegin(snapshot));
      xmark2LoopScheduler.add(xmarkRoutineEachFrame());
      xmark2LoopScheduler.add(xmarkRoutineEnd(snapshot));
      xmark2LoopScheduler.add(xmark2LoopEndIteration(xmark2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function xmark2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(xmark2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function xmark2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function testSet2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(testSet2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function testSet2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function LearningSetThreeLoopBegin(LearningSetThreeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    LearningSetThree = new TrialHandler({
      psychoJS: psychoJS,
      nReps: numReps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'LearningSetThree'
    });
    psychoJS.experiment.addLoop(LearningSetThree); // add the loop to the experiment
    currentLoop = LearningSetThree;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLearningSetThree of LearningSetThree) {
      snapshot = LearningSetThree.getSnapshot();
      LearningSetThreeLoopScheduler.add(importConditions(snapshot));
      LearningSetThreeLoopScheduler.add(randomize_setRoutineBegin(snapshot));
      LearningSetThreeLoopScheduler.add(randomize_setRoutineEachFrame());
      LearningSetThreeLoopScheduler.add(randomize_setRoutineEnd(snapshot));
      const setThreeLoopScheduler = new Scheduler(psychoJS);
      LearningSetThreeLoopScheduler.add(setThreeLoopBegin(setThreeLoopScheduler, snapshot));
      LearningSetThreeLoopScheduler.add(setThreeLoopScheduler);
      LearningSetThreeLoopScheduler.add(setThreeLoopEnd);
      LearningSetThreeLoopScheduler.add(breakBetweenRepeatsRoutineBegin(snapshot));
      LearningSetThreeLoopScheduler.add(breakBetweenRepeatsRoutineEachFrame());
      LearningSetThreeLoopScheduler.add(breakBetweenRepeatsRoutineEnd(snapshot));
      LearningSetThreeLoopScheduler.add(LearningSetThreeLoopEndIteration(LearningSetThreeLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function setThreeLoopBegin(setThreeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    setThree = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 12, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'setThree'
    });
    psychoJS.experiment.addLoop(setThree); // add the loop to the experiment
    currentLoop = setThree;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisSetThree of setThree) {
      snapshot = setThree.getSnapshot();
      setThreeLoopScheduler.add(importConditions(snapshot));
      setThreeLoopScheduler.add(IncrementRoutineBegin(snapshot));
      setThreeLoopScheduler.add(IncrementRoutineEachFrame());
      setThreeLoopScheduler.add(IncrementRoutineEnd(snapshot));
      const nreps_A3LoopScheduler = new Scheduler(psychoJS);
      setThreeLoopScheduler.add(nreps_A3LoopBegin(nreps_A3LoopScheduler, snapshot));
      setThreeLoopScheduler.add(nreps_A3LoopScheduler);
      setThreeLoopScheduler.add(nreps_A3LoopEnd);
      const nreps_B3LoopScheduler = new Scheduler(psychoJS);
      setThreeLoopScheduler.add(nreps_B3LoopBegin(nreps_B3LoopScheduler, snapshot));
      setThreeLoopScheduler.add(nreps_B3LoopScheduler);
      setThreeLoopScheduler.add(nreps_B3LoopEnd);
      setThreeLoopScheduler.add(plusBetweenRoutineBegin(snapshot));
      setThreeLoopScheduler.add(plusBetweenRoutineEachFrame());
      setThreeLoopScheduler.add(plusBetweenRoutineEnd(snapshot));
      setThreeLoopScheduler.add(setThreeLoopEndIteration(setThreeLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function nreps_A3LoopBegin(nreps_A3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    nreps_A3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nreps_A, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'nreps_A3'
    });
    psychoJS.experiment.addLoop(nreps_A3); // add the loop to the experiment
    currentLoop = nreps_A3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNreps_A3 of nreps_A3) {
      snapshot = nreps_A3.getSnapshot();
      nreps_A3LoopScheduler.add(importConditions(snapshot));
      nreps_A3LoopScheduler.add(amharic3_ARoutineBegin(snapshot));
      nreps_A3LoopScheduler.add(amharic3_ARoutineEachFrame());
      nreps_A3LoopScheduler.add(amharic3_ARoutineEnd(snapshot));
      nreps_A3LoopScheduler.add(nreps_A3LoopEndIteration(nreps_A3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function nreps_A3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(nreps_A3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function nreps_A3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function nreps_B3LoopBegin(nreps_B3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    nreps_B3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nreps_B, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'nreps_B3'
    });
    psychoJS.experiment.addLoop(nreps_B3); // add the loop to the experiment
    currentLoop = nreps_B3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNreps_B3 of nreps_B3) {
      snapshot = nreps_B3.getSnapshot();
      nreps_B3LoopScheduler.add(importConditions(snapshot));
      nreps_B3LoopScheduler.add(amharic3_BRoutineBegin(snapshot));
      nreps_B3LoopScheduler.add(amharic3_BRoutineEachFrame());
      nreps_B3LoopScheduler.add(amharic3_BRoutineEnd(snapshot));
      nreps_B3LoopScheduler.add(nreps_B3LoopEndIteration(nreps_B3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function nreps_B3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(nreps_B3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function nreps_B3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function setThreeLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(setThree);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function setThreeLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function LearningSetThreeLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(LearningSetThree);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function LearningSetThreeLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function testSet3LoopBegin(testSet3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    testSet3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 12, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'testSet3'
    });
    psychoJS.experiment.addLoop(testSet3); // add the loop to the experiment
    currentLoop = testSet3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTestSet3 of testSet3) {
      snapshot = testSet3.getSnapshot();
      testSet3LoopScheduler.add(importConditions(snapshot));
      testSet3LoopScheduler.add(test3_NEWRoutineBegin(snapshot));
      testSet3LoopScheduler.add(test3_NEWRoutineEachFrame());
      testSet3LoopScheduler.add(test3_NEWRoutineEnd(snapshot));
      testSet3LoopScheduler.add(checkForCorr_3RoutineBegin(snapshot));
      testSet3LoopScheduler.add(checkForCorr_3RoutineEachFrame());
      testSet3LoopScheduler.add(checkForCorr_3RoutineEnd(snapshot));
      const checkloops3LoopScheduler = new Scheduler(psychoJS);
      testSet3LoopScheduler.add(checkloops3LoopBegin(checkloops3LoopScheduler, snapshot));
      testSet3LoopScheduler.add(checkloops3LoopScheduler);
      testSet3LoopScheduler.add(checkloops3LoopEnd);
      const xmarkloops3LoopScheduler = new Scheduler(psychoJS);
      testSet3LoopScheduler.add(xmarkloops3LoopBegin(xmarkloops3LoopScheduler, snapshot));
      testSet3LoopScheduler.add(xmarkloops3LoopScheduler);
      testSet3LoopScheduler.add(xmarkloops3LoopEnd);
      testSet3LoopScheduler.add(resetRepsRoutineBegin(snapshot));
      testSet3LoopScheduler.add(resetRepsRoutineEachFrame());
      testSet3LoopScheduler.add(resetRepsRoutineEnd(snapshot));
      testSet3LoopScheduler.add(blank500RoutineBegin(snapshot));
      testSet3LoopScheduler.add(blank500RoutineEachFrame());
      testSet3LoopScheduler.add(blank500RoutineEnd(snapshot));
      testSet3LoopScheduler.add(testSet3LoopEndIteration(testSet3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function checkloops3LoopBegin(checkloops3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    checkloops3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: checkmark_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'checkloops3'
    });
    psychoJS.experiment.addLoop(checkloops3); // add the loop to the experiment
    currentLoop = checkloops3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCheckloops3 of checkloops3) {
      snapshot = checkloops3.getSnapshot();
      checkloops3LoopScheduler.add(importConditions(snapshot));
      checkloops3LoopScheduler.add(checkmarkRoutineBegin(snapshot));
      checkloops3LoopScheduler.add(checkmarkRoutineEachFrame());
      checkloops3LoopScheduler.add(checkmarkRoutineEnd(snapshot));
      checkloops3LoopScheduler.add(checkloops3LoopEndIteration(checkloops3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function checkloops3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(checkloops3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function checkloops3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function xmarkloops3LoopBegin(xmarkloops3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    xmarkloops3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: xmark_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'xmarkloops3'
    });
    psychoJS.experiment.addLoop(xmarkloops3); // add the loop to the experiment
    currentLoop = xmarkloops3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisXmarkloops3 of xmarkloops3) {
      snapshot = xmarkloops3.getSnapshot();
      xmarkloops3LoopScheduler.add(importConditions(snapshot));
      xmarkloops3LoopScheduler.add(xmarkRoutineBegin(snapshot));
      xmarkloops3LoopScheduler.add(xmarkRoutineEachFrame());
      xmarkloops3LoopScheduler.add(xmarkRoutineEnd(snapshot));
      xmarkloops3LoopScheduler.add(xmarkloops3LoopEndIteration(xmarkloops3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function xmarkloops3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(xmarkloops3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function xmarkloops3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function testSet3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(testSet3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function testSet3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function LearningSetFourLoopBegin(LearningSetFourLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    LearningSetFour = new TrialHandler({
      psychoJS: psychoJS,
      nReps: numReps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'LearningSetFour'
    });
    psychoJS.experiment.addLoop(LearningSetFour); // add the loop to the experiment
    currentLoop = LearningSetFour;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLearningSetFour of LearningSetFour) {
      snapshot = LearningSetFour.getSnapshot();
      LearningSetFourLoopScheduler.add(importConditions(snapshot));
      LearningSetFourLoopScheduler.add(randomize_setRoutineBegin(snapshot));
      LearningSetFourLoopScheduler.add(randomize_setRoutineEachFrame());
      LearningSetFourLoopScheduler.add(randomize_setRoutineEnd(snapshot));
      const setFourLoopScheduler = new Scheduler(psychoJS);
      LearningSetFourLoopScheduler.add(setFourLoopBegin(setFourLoopScheduler, snapshot));
      LearningSetFourLoopScheduler.add(setFourLoopScheduler);
      LearningSetFourLoopScheduler.add(setFourLoopEnd);
      LearningSetFourLoopScheduler.add(breakBetweenRepeatsRoutineBegin(snapshot));
      LearningSetFourLoopScheduler.add(breakBetweenRepeatsRoutineEachFrame());
      LearningSetFourLoopScheduler.add(breakBetweenRepeatsRoutineEnd(snapshot));
      LearningSetFourLoopScheduler.add(LearningSetFourLoopEndIteration(LearningSetFourLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function setFourLoopBegin(setFourLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    setFour = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 12, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'setFour'
    });
    psychoJS.experiment.addLoop(setFour); // add the loop to the experiment
    currentLoop = setFour;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisSetFour of setFour) {
      snapshot = setFour.getSnapshot();
      setFourLoopScheduler.add(importConditions(snapshot));
      setFourLoopScheduler.add(IncrementRoutineBegin(snapshot));
      setFourLoopScheduler.add(IncrementRoutineEachFrame());
      setFourLoopScheduler.add(IncrementRoutineEnd(snapshot));
      const nreps_A4LoopScheduler = new Scheduler(psychoJS);
      setFourLoopScheduler.add(nreps_A4LoopBegin(nreps_A4LoopScheduler, snapshot));
      setFourLoopScheduler.add(nreps_A4LoopScheduler);
      setFourLoopScheduler.add(nreps_A4LoopEnd);
      const nreps_B4LoopScheduler = new Scheduler(psychoJS);
      setFourLoopScheduler.add(nreps_B4LoopBegin(nreps_B4LoopScheduler, snapshot));
      setFourLoopScheduler.add(nreps_B4LoopScheduler);
      setFourLoopScheduler.add(nreps_B4LoopEnd);
      setFourLoopScheduler.add(plusBetweenRoutineBegin(snapshot));
      setFourLoopScheduler.add(plusBetweenRoutineEachFrame());
      setFourLoopScheduler.add(plusBetweenRoutineEnd(snapshot));
      setFourLoopScheduler.add(setFourLoopEndIteration(setFourLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function nreps_A4LoopBegin(nreps_A4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    nreps_A4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nreps_A, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'nreps_A4'
    });
    psychoJS.experiment.addLoop(nreps_A4); // add the loop to the experiment
    currentLoop = nreps_A4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNreps_A4 of nreps_A4) {
      snapshot = nreps_A4.getSnapshot();
      nreps_A4LoopScheduler.add(importConditions(snapshot));
      nreps_A4LoopScheduler.add(amharic4_ARoutineBegin(snapshot));
      nreps_A4LoopScheduler.add(amharic4_ARoutineEachFrame());
      nreps_A4LoopScheduler.add(amharic4_ARoutineEnd(snapshot));
      nreps_A4LoopScheduler.add(nreps_A4LoopEndIteration(nreps_A4LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function nreps_A4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(nreps_A4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function nreps_A4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function nreps_B4LoopBegin(nreps_B4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    nreps_B4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nreps_B, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'nreps_B4'
    });
    psychoJS.experiment.addLoop(nreps_B4); // add the loop to the experiment
    currentLoop = nreps_B4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisNreps_B4 of nreps_B4) {
      snapshot = nreps_B4.getSnapshot();
      nreps_B4LoopScheduler.add(importConditions(snapshot));
      nreps_B4LoopScheduler.add(amharic4_BRoutineBegin(snapshot));
      nreps_B4LoopScheduler.add(amharic4_BRoutineEachFrame());
      nreps_B4LoopScheduler.add(amharic4_BRoutineEnd(snapshot));
      nreps_B4LoopScheduler.add(nreps_B4LoopEndIteration(nreps_B4LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function nreps_B4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(nreps_B4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function nreps_B4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function setFourLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(setFour);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function setFourLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function LearningSetFourLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(LearningSetFour);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function LearningSetFourLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function testSet4LoopBegin(testSet4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    testSet4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 12, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'testSet4'
    });
    psychoJS.experiment.addLoop(testSet4); // add the loop to the experiment
    currentLoop = testSet4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTestSet4 of testSet4) {
      snapshot = testSet4.getSnapshot();
      testSet4LoopScheduler.add(importConditions(snapshot));
      testSet4LoopScheduler.add(test4_NEWRoutineBegin(snapshot));
      testSet4LoopScheduler.add(test4_NEWRoutineEachFrame());
      testSet4LoopScheduler.add(test4_NEWRoutineEnd(snapshot));
      testSet4LoopScheduler.add(checkForCorr_4RoutineBegin(snapshot));
      testSet4LoopScheduler.add(checkForCorr_4RoutineEachFrame());
      testSet4LoopScheduler.add(checkForCorr_4RoutineEnd(snapshot));
      const checkmark_loop4LoopScheduler = new Scheduler(psychoJS);
      testSet4LoopScheduler.add(checkmark_loop4LoopBegin(checkmark_loop4LoopScheduler, snapshot));
      testSet4LoopScheduler.add(checkmark_loop4LoopScheduler);
      testSet4LoopScheduler.add(checkmark_loop4LoopEnd);
      const xmark_loop4LoopScheduler = new Scheduler(psychoJS);
      testSet4LoopScheduler.add(xmark_loop4LoopBegin(xmark_loop4LoopScheduler, snapshot));
      testSet4LoopScheduler.add(xmark_loop4LoopScheduler);
      testSet4LoopScheduler.add(xmark_loop4LoopEnd);
      testSet4LoopScheduler.add(resetRepsRoutineBegin(snapshot));
      testSet4LoopScheduler.add(resetRepsRoutineEachFrame());
      testSet4LoopScheduler.add(resetRepsRoutineEnd(snapshot));
      testSet4LoopScheduler.add(blank500RoutineBegin(snapshot));
      testSet4LoopScheduler.add(blank500RoutineEachFrame());
      testSet4LoopScheduler.add(blank500RoutineEnd(snapshot));
      testSet4LoopScheduler.add(testSet4LoopEndIteration(testSet4LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function checkmark_loop4LoopBegin(checkmark_loop4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    checkmark_loop4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: checkmark_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'checkmark_loop4'
    });
    psychoJS.experiment.addLoop(checkmark_loop4); // add the loop to the experiment
    currentLoop = checkmark_loop4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCheckmark_loop4 of checkmark_loop4) {
      snapshot = checkmark_loop4.getSnapshot();
      checkmark_loop4LoopScheduler.add(importConditions(snapshot));
      checkmark_loop4LoopScheduler.add(checkmarkRoutineBegin(snapshot));
      checkmark_loop4LoopScheduler.add(checkmarkRoutineEachFrame());
      checkmark_loop4LoopScheduler.add(checkmarkRoutineEnd(snapshot));
      checkmark_loop4LoopScheduler.add(checkmark_loop4LoopEndIteration(checkmark_loop4LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function checkmark_loop4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(checkmark_loop4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function checkmark_loop4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function xmark_loop4LoopBegin(xmark_loop4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    xmark_loop4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: xmark_reps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'xmark_loop4'
    });
    psychoJS.experiment.addLoop(xmark_loop4); // add the loop to the experiment
    currentLoop = xmark_loop4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisXmark_loop4 of xmark_loop4) {
      snapshot = xmark_loop4.getSnapshot();
      xmark_loop4LoopScheduler.add(importConditions(snapshot));
      xmark_loop4LoopScheduler.add(xmarkRoutineBegin(snapshot));
      xmark_loop4LoopScheduler.add(xmarkRoutineEachFrame());
      xmark_loop4LoopScheduler.add(xmarkRoutineEnd(snapshot));
      xmark_loop4LoopScheduler.add(xmark_loop4LoopEndIteration(xmark_loop4LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function xmark_loop4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(xmark_loop4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function xmark_loop4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function testSet4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(testSet4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function testSet4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function TrialsLoopBegin(TrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 24, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'Trials'
    });
    psychoJS.experiment.addLoop(Trials); // add the loop to the experiment
    currentLoop = Trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of Trials) {
      snapshot = Trials.getSnapshot();
      TrialsLoopScheduler.add(importConditions(snapshot));
      TrialsLoopScheduler.add(TestQuestionRoutineBegin(snapshot));
      TrialsLoopScheduler.add(TestQuestionRoutineEachFrame());
      TrialsLoopScheduler.add(TestQuestionRoutineEnd(snapshot));
      TrialsLoopScheduler.add(EvaluateRoutineBegin(snapshot));
      TrialsLoopScheduler.add(EvaluateRoutineEachFrame());
      TrialsLoopScheduler.add(EvaluateRoutineEnd(snapshot));
      TrialsLoopScheduler.add(TrialsLoopEndIteration(TrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function TrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(Trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function TrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function LoadCharactersRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'LoadCharacters' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    LoadCharactersClock.reset();
    routineTimer.reset();
    LoadCharactersMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codeLoader
    word_list1.push(words_set1);
    amharic_list1.push(amharic_set1);
    word_list2.push(words_set2);
    amharic_list2.push(amharic_set2);
    word_list3.push(words_set3);
    amharic_list3.push(amharic_set3);
    word_list4.push(words_set4);
    amharic_list4.push(amharic_set4);
    markers.push(symbols);
    practice_amharic.push(amharic_practices);
    practice_words.push(words_practice);
    characters_words[amharic_set1] = words_set1;
    characters_words[amharic_set2] = words_set2;
    characters_words[amharic_set3] = words_set3;
    characters_words[amharic_set4] = words_set4;
    
    psychoJS.experiment.addData('LoadCharacters.started', globalClock.getTime());
    LoadCharactersMaxDuration = null
    // keep track of which components have finished
    LoadCharactersComponents = [];
    
    for (const thisComponent of LoadCharactersComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function LoadCharactersRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'LoadCharacters' ---
    // get current time
    t = LoadCharactersClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of LoadCharactersComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function LoadCharactersRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'LoadCharacters' ---
    for (const thisComponent of LoadCharactersComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('LoadCharacters.stopped', globalClock.getTime());
    // the Routine "LoadCharacters" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function RemoveNoneRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RemoveNone' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    RemoveNoneClock.reset();
    routineTimer.reset();
    RemoveNoneMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from loadWordsAndRemoveNone
    word_list1.remove(null);
    amharic_list1.remove(null);
    word_list2.remove(null);
    amharic_list2.remove(null);
    word_list3.remove(null);
    amharic_list3.remove(null);
    word_list4.remove(null);
    amharic_list4.remove(null);
    delete characters_words[null];
    
    psychoJS.experiment.addData('RemoveNone.started', globalClock.getTime());
    RemoveNoneMaxDuration = null
    // keep track of which components have finished
    RemoveNoneComponents = [];
    
    for (const thisComponent of RemoveNoneComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function RemoveNoneRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RemoveNone' ---
    // get current time
    t = RemoveNoneClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RemoveNoneComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function RemoveNoneRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RemoveNone' ---
    for (const thisComponent of RemoveNoneComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RemoveNone.stopped', globalClock.getTime());
    // Run 'End Routine' code from loadWordsAndRemoveNone
    amharic_word_list1 = {};
    amharic_word_list2 = {};
    amharic_word_list3 = {};
    amharic_word_list4 = {};
    practice_list = {};
    for (var i, _pj_c = 0, _pj_a = util.range(12), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        amharic_word_list1[i] = [amharic_list1[i], word_list1[i], `pictures/${word_list1[i]}.jpg`.toString()];
        amharic_word_list2[i] = [amharic_list2[i], word_list2[i], `pictures/${word_list2[i]}.jpg`.toString()];
        amharic_word_list3[i] = [amharic_list3[i], word_list3[i], `pictures/${word_list3[i]}.jpg`.toString()];
        amharic_word_list4[i] = [amharic_list4[i], word_list4[i], `pictures/${word_list4[i]}.jpg`.toString()];
        practice_list[i] = [practice_amharic[i], practice_words[i], `pictures/${practice_words[i]}.jpg`.toString()];
    }
    for (var i, _pj_c = 0, _pj_a = util.range(12), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        console.log(amharic_word_list1[i]);
        console.log(amharic_word_list2[i]);
        console.log(amharic_word_list3[i]);
        console.log(amharic_word_list4[i]);
        console.log(practice_list[i]);
    }
    
    // the Routine "RemoveNone" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function GenerateQuestionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'GenerateQuestions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    GenerateQuestionsClock.reset();
    routineTimer.reset();
    GenerateQuestionsMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from genQuestions
    /* Syntax Error: Fix Python code */
    psychoJS.experiment.addData('GenerateQuestions.started', globalClock.getTime());
    GenerateQuestionsMaxDuration = null
    // keep track of which components have finished
    GenerateQuestionsComponents = [];
    
    for (const thisComponent of GenerateQuestionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function GenerateQuestionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'GenerateQuestions' ---
    // get current time
    t = GenerateQuestionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of GenerateQuestionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function GenerateQuestionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'GenerateQuestions' ---
    for (const thisComponent of GenerateQuestionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('GenerateQuestions.stopped', globalClock.getTime());
    // the Routine "GenerateQuestions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practice_welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_welcome' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice_welcomeClock.reset();
    routineTimer.reset();
    practice_welcomeMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    psychoJS.experiment.addData('practice_welcome.started', globalClock.getTime());
    practice_welcomeMaxDuration = null
    // keep track of which components have finished
    practice_welcomeComponents = [];
    practice_welcomeComponents.push(text_4);
    practice_welcomeComponents.push(key_resp_9);
    
    for (const thisComponent of practice_welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function practice_welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_welcome' ---
    // get current time
    t = practice_welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    
    // *key_resp_9* updates
    if (t >= 0.0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }
    
    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        key_resp_9.duration = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practice_welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_welcome' ---
    for (const thisComponent of practice_welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_9.corr, level);
    }
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        psychoJS.experiment.addData('key_resp_9.duration', key_resp_9.duration);
        routineTimer.reset();
        }
    
    key_resp_9.stop();
    // the Routine "practice_welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practice_wrdssRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_wrdss' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice_wrdssClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    practice_wrdssMaxDurationReached = false;
    // update component parameters for each repeat
    practice_amharicc.setText(amharic_practices);
    practice_wordssss.setText(words_practice);
    psychoJS.experiment.addData('practice_wrdss.started', globalClock.getTime());
    practice_wrdssMaxDuration = null
    // keep track of which components have finished
    practice_wrdssComponents = [];
    practice_wrdssComponents.push(practice_amharicc);
    practice_wrdssComponents.push(practice_wordssss);
    
    for (const thisComponent of practice_wrdssComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function practice_wrdssRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_wrdss' ---
    // get current time
    t = practice_wrdssClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_amharicc* updates
    if (t >= 0.0 && practice_amharicc.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_amharicc.tStart = t;  // (not accounting for frame time here)
      practice_amharicc.frameNStart = frameN;  // exact frame index
      
      practice_amharicc.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (practice_amharicc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_amharicc.setAutoDraw(false);
    }
    
    
    // *practice_wordssss* updates
    if (t >= 0.0 && practice_wordssss.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_wordssss.tStart = t;  // (not accounting for frame time here)
      practice_wordssss.frameNStart = frameN;  // exact frame index
      
      practice_wordssss.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (practice_wordssss.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_wordssss.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_wrdssComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practice_wrdssRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_wrdss' ---
    for (const thisComponent of practice_wrdssComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_wrdss.stopped', globalClock.getTime());
    if (practice_wrdssMaxDurationReached) {
        practice_wrdssClock.add(practice_wrdssMaxDuration);
    } else {
        practice_wrdssClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function plusBetweenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'plusBetween' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    plusBetweenClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    plusBetweenMaxDurationReached = false;
    // update component parameters for each repeat
    plus.setText('+');
    debugging_press_enter_to_skip_4.keys = undefined;
    debugging_press_enter_to_skip_4.rt = undefined;
    _debugging_press_enter_to_skip_4_allKeys = [];
    psychoJS.experiment.addData('plusBetween.started', globalClock.getTime());
    plusBetweenMaxDuration = null
    // keep track of which components have finished
    plusBetweenComponents = [];
    plusBetweenComponents.push(plus);
    plusBetweenComponents.push(debugging_press_enter_to_skip_4);
    
    for (const thisComponent of plusBetweenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function plusBetweenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'plusBetween' ---
    // get current time
    t = plusBetweenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *plus* updates
    if (t >= 0.0 && plus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      plus.tStart = t;  // (not accounting for frame time here)
      plus.frameNStart = frameN;  // exact frame index
      
      plus.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (plus.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      plus.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_4* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_4.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_4.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_4.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_4.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_4_allKeys = _debugging_press_enter_to_skip_4_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_4_allKeys.length > 0) {
        debugging_press_enter_to_skip_4.keys = _debugging_press_enter_to_skip_4_allKeys[_debugging_press_enter_to_skip_4_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_4.rt = _debugging_press_enter_to_skip_4_allKeys[_debugging_press_enter_to_skip_4_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_4.duration = _debugging_press_enter_to_skip_4_allKeys[_debugging_press_enter_to_skip_4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of plusBetweenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function plusBetweenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'plusBetween' ---
    for (const thisComponent of plusBetweenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('plusBetween.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_4.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_4.keys', debugging_press_enter_to_skip_4.keys);
    if (typeof debugging_press_enter_to_skip_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_4.rt', debugging_press_enter_to_skip_4.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_4.duration', debugging_press_enter_to_skip_4.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_4.stop();
    if (plusBetweenMaxDurationReached) {
        plusBetweenClock.add(plusBetweenMaxDuration);
    } else {
        plusBetweenClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function breakBetweenSetsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'breakBetweenSets' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    breakBetweenSetsClock.reset(routineTimer.getTime());
    routineTimer.add(30.000000);
    breakBetweenSetsMaxDurationReached = false;
    // update component parameters for each repeat
    debugging_press_enter_to_skip_8.keys = undefined;
    debugging_press_enter_to_skip_8.rt = undefined;
    _debugging_press_enter_to_skip_8_allKeys = [];
    psychoJS.experiment.addData('breakBetweenSets.started', globalClock.getTime());
    breakBetweenSetsMaxDuration = null
    // keep track of which components have finished
    breakBetweenSetsComponents = [];
    breakBetweenSetsComponents.push(cross);
    breakBetweenSetsComponents.push(debugging_press_enter_to_skip_8);
    
    for (const thisComponent of breakBetweenSetsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function breakBetweenSetsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'breakBetweenSets' ---
    // get current time
    t = breakBetweenSetsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cross* updates
    if (t >= 0.0 && cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cross.tStart = t;  // (not accounting for frame time here)
      cross.frameNStart = frameN;  // exact frame index
      
      cross.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cross.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_8* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_8.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_8.clearEvents(); });
    }
    
    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_8.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_8.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_8_allKeys = _debugging_press_enter_to_skip_8_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_8_allKeys.length > 0) {
        debugging_press_enter_to_skip_8.keys = _debugging_press_enter_to_skip_8_allKeys[_debugging_press_enter_to_skip_8_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_8.rt = _debugging_press_enter_to_skip_8_allKeys[_debugging_press_enter_to_skip_8_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_8.duration = _debugging_press_enter_to_skip_8_allKeys[_debugging_press_enter_to_skip_8_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of breakBetweenSetsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function breakBetweenSetsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'breakBetweenSets' ---
    for (const thisComponent of breakBetweenSetsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('breakBetweenSets.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_8.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_8.keys', debugging_press_enter_to_skip_8.keys);
    if (typeof debugging_press_enter_to_skip_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_8.rt', debugging_press_enter_to_skip_8.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_8.duration', debugging_press_enter_to_skip_8.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_8.stop();
    if (breakBetweenSetsMaxDurationReached) {
        breakBetweenSetsClock.add(breakBetweenSetsMaxDuration);
    } else {
        breakBetweenSetsClock.add(30.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practice_imagesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_images' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice_imagesClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    practice_imagesMaxDurationReached = false;
    // update component parameters for each repeat
    amharic_practice2.setText(amharic_practices);
    image_practice.setImage(image_practice);
    psychoJS.experiment.addData('practice_images.started', globalClock.getTime());
    practice_imagesMaxDuration = null
    // keep track of which components have finished
    practice_imagesComponents = [];
    practice_imagesComponents.push(amharic_practice2);
    practice_imagesComponents.push(image_practice);
    
    for (const thisComponent of practice_imagesComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function practice_imagesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_images' ---
    // get current time
    t = practice_imagesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *amharic_practice2* updates
    if (t >= 0.0 && amharic_practice2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      amharic_practice2.tStart = t;  // (not accounting for frame time here)
      amharic_practice2.frameNStart = frameN;  // exact frame index
      
      amharic_practice2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (amharic_practice2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      amharic_practice2.setAutoDraw(false);
    }
    
    
    // *image_practice* updates
    if (t >= 0.0 && image_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_practice.tStart = t;  // (not accounting for frame time here)
      image_practice.frameNStart = frameN;  // exact frame index
      
      image_practice.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_practice.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_imagesComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practice_imagesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_images' ---
    for (const thisComponent of practice_imagesComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_images.stopped', globalClock.getTime());
    if (practice_imagesMaxDurationReached) {
        practice_imagesClock.add(practice_imagesMaxDuration);
    } else {
        practice_imagesClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practice_testRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_test' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    practice_testClock.reset();
    routineTimer.reset();
    practice_testMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codeSymbol_9
    /* Syntax Error: Fix Python code */
    textAmharic_9.setText(amharic_p);
    textOptionA_9.setText(lottery_list_p[0]);
    textOptionB_9.setText(lottery_list_p[1]);
    textOptionC_9.setText(lottery_list_p[2]);
    textOptionD_9.setText(lottery_list_p[3]);
    textDiamond_8.setText(f'''     {lottery_list_p[0]}
       {lottery_list_p[1]}   {lottery_list_p[2]}
         {lottery_list_p[3]}''');
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    debugging_press_enter_to_skip_23.keys = undefined;
    debugging_press_enter_to_skip_23.rt = undefined;
    _debugging_press_enter_to_skip_23_allKeys = [];
    psychoJS.experiment.addData('practice_test.started', globalClock.getTime());
    practice_testMaxDuration = null
    // keep track of which components have finished
    practice_testComponents = [];
    practice_testComponents.push(textAmharic_9);
    practice_testComponents.push(textOptionA_9);
    practice_testComponents.push(textOptionB_9);
    practice_testComponents.push(textOptionC_9);
    practice_testComponents.push(textOptionD_9);
    practice_testComponents.push(textDiamond_8);
    practice_testComponents.push(key_resp_10);
    practice_testComponents.push(debugging_press_enter_to_skip_23);
    
    for (const thisComponent of practice_testComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function practice_testRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_test' ---
    // get current time
    t = practice_testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textAmharic_9* updates
    if (t >= 0.0 && textAmharic_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textAmharic_9.tStart = t;  // (not accounting for frame time here)
      textAmharic_9.frameNStart = frameN;  // exact frame index
      
      textAmharic_9.setAutoDraw(true);
    }
    
    
    // *textOptionA_9* updates
    if (t >= 0.5 && textOptionA_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionA_9.tStart = t;  // (not accounting for frame time here)
      textOptionA_9.frameNStart = frameN;  // exact frame index
      
      textOptionA_9.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionA_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionA_9.setAutoDraw(false);
    }
    
    
    // *textOptionB_9* updates
    if (t >= 1.5 && textOptionB_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionB_9.tStart = t;  // (not accounting for frame time here)
      textOptionB_9.frameNStart = frameN;  // exact frame index
      
      textOptionB_9.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionB_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionB_9.setAutoDraw(false);
    }
    
    
    // *textOptionC_9* updates
    if (t >= 2.5 && textOptionC_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionC_9.tStart = t;  // (not accounting for frame time here)
      textOptionC_9.frameNStart = frameN;  // exact frame index
      
      textOptionC_9.setAutoDraw(true);
    }
    
    frameRemains = 2.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionC_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionC_9.setAutoDraw(false);
    }
    
    
    // *textOptionD_9* updates
    if (t >= 3.5 && textOptionD_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionD_9.tStart = t;  // (not accounting for frame time here)
      textOptionD_9.frameNStart = frameN;  // exact frame index
      
      textOptionD_9.setAutoDraw(true);
    }
    
    frameRemains = 3.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionD_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionD_9.setAutoDraw(false);
    }
    
    
    // *textDiamond_8* updates
    if (t >= 4.5 && textDiamond_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textDiamond_8.tStart = t;  // (not accounting for frame time here)
      textDiamond_8.frameNStart = frameN;  // exact frame index
      
      textDiamond_8.setAutoDraw(true);
    }
    
    
    // *key_resp_10* updates
    if (t >= 4.5 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }
    
    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: ['right', 'up', 'left', 'down', 'space'], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
        key_resp_10.duration = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_10.keys == correctAns) {
            key_resp_10.corr = 1;
        } else {
            key_resp_10.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *debugging_press_enter_to_skip_23* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_23.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_23.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_23.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_23.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_23.clearEvents(); });
    }
    
    if (debugging_press_enter_to_skip_23.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_23.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_23_allKeys = _debugging_press_enter_to_skip_23_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_23_allKeys.length > 0) {
        debugging_press_enter_to_skip_23.keys = _debugging_press_enter_to_skip_23_allKeys[_debugging_press_enter_to_skip_23_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_23.rt = _debugging_press_enter_to_skip_23_allKeys[_debugging_press_enter_to_skip_23_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_23.duration = _debugging_press_enter_to_skip_23_allKeys[_debugging_press_enter_to_skip_23_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_testComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practice_testRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_test' ---
    for (const thisComponent of practice_testComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_test.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_10.keys === undefined) {
      if (['None','none',undefined].includes(correctAns)) {
         key_resp_10.corr = 1;  // correct non-response
      } else {
         key_resp_10.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_10.corr, level);
    }
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    psychoJS.experiment.addData('key_resp_10.corr', key_resp_10.corr);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        psychoJS.experiment.addData('key_resp_10.duration', key_resp_10.duration);
        routineTimer.reset();
        }
    
    key_resp_10.stop();
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_23.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_23.keys', debugging_press_enter_to_skip_23.keys);
    if (typeof debugging_press_enter_to_skip_23.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_23.rt', debugging_press_enter_to_skip_23.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_23.duration', debugging_press_enter_to_skip_23.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_23.stop();
    // the Routine "practice_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function checkForCorr_5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'checkForCorr_5' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    checkForCorr_5Clock.reset();
    routineTimer.reset();
    checkForCorr_5MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_7
    if ((key_resp_10.corr === 1)) {
        checkmark_reps = 1;
        xmark_reps = 0;
    }
    if ((key_resp_10.corr === 0)) {
        checkmark_reps = 0;
        xmark_reps = 1;
    }
    
    psychoJS.experiment.addData('checkForCorr_5.started', globalClock.getTime());
    checkForCorr_5MaxDuration = null
    // keep track of which components have finished
    checkForCorr_5Components = [];
    
    for (const thisComponent of checkForCorr_5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function checkForCorr_5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'checkForCorr_5' ---
    // get current time
    t = checkForCorr_5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of checkForCorr_5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function checkForCorr_5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'checkForCorr_5' ---
    for (const thisComponent of checkForCorr_5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('checkForCorr_5.stopped', globalClock.getTime());
    // the Routine "checkForCorr_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function checkmarkRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'checkmark' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    checkmarkClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    checkmarkMaxDurationReached = false;
    // update component parameters for each repeat
    textCheck.setText(markers[0]);
    psychoJS.experiment.addData('checkmark.started', globalClock.getTime());
    checkmarkMaxDuration = null
    // keep track of which components have finished
    checkmarkComponents = [];
    checkmarkComponents.push(textCheck);
    
    for (const thisComponent of checkmarkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function checkmarkRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'checkmark' ---
    // get current time
    t = checkmarkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textCheck* updates
    if (t >= 0.0 && textCheck.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textCheck.tStart = t;  // (not accounting for frame time here)
      textCheck.frameNStart = frameN;  // exact frame index
      
      textCheck.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textCheck.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textCheck.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of checkmarkComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function checkmarkRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'checkmark' ---
    for (const thisComponent of checkmarkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('checkmark.stopped', globalClock.getTime());
    if (checkmarkMaxDurationReached) {
        checkmarkClock.add(checkmarkMaxDuration);
    } else {
        checkmarkClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function xmarkRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'xmark' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    xmarkClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    xmarkMaxDurationReached = false;
    // update component parameters for each repeat
    textXmark.setText(markers[1]);
    psychoJS.experiment.addData('xmark.started', globalClock.getTime());
    xmarkMaxDuration = null
    // keep track of which components have finished
    xmarkComponents = [];
    xmarkComponents.push(textXmark);
    
    for (const thisComponent of xmarkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function xmarkRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'xmark' ---
    // get current time
    t = xmarkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textXmark* updates
    if (t >= 0.0 && textXmark.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textXmark.tStart = t;  // (not accounting for frame time here)
      textXmark.frameNStart = frameN;  // exact frame index
      
      textXmark.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textXmark.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textXmark.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of xmarkComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function xmarkRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'xmark' ---
    for (const thisComponent of xmarkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('xmark.stopped', globalClock.getTime());
    if (xmarkMaxDurationReached) {
        xmarkClock.add(xmarkMaxDuration);
    } else {
        xmarkClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function resetRepsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'resetReps' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    resetRepsClock.reset();
    routineTimer.reset();
    resetRepsMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('resetReps.started', globalClock.getTime());
    resetRepsMaxDuration = null
    // keep track of which components have finished
    resetRepsComponents = [];
    
    for (const thisComponent of resetRepsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function resetRepsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'resetReps' ---
    // get current time
    t = resetRepsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of resetRepsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function resetRepsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'resetReps' ---
    for (const thisComponent of resetRepsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('resetReps.stopped', globalClock.getTime());
    // the Routine "resetReps" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function blank500RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blank500' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    blank500Clock.reset(routineTimer.getTime());
    routineTimer.add(0.500000);
    blank500MaxDurationReached = false;
    // update component parameters for each repeat
    text_2.setText('');
    debugging_press_enter_to_skip_15.keys = undefined;
    debugging_press_enter_to_skip_15.rt = undefined;
    _debugging_press_enter_to_skip_15_allKeys = [];
    psychoJS.experiment.addData('blank500.started', globalClock.getTime());
    blank500MaxDuration = null
    // keep track of which components have finished
    blank500Components = [];
    blank500Components.push(text_2);
    blank500Components.push(debugging_press_enter_to_skip_15);
    
    for (const thisComponent of blank500Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function blank500RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blank500' ---
    // get current time
    t = blank500Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_15* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_15.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_15.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_15.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_15.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_15.clearEvents(); });
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_15.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_15.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_15.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_15_allKeys = _debugging_press_enter_to_skip_15_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_15_allKeys.length > 0) {
        debugging_press_enter_to_skip_15.keys = _debugging_press_enter_to_skip_15_allKeys[_debugging_press_enter_to_skip_15_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_15.rt = _debugging_press_enter_to_skip_15_allKeys[_debugging_press_enter_to_skip_15_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_15.duration = _debugging_press_enter_to_skip_15_allKeys[_debugging_press_enter_to_skip_15_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blank500Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function blank500RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blank500' ---
    for (const thisComponent of blank500Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('blank500.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_15.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_15.keys', debugging_press_enter_to_skip_15.keys);
    if (typeof debugging_press_enter_to_skip_15.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_15.rt', debugging_press_enter_to_skip_15.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_15.duration', debugging_press_enter_to_skip_15.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_15.stop();
    if (blank500MaxDurationReached) {
        blank500Clock.add(blank500MaxDuration);
    } else {
        blank500Clock.add(0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function WelcomeScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'WelcomeScreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    WelcomeScreenClock.reset();
    routineTimer.reset();
    WelcomeScreenMaxDurationReached = false;
    // update component parameters for each repeat
    Press_Space_When_Ready.keys = undefined;
    Press_Space_When_Ready.rt = undefined;
    _Press_Space_When_Ready_allKeys = [];
    psychoJS.experiment.addData('WelcomeScreen.started', globalClock.getTime());
    WelcomeScreenMaxDuration = null
    // keep track of which components have finished
    WelcomeScreenComponents = [];
    WelcomeScreenComponents.push(text_3);
    WelcomeScreenComponents.push(Press_Space_When_Ready);
    
    for (const thisComponent of WelcomeScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function WelcomeScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'WelcomeScreen' ---
    // get current time
    t = WelcomeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    
    // *Press_Space_When_Ready* updates
    if (t >= 0.0 && Press_Space_When_Ready.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Press_Space_When_Ready.tStart = t;  // (not accounting for frame time here)
      Press_Space_When_Ready.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Press_Space_When_Ready.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Press_Space_When_Ready.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Press_Space_When_Ready.clearEvents(); });
    }
    
    if (Press_Space_When_Ready.status === PsychoJS.Status.STARTED) {
      let theseKeys = Press_Space_When_Ready.getKeys({keyList: ['space'], waitRelease: false});
      _Press_Space_When_Ready_allKeys = _Press_Space_When_Ready_allKeys.concat(theseKeys);
      if (_Press_Space_When_Ready_allKeys.length > 0) {
        Press_Space_When_Ready.keys = _Press_Space_When_Ready_allKeys[_Press_Space_When_Ready_allKeys.length - 1].name;  // just the last key pressed
        Press_Space_When_Ready.rt = _Press_Space_When_Ready_allKeys[_Press_Space_When_Ready_allKeys.length - 1].rt;
        Press_Space_When_Ready.duration = _Press_Space_When_Ready_allKeys[_Press_Space_When_Ready_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WelcomeScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function WelcomeScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'WelcomeScreen' ---
    for (const thisComponent of WelcomeScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('WelcomeScreen.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Press_Space_When_Ready.corr, level);
    }
    psychoJS.experiment.addData('Press_Space_When_Ready.keys', Press_Space_When_Ready.keys);
    if (typeof Press_Space_When_Ready.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Press_Space_When_Ready.rt', Press_Space_When_Ready.rt);
        psychoJS.experiment.addData('Press_Space_When_Ready.duration', Press_Space_When_Ready.duration);
        routineTimer.reset();
        }
    
    Press_Space_When_Ready.stop();
    // the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function randomize_setRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'randomize_set' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    randomize_setClock.reset();
    routineTimer.reset();
    randomize_setMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from randomize_learning_set
    
            // add-on: list(s: string): string[]
            function list(s) {
                // if s is a string, we return a list of its characters
                if (typeof s === 'string')
                    return s.split('');
                else
                    // otherwise we return s:
                    return s;
            }
    
            keys = list(util.range(12));
    Math.random.shuffle(keys);
    console.log(("learning set order: " + keys.toString()));
    
    psychoJS.experiment.addData('randomize_set.started', globalClock.getTime());
    randomize_setMaxDuration = null
    // keep track of which components have finished
    randomize_setComponents = [];
    
    for (const thisComponent of randomize_setComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function randomize_setRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'randomize_set' ---
    // get current time
    t = randomize_setClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of randomize_setComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function randomize_setRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'randomize_set' ---
    for (const thisComponent of randomize_setComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('randomize_set.stopped', globalClock.getTime());
    // the Routine "randomize_set" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function IncrementRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Increment' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    IncrementClock.reset();
    routineTimer.reset();
    IncrementMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from increment_index
    learning_index += 1;
    learning_index %= keys.length;
    
    psychoJS.experiment.addData('Increment.started', globalClock.getTime());
    IncrementMaxDuration = null
    // keep track of which components have finished
    IncrementComponents = [];
    
    for (const thisComponent of IncrementComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function IncrementRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Increment' ---
    // get current time
    t = IncrementClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of IncrementComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function IncrementRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Increment' ---
    for (const thisComponent of IncrementComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Increment.stopped', globalClock.getTime());
    // the Routine "Increment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function amharic1_ARoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'amharic1_A' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    amharic1_AClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    amharic1_AMaxDurationReached = false;
    // update component parameters for each repeat
    pratice_amharic.setText(practice_list[keys[learning_index]][0]);
    practice_words.setText(practice_list[keys[learning_index]][1]);
    // Run 'Begin Routine' code from amharic_word_code1
    console.log(((((((("Index: " + keys[learning_index].toString()) + "\n Character: ") + practice_list[keys[learning_index]][0].toString()) + "\n Meaning: ") + practice_list[keys[learning_index]][1].toString()) + "\n Image Path: ") + practice_list[keys[learning_index]][2].toString()));
    
    debugging_press_enter_to_skip.keys = undefined;
    debugging_press_enter_to_skip.rt = undefined;
    _debugging_press_enter_to_skip_allKeys = [];
    psychoJS.experiment.addData('amharic1_A.started', globalClock.getTime());
    amharic1_AMaxDuration = null
    // keep track of which components have finished
    amharic1_AComponents = [];
    amharic1_AComponents.push(pratice_amharic);
    amharic1_AComponents.push(practice_words);
    amharic1_AComponents.push(debugging_press_enter_to_skip);
    
    for (const thisComponent of amharic1_AComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function amharic1_ARoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'amharic1_A' ---
    // get current time
    t = amharic1_AClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pratice_amharic* updates
    if (t >= 0.0 && pratice_amharic.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pratice_amharic.tStart = t;  // (not accounting for frame time here)
      pratice_amharic.frameNStart = frameN;  // exact frame index
      
      pratice_amharic.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (pratice_amharic.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pratice_amharic.setAutoDraw(false);
    }
    
    
    // *practice_words* updates
    if (t >= 0.0 && practice_words.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_words.tStart = t;  // (not accounting for frame time here)
      practice_words.frameNStart = frameN;  // exact frame index
      
      practice_words.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (practice_words.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_words.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip* updates
    if (t >= 0.0 && debugging_press_enter_to_skip.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_allKeys = _debugging_press_enter_to_skip_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_allKeys.length > 0) {
        debugging_press_enter_to_skip.keys = _debugging_press_enter_to_skip_allKeys[_debugging_press_enter_to_skip_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip.rt = _debugging_press_enter_to_skip_allKeys[_debugging_press_enter_to_skip_allKeys.length - 1].rt;
        debugging_press_enter_to_skip.duration = _debugging_press_enter_to_skip_allKeys[_debugging_press_enter_to_skip_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of amharic1_AComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function amharic1_ARoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'amharic1_A' ---
    for (const thisComponent of amharic1_AComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('amharic1_A.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip.keys', debugging_press_enter_to_skip.keys);
    if (typeof debugging_press_enter_to_skip.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip.rt', debugging_press_enter_to_skip.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip.duration', debugging_press_enter_to_skip.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip.stop();
    if (amharic1_AMaxDurationReached) {
        amharic1_AClock.add(amharic1_AMaxDuration);
    } else {
        amharic1_AClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function amharic1_BRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'amharic1_B' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    amharic1_BClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    amharic1_BMaxDurationReached = false;
    // update component parameters for each repeat
    amharics1_2.setText(amharic_word_list1[keys[learning_index]][0]);
    words1_image_2.setImage(amharic_word_list1[keys[learning_index]][2]);
    // Run 'Begin Routine' code from amharic_word_code1_2
    console.log(((((((("Index: " + keys[learning_index].toString()) + "\n Character: ") + amharic_word_list1[keys[learning_index]][0].toString()) + "\n Meaning: ") + amharic_word_list1[keys[learning_index]][1].toString()) + "\n Image Path: ") + amharic_word_list1[keys[learning_index]][2].toString()));
    
    debugging_press_enter_to_skip_2.keys = undefined;
    debugging_press_enter_to_skip_2.rt = undefined;
    _debugging_press_enter_to_skip_2_allKeys = [];
    psychoJS.experiment.addData('amharic1_B.started', globalClock.getTime());
    amharic1_BMaxDuration = null
    // keep track of which components have finished
    amharic1_BComponents = [];
    amharic1_BComponents.push(amharics1_2);
    amharic1_BComponents.push(words1_image_2);
    amharic1_BComponents.push(debugging_press_enter_to_skip_2);
    
    for (const thisComponent of amharic1_BComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function amharic1_BRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'amharic1_B' ---
    // get current time
    t = amharic1_BClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *amharics1_2* updates
    if (t >= 0.0 && amharics1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      amharics1_2.tStart = t;  // (not accounting for frame time here)
      amharics1_2.frameNStart = frameN;  // exact frame index
      
      amharics1_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (amharics1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      amharics1_2.setAutoDraw(false);
    }
    
    
    // *words1_image_2* updates
    if (t >= 0.0 && words1_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      words1_image_2.tStart = t;  // (not accounting for frame time here)
      words1_image_2.frameNStart = frameN;  // exact frame index
      
      words1_image_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (words1_image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      words1_image_2.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_2* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_2.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_2.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_2.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_2.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_2_allKeys = _debugging_press_enter_to_skip_2_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_2_allKeys.length > 0) {
        debugging_press_enter_to_skip_2.keys = _debugging_press_enter_to_skip_2_allKeys[_debugging_press_enter_to_skip_2_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_2.rt = _debugging_press_enter_to_skip_2_allKeys[_debugging_press_enter_to_skip_2_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_2.duration = _debugging_press_enter_to_skip_2_allKeys[_debugging_press_enter_to_skip_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of amharic1_BComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function amharic1_BRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'amharic1_B' ---
    for (const thisComponent of amharic1_BComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('amharic1_B.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_2.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_2.keys', debugging_press_enter_to_skip_2.keys);
    if (typeof debugging_press_enter_to_skip_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_2.rt', debugging_press_enter_to_skip_2.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_2.duration', debugging_press_enter_to_skip_2.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_2.stop();
    if (amharic1_BMaxDurationReached) {
        amharic1_BClock.add(amharic1_BMaxDuration);
    } else {
        amharic1_BClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function breakBetweenRepeatsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'breakBetweenRepeats' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    breakBetweenRepeatsClock.reset(routineTimer.getTime());
    routineTimer.add(5.000000);
    breakBetweenRepeatsMaxDurationReached = false;
    // update component parameters for each repeat
    maybe_a_beep.setValue('A');
    maybe_a_beep.secs=1.0;
    maybe_a_beep.setVolume(1.0);
    debugging_press_enter_to_skip_5.keys = undefined;
    debugging_press_enter_to_skip_5.rt = undefined;
    _debugging_press_enter_to_skip_5_allKeys = [];
    psychoJS.experiment.addData('breakBetweenRepeats.started', globalClock.getTime());
    breakBetweenRepeatsMaxDuration = null
    // keep track of which components have finished
    breakBetweenRepeatsComponents = [];
    breakBetweenRepeatsComponents.push(five_seconds);
    breakBetweenRepeatsComponents.push(maybe_a_beep);
    breakBetweenRepeatsComponents.push(debugging_press_enter_to_skip_5);
    
    for (const thisComponent of breakBetweenRepeatsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function breakBetweenRepeatsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'breakBetweenRepeats' ---
    // get current time
    t = breakBetweenRepeatsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *five_seconds* updates
    if (t >= 0.0 && five_seconds.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      five_seconds.tStart = t;  // (not accounting for frame time here)
      five_seconds.frameNStart = frameN;  // exact frame index
      
      five_seconds.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (five_seconds.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      five_seconds.setAutoDraw(false);
    }
    
    // start/stop maybe_a_beep
    if (t >= 0.0 && maybe_a_beep.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      maybe_a_beep.tStart = t;  // (not accounting for frame time here)
      maybe_a_beep.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ maybe_a_beep.play(); });  // screen flip
      maybe_a_beep.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (maybe_a_beep.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (t >= maybe_a_beep.tStart + 0.5) {
        maybe_a_beep.stop();  // stop the sound (if longer than duration)
        maybe_a_beep.status = PsychoJS.Status.FINISHED;
      }
    }
    
    // *debugging_press_enter_to_skip_5* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_5.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_5.clearEvents(); });
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_5.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_5.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_5_allKeys = _debugging_press_enter_to_skip_5_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_5_allKeys.length > 0) {
        debugging_press_enter_to_skip_5.keys = _debugging_press_enter_to_skip_5_allKeys[_debugging_press_enter_to_skip_5_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_5.rt = _debugging_press_enter_to_skip_5_allKeys[_debugging_press_enter_to_skip_5_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_5.duration = _debugging_press_enter_to_skip_5_allKeys[_debugging_press_enter_to_skip_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of breakBetweenRepeatsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function breakBetweenRepeatsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'breakBetweenRepeats' ---
    for (const thisComponent of breakBetweenRepeatsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('breakBetweenRepeats.stopped', globalClock.getTime());
    maybe_a_beep.stop();  // ensure sound has stopped at end of Routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_5.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_5.keys', debugging_press_enter_to_skip_5.keys);
    if (typeof debugging_press_enter_to_skip_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_5.rt', debugging_press_enter_to_skip_5.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_5.duration', debugging_press_enter_to_skip_5.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_5.stop();
    if (breakBetweenRepeatsMaxDurationReached) {
        breakBetweenRepeatsClock.add(breakBetweenRepeatsMaxDuration);
    } else {
        breakBetweenRepeatsClock.add(5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function routine_30SecondsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'routine_30Seconds' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routine_30SecondsClock.reset(routineTimer.getTime());
    routineTimer.add(30.000000);
    routine_30SecondsMaxDurationReached = false;
    // update component parameters for each repeat
    debugging_press_enter_to_skip_6.keys = undefined;
    debugging_press_enter_to_skip_6.rt = undefined;
    _debugging_press_enter_to_skip_6_allKeys = [];
    psychoJS.experiment.addData('routine_30Seconds.started', globalClock.getTime());
    routine_30SecondsMaxDuration = null
    // keep track of which components have finished
    routine_30SecondsComponents = [];
    routine_30SecondsComponents.push(thirtySeconds);
    routine_30SecondsComponents.push(debugging_press_enter_to_skip_6);
    
    for (const thisComponent of routine_30SecondsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function routine_30SecondsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'routine_30Seconds' ---
    // get current time
    t = routine_30SecondsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thirtySeconds* updates
    if (t >= 0.0 && thirtySeconds.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thirtySeconds.tStart = t;  // (not accounting for frame time here)
      thirtySeconds.frameNStart = frameN;  // exact frame index
      
      thirtySeconds.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (thirtySeconds.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      thirtySeconds.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_6* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_6.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_6.clearEvents(); });
    }
    
    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_6.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_6.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_6_allKeys = _debugging_press_enter_to_skip_6_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_6_allKeys.length > 0) {
        debugging_press_enter_to_skip_6.keys = _debugging_press_enter_to_skip_6_allKeys[_debugging_press_enter_to_skip_6_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_6.rt = _debugging_press_enter_to_skip_6_allKeys[_debugging_press_enter_to_skip_6_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_6.duration = _debugging_press_enter_to_skip_6_allKeys[_debugging_press_enter_to_skip_6_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of routine_30SecondsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function routine_30SecondsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'routine_30Seconds' ---
    for (const thisComponent of routine_30SecondsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('routine_30Seconds.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_6.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_6.keys', debugging_press_enter_to_skip_6.keys);
    if (typeof debugging_press_enter_to_skip_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_6.rt', debugging_press_enter_to_skip_6.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_6.duration', debugging_press_enter_to_skip_6.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_6.stop();
    if (routine_30SecondsMaxDurationReached) {
        routine_30SecondsClock.add(routine_30SecondsMaxDuration);
    } else {
        routine_30SecondsClock.add(30.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function start_testRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start_test' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    start_testClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    start_testMaxDurationReached = false;
    // update component parameters for each repeat
    debugging_press_enter_to_skip_7.keys = undefined;
    debugging_press_enter_to_skip_7.rt = undefined;
    _debugging_press_enter_to_skip_7_allKeys = [];
    psychoJS.experiment.addData('start_test.started', globalClock.getTime());
    start_testMaxDuration = null
    // keep track of which components have finished
    start_testComponents = [];
    start_testComponents.push(textWelcome);
    start_testComponents.push(debugging_press_enter_to_skip_7);
    
    for (const thisComponent of start_testComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function start_testRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start_test' ---
    // get current time
    t = start_testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWelcome* updates
    if (t >= 0.0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWelcome.tStart = t;  // (not accounting for frame time here)
      textWelcome.frameNStart = frameN;  // exact frame index
      
      textWelcome.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textWelcome.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textWelcome.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_7* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_7.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_7.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_7.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_7.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_7_allKeys = _debugging_press_enter_to_skip_7_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_7_allKeys.length > 0) {
        debugging_press_enter_to_skip_7.keys = _debugging_press_enter_to_skip_7_allKeys[_debugging_press_enter_to_skip_7_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_7.rt = _debugging_press_enter_to_skip_7_allKeys[_debugging_press_enter_to_skip_7_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_7.duration = _debugging_press_enter_to_skip_7_allKeys[_debugging_press_enter_to_skip_7_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of start_testComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function start_testRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start_test' ---
    for (const thisComponent of start_testComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('start_test.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_7.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_7.keys', debugging_press_enter_to_skip_7.keys);
    if (typeof debugging_press_enter_to_skip_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_7.rt', debugging_press_enter_to_skip_7.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_7.duration', debugging_press_enter_to_skip_7.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_7.stop();
    if (start_testMaxDurationReached) {
        start_testClock.add(start_testMaxDuration);
    } else {
        start_testClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function test1_NEWRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test1_NEW' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    test1_NEWClock.reset();
    routineTimer.reset();
    test1_NEWMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codeSymbol_5
    /* Syntax Error: Fix Python code */
    textAmharic_5.setText(amharic1);
    textOptionA_5.setText(lottery_list1[0]);
    textOptionB_5.setText(lottery_list1[1]);
    textOptionC_5.setText(lottery_list1[2]);
    textOptionD_5.setText(lottery_list1[3]);
    textDiamond_3.setText(f'''     {lottery_list1[0]}
       {lottery_list1[1]}   {lottery_list1[2]}
         {lottery_list1[3]}''');
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    debugging_press_enter_to_skip_19.keys = undefined;
    debugging_press_enter_to_skip_19.rt = undefined;
    _debugging_press_enter_to_skip_19_allKeys = [];
    psychoJS.experiment.addData('test1_NEW.started', globalClock.getTime());
    test1_NEWMaxDuration = null
    // keep track of which components have finished
    test1_NEWComponents = [];
    test1_NEWComponents.push(textAmharic_5);
    test1_NEWComponents.push(textOptionA_5);
    test1_NEWComponents.push(textOptionB_5);
    test1_NEWComponents.push(textOptionC_5);
    test1_NEWComponents.push(textOptionD_5);
    test1_NEWComponents.push(textDiamond_3);
    test1_NEWComponents.push(key_resp_5);
    test1_NEWComponents.push(debugging_press_enter_to_skip_19);
    
    for (const thisComponent of test1_NEWComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function test1_NEWRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test1_NEW' ---
    // get current time
    t = test1_NEWClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textAmharic_5* updates
    if (t >= 0.0 && textAmharic_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textAmharic_5.tStart = t;  // (not accounting for frame time here)
      textAmharic_5.frameNStart = frameN;  // exact frame index
      
      textAmharic_5.setAutoDraw(true);
    }
    
    
    // *textOptionA_5* updates
    if (t >= 0.5 && textOptionA_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionA_5.tStart = t;  // (not accounting for frame time here)
      textOptionA_5.frameNStart = frameN;  // exact frame index
      
      textOptionA_5.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionA_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionA_5.setAutoDraw(false);
    }
    
    
    // *textOptionB_5* updates
    if (t >= 1.5 && textOptionB_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionB_5.tStart = t;  // (not accounting for frame time here)
      textOptionB_5.frameNStart = frameN;  // exact frame index
      
      textOptionB_5.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionB_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionB_5.setAutoDraw(false);
    }
    
    
    // *textOptionC_5* updates
    if (t >= 2.5 && textOptionC_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionC_5.tStart = t;  // (not accounting for frame time here)
      textOptionC_5.frameNStart = frameN;  // exact frame index
      
      textOptionC_5.setAutoDraw(true);
    }
    
    frameRemains = 2.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionC_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionC_5.setAutoDraw(false);
    }
    
    
    // *textOptionD_5* updates
    if (t >= 3.5 && textOptionD_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionD_5.tStart = t;  // (not accounting for frame time here)
      textOptionD_5.frameNStart = frameN;  // exact frame index
      
      textOptionD_5.setAutoDraw(true);
    }
    
    frameRemains = 3.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionD_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionD_5.setAutoDraw(false);
    }
    
    
    // *textDiamond_3* updates
    if (t >= 4.5 && textDiamond_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textDiamond_3.tStart = t;  // (not accounting for frame time here)
      textDiamond_3.frameNStart = frameN;  // exact frame index
      
      textDiamond_3.setAutoDraw(true);
    }
    
    
    // *key_resp_5* updates
    if (t >= 4.5 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }
    
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['right', 'up', 'left', 'down', 'space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        key_resp_5.duration = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_5.keys == correctAns) {
            key_resp_5.corr = 1;
        } else {
            key_resp_5.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *debugging_press_enter_to_skip_19* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_19.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_19.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_19.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_19.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_19.clearEvents(); });
    }
    
    if (debugging_press_enter_to_skip_19.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_19.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_19_allKeys = _debugging_press_enter_to_skip_19_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_19_allKeys.length > 0) {
        debugging_press_enter_to_skip_19.keys = _debugging_press_enter_to_skip_19_allKeys[_debugging_press_enter_to_skip_19_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_19.rt = _debugging_press_enter_to_skip_19_allKeys[_debugging_press_enter_to_skip_19_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_19.duration = _debugging_press_enter_to_skip_19_allKeys[_debugging_press_enter_to_skip_19_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test1_NEWComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function test1_NEWRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test1_NEW' ---
    for (const thisComponent of test1_NEWComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('test1_NEW.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_5.keys === undefined) {
      if (['None','none',undefined].includes(correctAns)) {
         key_resp_5.corr = 1;  // correct non-response
      } else {
         key_resp_5.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    psychoJS.experiment.addData('key_resp_5.corr', key_resp_5.corr);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        psychoJS.experiment.addData('key_resp_5.duration', key_resp_5.duration);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_19.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_19.keys', debugging_press_enter_to_skip_19.keys);
    if (typeof debugging_press_enter_to_skip_19.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_19.rt', debugging_press_enter_to_skip_19.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_19.duration', debugging_press_enter_to_skip_19.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_19.stop();
    // the Routine "test1_NEW" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function checkForCorrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'checkForCorr' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    checkForCorrClock.reset();
    routineTimer.reset();
    checkForCorrMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    if ((key_resp_5.corr === 1)) {
        checkmark_reps = 1;
        xmark_reps = 0;
    }
    if ((key_resp_5.corr === 0)) {
        checkmark_reps = 0;
        xmark_reps = 1;
    }
    
    psychoJS.experiment.addData('checkForCorr.started', globalClock.getTime());
    checkForCorrMaxDuration = null
    // keep track of which components have finished
    checkForCorrComponents = [];
    
    for (const thisComponent of checkForCorrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function checkForCorrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'checkForCorr' ---
    // get current time
    t = checkForCorrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of checkForCorrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function checkForCorrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'checkForCorr' ---
    for (const thisComponent of checkForCorrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('checkForCorr.stopped', globalClock.getTime());
    // the Routine "checkForCorr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function amharic2_ARoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'amharic2_A' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    amharic2_AClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    amharic2_AMaxDurationReached = false;
    // update component parameters for each repeat
    amharics2.setText(amharic_word_list2[keys[learning_index]][0]);
    words2.setText(amharic_word_list2[keys[learning_index]][1]);
    // Run 'Begin Routine' code from amharic_word_code_2
    console.log(((((((("Index: " + keys[learning_index].toString()) + "\n Character: ") + amharic_word_list2[keys[learning_index]][0].toString()) + "\n Meaning: ") + amharic_word_list2[keys[learning_index]][1].toString()) + "\n Image Path: ") + amharic_word_list2[keys[learning_index]][2].toString()));
    
    debugging_press_enter_to_skip_9.keys = undefined;
    debugging_press_enter_to_skip_9.rt = undefined;
    _debugging_press_enter_to_skip_9_allKeys = [];
    psychoJS.experiment.addData('amharic2_A.started', globalClock.getTime());
    amharic2_AMaxDuration = null
    // keep track of which components have finished
    amharic2_AComponents = [];
    amharic2_AComponents.push(amharics2);
    amharic2_AComponents.push(words2);
    amharic2_AComponents.push(debugging_press_enter_to_skip_9);
    
    for (const thisComponent of amharic2_AComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function amharic2_ARoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'amharic2_A' ---
    // get current time
    t = amharic2_AClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *amharics2* updates
    if (t >= 0.0 && amharics2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      amharics2.tStart = t;  // (not accounting for frame time here)
      amharics2.frameNStart = frameN;  // exact frame index
      
      amharics2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (amharics2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      amharics2.setAutoDraw(false);
    }
    
    
    // *words2* updates
    if (t >= 0.0 && words2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      words2.tStart = t;  // (not accounting for frame time here)
      words2.frameNStart = frameN;  // exact frame index
      
      words2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (words2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      words2.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_9* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_9.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_9.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_9.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_9.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_9_allKeys = _debugging_press_enter_to_skip_9_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_9_allKeys.length > 0) {
        debugging_press_enter_to_skip_9.keys = _debugging_press_enter_to_skip_9_allKeys[_debugging_press_enter_to_skip_9_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_9.rt = _debugging_press_enter_to_skip_9_allKeys[_debugging_press_enter_to_skip_9_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_9.duration = _debugging_press_enter_to_skip_9_allKeys[_debugging_press_enter_to_skip_9_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of amharic2_AComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function amharic2_ARoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'amharic2_A' ---
    for (const thisComponent of amharic2_AComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('amharic2_A.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_9.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_9.keys', debugging_press_enter_to_skip_9.keys);
    if (typeof debugging_press_enter_to_skip_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_9.rt', debugging_press_enter_to_skip_9.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_9.duration', debugging_press_enter_to_skip_9.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_9.stop();
    if (amharic2_AMaxDurationReached) {
        amharic2_AClock.add(amharic2_AMaxDuration);
    } else {
        amharic2_AClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function amharic2_BRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'amharic2_B' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    amharic2_BClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    amharic2_BMaxDurationReached = false;
    // update component parameters for each repeat
    amharics2_2.setText(amharic_word_list2[keys[learning_index]][0]);
    words2_image_2.setImage(amharic_word_list2[keys[learning_index]][2]);
    // Run 'Begin Routine' code from amharic_word_code
    console.log(((((((("Index: " + keys[learning_index].toString()) + "\n Character: ") + amharic_word_list2[keys[learning_index]][0].toString()) + "\n Meaning: ") + amharic_word_list2[keys[learning_index]][1].toString()) + "\n Image Path: ") + amharic_word_list2[keys[learning_index]][2].toString()));
    
    debugging_press_enter_to_skip_10.keys = undefined;
    debugging_press_enter_to_skip_10.rt = undefined;
    _debugging_press_enter_to_skip_10_allKeys = [];
    psychoJS.experiment.addData('amharic2_B.started', globalClock.getTime());
    amharic2_BMaxDuration = null
    // keep track of which components have finished
    amharic2_BComponents = [];
    amharic2_BComponents.push(amharics2_2);
    amharic2_BComponents.push(words2_image_2);
    amharic2_BComponents.push(debugging_press_enter_to_skip_10);
    
    for (const thisComponent of amharic2_BComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function amharic2_BRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'amharic2_B' ---
    // get current time
    t = amharic2_BClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *amharics2_2* updates
    if (t >= 0.0 && amharics2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      amharics2_2.tStart = t;  // (not accounting for frame time here)
      amharics2_2.frameNStart = frameN;  // exact frame index
      
      amharics2_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (amharics2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      amharics2_2.setAutoDraw(false);
    }
    
    
    // *words2_image_2* updates
    if (t >= 0.0 && words2_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      words2_image_2.tStart = t;  // (not accounting for frame time here)
      words2_image_2.frameNStart = frameN;  // exact frame index
      
      words2_image_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (words2_image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      words2_image_2.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_10* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_10.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_10.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_10.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_10.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_10_allKeys = _debugging_press_enter_to_skip_10_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_10_allKeys.length > 0) {
        debugging_press_enter_to_skip_10.keys = _debugging_press_enter_to_skip_10_allKeys[_debugging_press_enter_to_skip_10_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_10.rt = _debugging_press_enter_to_skip_10_allKeys[_debugging_press_enter_to_skip_10_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_10.duration = _debugging_press_enter_to_skip_10_allKeys[_debugging_press_enter_to_skip_10_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of amharic2_BComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function amharic2_BRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'amharic2_B' ---
    for (const thisComponent of amharic2_BComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('amharic2_B.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_10.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_10.keys', debugging_press_enter_to_skip_10.keys);
    if (typeof debugging_press_enter_to_skip_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_10.rt', debugging_press_enter_to_skip_10.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_10.duration', debugging_press_enter_to_skip_10.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_10.stop();
    if (amharic2_BMaxDurationReached) {
        amharic2_BClock.add(amharic2_BMaxDuration);
    } else {
        amharic2_BClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function test2_NEWRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test2_NEW' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    test2_NEWClock.reset();
    routineTimer.reset();
    test2_NEWMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codeSymbol_6
    /* Syntax Error: Fix Python code */
    textAmharic_6.setText(amharic2);
    textOptionA_6.setText(lottery_list2[0]);
    textOptionB_6.setText(lottery_list2[1]);
    textOptionC_6.setText(lottery_list2[2]);
    textOptionD_6.setText(lottery_list2[3]);
    textDiamond_5.setText(f'''     {lottery_list2[0]}
       {lottery_list2[1]}   {lottery_list2[2]}
         {lottery_list2[3]}''');
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    debugging_press_enter_to_skip_20.keys = undefined;
    debugging_press_enter_to_skip_20.rt = undefined;
    _debugging_press_enter_to_skip_20_allKeys = [];
    psychoJS.experiment.addData('test2_NEW.started', globalClock.getTime());
    test2_NEWMaxDuration = null
    // keep track of which components have finished
    test2_NEWComponents = [];
    test2_NEWComponents.push(textAmharic_6);
    test2_NEWComponents.push(textOptionA_6);
    test2_NEWComponents.push(textOptionB_6);
    test2_NEWComponents.push(textOptionC_6);
    test2_NEWComponents.push(textOptionD_6);
    test2_NEWComponents.push(textDiamond_5);
    test2_NEWComponents.push(key_resp_6);
    test2_NEWComponents.push(debugging_press_enter_to_skip_20);
    
    for (const thisComponent of test2_NEWComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function test2_NEWRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test2_NEW' ---
    // get current time
    t = test2_NEWClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textAmharic_6* updates
    if (t >= 0.0 && textAmharic_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textAmharic_6.tStart = t;  // (not accounting for frame time here)
      textAmharic_6.frameNStart = frameN;  // exact frame index
      
      textAmharic_6.setAutoDraw(true);
    }
    
    
    // *textOptionA_6* updates
    if (t >= 0.5 && textOptionA_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionA_6.tStart = t;  // (not accounting for frame time here)
      textOptionA_6.frameNStart = frameN;  // exact frame index
      
      textOptionA_6.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionA_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionA_6.setAutoDraw(false);
    }
    
    
    // *textOptionB_6* updates
    if (t >= 1.5 && textOptionB_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionB_6.tStart = t;  // (not accounting for frame time here)
      textOptionB_6.frameNStart = frameN;  // exact frame index
      
      textOptionB_6.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionB_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionB_6.setAutoDraw(false);
    }
    
    
    // *textOptionC_6* updates
    if (t >= 2.5 && textOptionC_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionC_6.tStart = t;  // (not accounting for frame time here)
      textOptionC_6.frameNStart = frameN;  // exact frame index
      
      textOptionC_6.setAutoDraw(true);
    }
    
    frameRemains = 2.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionC_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionC_6.setAutoDraw(false);
    }
    
    
    // *textOptionD_6* updates
    if (t >= 3.5 && textOptionD_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionD_6.tStart = t;  // (not accounting for frame time here)
      textOptionD_6.frameNStart = frameN;  // exact frame index
      
      textOptionD_6.setAutoDraw(true);
    }
    
    frameRemains = 3.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionD_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionD_6.setAutoDraw(false);
    }
    
    
    // *textDiamond_5* updates
    if (t >= 4.5 && textDiamond_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textDiamond_5.tStart = t;  // (not accounting for frame time here)
      textDiamond_5.frameNStart = frameN;  // exact frame index
      
      textDiamond_5.setAutoDraw(true);
    }
    
    
    // *key_resp_6* updates
    if (t >= 4.5 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }
    
    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['right', 'up', 'left', 'down'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        key_resp_6.duration = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_6.keys == correctAns2) {
            key_resp_6.corr = 1;
        } else {
            key_resp_6.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *debugging_press_enter_to_skip_20* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_20.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_20.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_20.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_20.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_20.clearEvents(); });
    }
    
    if (debugging_press_enter_to_skip_20.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_20.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_20_allKeys = _debugging_press_enter_to_skip_20_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_20_allKeys.length > 0) {
        debugging_press_enter_to_skip_20.keys = _debugging_press_enter_to_skip_20_allKeys[_debugging_press_enter_to_skip_20_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_20.rt = _debugging_press_enter_to_skip_20_allKeys[_debugging_press_enter_to_skip_20_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_20.duration = _debugging_press_enter_to_skip_20_allKeys[_debugging_press_enter_to_skip_20_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test2_NEWComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function test2_NEWRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test2_NEW' ---
    for (const thisComponent of test2_NEWComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('test2_NEW.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_6.keys === undefined) {
      if (['None','none',undefined].includes(correctAns2)) {
         key_resp_6.corr = 1;  // correct non-response
      } else {
         key_resp_6.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    psychoJS.experiment.addData('key_resp_6.corr', key_resp_6.corr);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        psychoJS.experiment.addData('key_resp_6.duration', key_resp_6.duration);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_20.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_20.keys', debugging_press_enter_to_skip_20.keys);
    if (typeof debugging_press_enter_to_skip_20.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_20.rt', debugging_press_enter_to_skip_20.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_20.duration', debugging_press_enter_to_skip_20.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_20.stop();
    // the Routine "test2_NEW" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function checkForCorr_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'checkForCorr_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    checkForCorr_2Clock.reset();
    routineTimer.reset();
    checkForCorr_2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    if ((key_resp_6.corr === 1)) {
        checkmark_reps = 1;
        xmark_reps = 0;
    }
    if ((key_resp_6.corr === 0)) {
        checkmark_reps = 0;
        xmark_reps = 1;
    }
    
    psychoJS.experiment.addData('checkForCorr_2.started', globalClock.getTime());
    checkForCorr_2MaxDuration = null
    // keep track of which components have finished
    checkForCorr_2Components = [];
    
    for (const thisComponent of checkForCorr_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function checkForCorr_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'checkForCorr_2' ---
    // get current time
    t = checkForCorr_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of checkForCorr_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function checkForCorr_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'checkForCorr_2' ---
    for (const thisComponent of checkForCorr_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('checkForCorr_2.stopped', globalClock.getTime());
    // the Routine "checkForCorr_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function amharic3_ARoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'amharic3_A' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    amharic3_AClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    amharic3_AMaxDurationReached = false;
    // update component parameters for each repeat
    amharics3.setText(amharic_word_list3[keys[learning_index]][0]);
    words3_image.setImage(amharic_word_list3[keys[learning_index]][2]);
    // Run 'Begin Routine' code from code3
    console.log(((((((("Index: " + keys[learning_index].toString()) + "\n Character: ") + amharic_word_list3[keys[learning_index]][0].toString()) + "\n Meaning: ") + amharic_word_list3[keys[learning_index]][1].toString()) + "\n Image Path: ") + amharic_word_list3[keys[learning_index]][2].toString()));
    
    debugging_press_enter_to_skip_11.keys = undefined;
    debugging_press_enter_to_skip_11.rt = undefined;
    _debugging_press_enter_to_skip_11_allKeys = [];
    psychoJS.experiment.addData('amharic3_A.started', globalClock.getTime());
    amharic3_AMaxDuration = null
    // keep track of which components have finished
    amharic3_AComponents = [];
    amharic3_AComponents.push(amharics3);
    amharic3_AComponents.push(words3_image);
    amharic3_AComponents.push(debugging_press_enter_to_skip_11);
    
    for (const thisComponent of amharic3_AComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function amharic3_ARoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'amharic3_A' ---
    // get current time
    t = amharic3_AClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *amharics3* updates
    if (t >= 0.0 && amharics3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      amharics3.tStart = t;  // (not accounting for frame time here)
      amharics3.frameNStart = frameN;  // exact frame index
      
      amharics3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (amharics3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      amharics3.setAutoDraw(false);
    }
    
    
    // *words3_image* updates
    if (t >= 0.0 && words3_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      words3_image.tStart = t;  // (not accounting for frame time here)
      words3_image.frameNStart = frameN;  // exact frame index
      
      words3_image.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (words3_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      words3_image.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_11* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_11.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_11.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_11.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_11.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_11_allKeys = _debugging_press_enter_to_skip_11_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_11_allKeys.length > 0) {
        debugging_press_enter_to_skip_11.keys = _debugging_press_enter_to_skip_11_allKeys[_debugging_press_enter_to_skip_11_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_11.rt = _debugging_press_enter_to_skip_11_allKeys[_debugging_press_enter_to_skip_11_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_11.duration = _debugging_press_enter_to_skip_11_allKeys[_debugging_press_enter_to_skip_11_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of amharic3_AComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function amharic3_ARoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'amharic3_A' ---
    for (const thisComponent of amharic3_AComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('amharic3_A.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_11.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_11.keys', debugging_press_enter_to_skip_11.keys);
    if (typeof debugging_press_enter_to_skip_11.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_11.rt', debugging_press_enter_to_skip_11.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_11.duration', debugging_press_enter_to_skip_11.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_11.stop();
    if (amharic3_AMaxDurationReached) {
        amharic3_AClock.add(amharic3_AMaxDuration);
    } else {
        amharic3_AClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function amharic3_BRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'amharic3_B' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    amharic3_BClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    amharic3_BMaxDurationReached = false;
    // update component parameters for each repeat
    amharics3_2.setText(amharic_word_list3[keys[learning_index]][0]);
    words3_2.setText(amharic_word_list3[keys[learning_index]][1]);
    // Run 'Begin Routine' code from code3_2
    console.log(((((((("Index: " + keys[learning_index].toString()) + "\n Character: ") + amharic_word_list3[keys[learning_index]][0].toString()) + "\n Meaning: ") + amharic_word_list3[keys[learning_index]][1].toString()) + "\n Image Path: ") + amharic_word_list3[keys[learning_index]][2].toString()));
    
    debugging_press_enter_to_skip_12.keys = undefined;
    debugging_press_enter_to_skip_12.rt = undefined;
    _debugging_press_enter_to_skip_12_allKeys = [];
    psychoJS.experiment.addData('amharic3_B.started', globalClock.getTime());
    amharic3_BMaxDuration = null
    // keep track of which components have finished
    amharic3_BComponents = [];
    amharic3_BComponents.push(amharics3_2);
    amharic3_BComponents.push(words3_2);
    amharic3_BComponents.push(debugging_press_enter_to_skip_12);
    
    for (const thisComponent of amharic3_BComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function amharic3_BRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'amharic3_B' ---
    // get current time
    t = amharic3_BClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *amharics3_2* updates
    if (t >= 0.0 && amharics3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      amharics3_2.tStart = t;  // (not accounting for frame time here)
      amharics3_2.frameNStart = frameN;  // exact frame index
      
      amharics3_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (amharics3_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      amharics3_2.setAutoDraw(false);
    }
    
    
    // *words3_2* updates
    if (t >= 0.0 && words3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      words3_2.tStart = t;  // (not accounting for frame time here)
      words3_2.frameNStart = frameN;  // exact frame index
      
      words3_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (words3_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      words3_2.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_12* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_12.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_12.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_12.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_12.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_12.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_12.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_12.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_12.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_12_allKeys = _debugging_press_enter_to_skip_12_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_12_allKeys.length > 0) {
        debugging_press_enter_to_skip_12.keys = _debugging_press_enter_to_skip_12_allKeys[_debugging_press_enter_to_skip_12_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_12.rt = _debugging_press_enter_to_skip_12_allKeys[_debugging_press_enter_to_skip_12_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_12.duration = _debugging_press_enter_to_skip_12_allKeys[_debugging_press_enter_to_skip_12_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of amharic3_BComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function amharic3_BRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'amharic3_B' ---
    for (const thisComponent of amharic3_BComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('amharic3_B.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_12.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_12.keys', debugging_press_enter_to_skip_12.keys);
    if (typeof debugging_press_enter_to_skip_12.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_12.rt', debugging_press_enter_to_skip_12.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_12.duration', debugging_press_enter_to_skip_12.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_12.stop();
    if (amharic3_BMaxDurationReached) {
        amharic3_BClock.add(amharic3_BMaxDuration);
    } else {
        amharic3_BClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function test3_NEWRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test3_NEW' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    test3_NEWClock.reset();
    routineTimer.reset();
    test3_NEWMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codeSymbol_7
    /* Syntax Error: Fix Python code */
    textAmharic_7.setText(amharic3);
    textOptionA_7.setText(lottery_list3[0]);
    textOptionB_7.setText(lottery_list3[1]);
    textOptionC_7.setText(lottery_list3[2]);
    textOptionD_7.setText(lottery_list3[3]);
    textDiamond_6.setText(f'''     {lottery_list3[0]}
       {lottery_list3[1]}   {lottery_list3[2]}
         {lottery_list3[3]}''');
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    debugging_press_enter_to_skip_21.keys = undefined;
    debugging_press_enter_to_skip_21.rt = undefined;
    _debugging_press_enter_to_skip_21_allKeys = [];
    psychoJS.experiment.addData('test3_NEW.started', globalClock.getTime());
    test3_NEWMaxDuration = null
    // keep track of which components have finished
    test3_NEWComponents = [];
    test3_NEWComponents.push(textAmharic_7);
    test3_NEWComponents.push(textOptionA_7);
    test3_NEWComponents.push(textOptionB_7);
    test3_NEWComponents.push(textOptionC_7);
    test3_NEWComponents.push(textOptionD_7);
    test3_NEWComponents.push(textDiamond_6);
    test3_NEWComponents.push(key_resp_7);
    test3_NEWComponents.push(debugging_press_enter_to_skip_21);
    
    for (const thisComponent of test3_NEWComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function test3_NEWRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test3_NEW' ---
    // get current time
    t = test3_NEWClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textAmharic_7* updates
    if (t >= 0.0 && textAmharic_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textAmharic_7.tStart = t;  // (not accounting for frame time here)
      textAmharic_7.frameNStart = frameN;  // exact frame index
      
      textAmharic_7.setAutoDraw(true);
    }
    
    
    // *textOptionA_7* updates
    if (t >= 0.5 && textOptionA_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionA_7.tStart = t;  // (not accounting for frame time here)
      textOptionA_7.frameNStart = frameN;  // exact frame index
      
      textOptionA_7.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionA_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionA_7.setAutoDraw(false);
    }
    
    
    // *textOptionB_7* updates
    if (t >= 1.5 && textOptionB_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionB_7.tStart = t;  // (not accounting for frame time here)
      textOptionB_7.frameNStart = frameN;  // exact frame index
      
      textOptionB_7.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionB_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionB_7.setAutoDraw(false);
    }
    
    
    // *textOptionC_7* updates
    if (t >= 2.5 && textOptionC_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionC_7.tStart = t;  // (not accounting for frame time here)
      textOptionC_7.frameNStart = frameN;  // exact frame index
      
      textOptionC_7.setAutoDraw(true);
    }
    
    frameRemains = 2.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionC_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionC_7.setAutoDraw(false);
    }
    
    
    // *textOptionD_7* updates
    if (t >= 3.5 && textOptionD_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionD_7.tStart = t;  // (not accounting for frame time here)
      textOptionD_7.frameNStart = frameN;  // exact frame index
      
      textOptionD_7.setAutoDraw(true);
    }
    
    frameRemains = 3.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionD_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionD_7.setAutoDraw(false);
    }
    
    
    // *textDiamond_6* updates
    if (t >= 4.5 && textDiamond_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textDiamond_6.tStart = t;  // (not accounting for frame time here)
      textDiamond_6.frameNStart = frameN;  // exact frame index
      
      textDiamond_6.setAutoDraw(true);
    }
    
    
    // *key_resp_7* updates
    if (t >= 4.5 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }
    
    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['right', 'up', 'left', 'down', 'space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        key_resp_7.duration = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_7.keys == correctAns3) {
            key_resp_7.corr = 1;
        } else {
            key_resp_7.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *debugging_press_enter_to_skip_21* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_21.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_21.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_21.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_21.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_21.clearEvents(); });
    }
    
    if (debugging_press_enter_to_skip_21.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_21.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_21_allKeys = _debugging_press_enter_to_skip_21_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_21_allKeys.length > 0) {
        debugging_press_enter_to_skip_21.keys = _debugging_press_enter_to_skip_21_allKeys[_debugging_press_enter_to_skip_21_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_21.rt = _debugging_press_enter_to_skip_21_allKeys[_debugging_press_enter_to_skip_21_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_21.duration = _debugging_press_enter_to_skip_21_allKeys[_debugging_press_enter_to_skip_21_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test3_NEWComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function test3_NEWRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test3_NEW' ---
    for (const thisComponent of test3_NEWComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('test3_NEW.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_7.keys === undefined) {
      if (['None','none',undefined].includes(correctAns3)) {
         key_resp_7.corr = 1;  // correct non-response
      } else {
         key_resp_7.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_7.corr, level);
    }
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    psychoJS.experiment.addData('key_resp_7.corr', key_resp_7.corr);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        psychoJS.experiment.addData('key_resp_7.duration', key_resp_7.duration);
        routineTimer.reset();
        }
    
    key_resp_7.stop();
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_21.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_21.keys', debugging_press_enter_to_skip_21.keys);
    if (typeof debugging_press_enter_to_skip_21.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_21.rt', debugging_press_enter_to_skip_21.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_21.duration', debugging_press_enter_to_skip_21.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_21.stop();
    // the Routine "test3_NEW" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function checkForCorr_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'checkForCorr_3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    checkForCorr_3Clock.reset();
    routineTimer.reset();
    checkForCorr_3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_4
    if ((key_resp_7.corr === 1)) {
        checkmark_reps = 1;
        xmark_reps = 0;
    }
    if ((key_resp_7.corr === 0)) {
        checkmark_reps = 0;
        xmark_reps = 1;
    }
    
    psychoJS.experiment.addData('checkForCorr_3.started', globalClock.getTime());
    checkForCorr_3MaxDuration = null
    // keep track of which components have finished
    checkForCorr_3Components = [];
    
    for (const thisComponent of checkForCorr_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function checkForCorr_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'checkForCorr_3' ---
    // get current time
    t = checkForCorr_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of checkForCorr_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function checkForCorr_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'checkForCorr_3' ---
    for (const thisComponent of checkForCorr_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('checkForCorr_3.stopped', globalClock.getTime());
    // the Routine "checkForCorr_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function amharic4_ARoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'amharic4_A' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    amharic4_AClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    amharic4_AMaxDurationReached = false;
    // update component parameters for each repeat
    amharics4.setText(amharic_word_list4[keys[learning_index]][0]);
    words4_image.setImage(amharic_word_list4[keys[learning_index]][2]);
    // Run 'Begin Routine' code from code4
    console.log(((((((("Index: " + keys[learning_index].toString()) + "\n Character: ") + amharic_word_list4[keys[learning_index]][0].toString()) + "\n Meaning: ") + amharic_word_list4[keys[learning_index]][1].toString()) + "\n Image Path: ") + amharic_word_list4[keys[learning_index]][2].toString()));
    
    debugging_press_enter_to_skip_13.keys = undefined;
    debugging_press_enter_to_skip_13.rt = undefined;
    _debugging_press_enter_to_skip_13_allKeys = [];
    psychoJS.experiment.addData('amharic4_A.started', globalClock.getTime());
    amharic4_AMaxDuration = null
    // keep track of which components have finished
    amharic4_AComponents = [];
    amharic4_AComponents.push(amharics4);
    amharic4_AComponents.push(words4_image);
    amharic4_AComponents.push(debugging_press_enter_to_skip_13);
    
    for (const thisComponent of amharic4_AComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function amharic4_ARoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'amharic4_A' ---
    // get current time
    t = amharic4_AClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *amharics4* updates
    if (t >= 0.0 && amharics4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      amharics4.tStart = t;  // (not accounting for frame time here)
      amharics4.frameNStart = frameN;  // exact frame index
      
      amharics4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (amharics4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      amharics4.setAutoDraw(false);
    }
    
    
    // *words4_image* updates
    if (t >= 0.0 && words4_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      words4_image.tStart = t;  // (not accounting for frame time here)
      words4_image.frameNStart = frameN;  // exact frame index
      
      words4_image.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (words4_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      words4_image.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_13* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_13.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_13.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_13.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_13.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_13.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_13.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_13.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_13.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_13_allKeys = _debugging_press_enter_to_skip_13_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_13_allKeys.length > 0) {
        debugging_press_enter_to_skip_13.keys = _debugging_press_enter_to_skip_13_allKeys[_debugging_press_enter_to_skip_13_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_13.rt = _debugging_press_enter_to_skip_13_allKeys[_debugging_press_enter_to_skip_13_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_13.duration = _debugging_press_enter_to_skip_13_allKeys[_debugging_press_enter_to_skip_13_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of amharic4_AComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function amharic4_ARoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'amharic4_A' ---
    for (const thisComponent of amharic4_AComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('amharic4_A.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_13.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_13.keys', debugging_press_enter_to_skip_13.keys);
    if (typeof debugging_press_enter_to_skip_13.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_13.rt', debugging_press_enter_to_skip_13.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_13.duration', debugging_press_enter_to_skip_13.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_13.stop();
    if (amharic4_AMaxDurationReached) {
        amharic4_AClock.add(amharic4_AMaxDuration);
    } else {
        amharic4_AClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function amharic4_BRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'amharic4_B' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    amharic4_BClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    amharic4_BMaxDurationReached = false;
    // update component parameters for each repeat
    amharics4_2.setText(amharic_word_list4[keys[learning_index]][0]);
    words4_2.setText(amharic_word_list4[keys[learning_index]][1]);
    // Run 'Begin Routine' code from code4_2
    console.log(((((((("Index: " + keys[learning_index].toString()) + "\n Character: ") + amharic_word_list4[keys[learning_index]][0].toString()) + "\n Meaning: ") + amharic_word_list4[keys[learning_index]][1].toString()) + "\n Image Path: ") + amharic_word_list4[keys[learning_index]][2].toString()));
    
    debugging_press_enter_to_skip_14.keys = undefined;
    debugging_press_enter_to_skip_14.rt = undefined;
    _debugging_press_enter_to_skip_14_allKeys = [];
    psychoJS.experiment.addData('amharic4_B.started', globalClock.getTime());
    amharic4_BMaxDuration = null
    // keep track of which components have finished
    amharic4_BComponents = [];
    amharic4_BComponents.push(amharics4_2);
    amharic4_BComponents.push(words4_2);
    amharic4_BComponents.push(debugging_press_enter_to_skip_14);
    
    for (const thisComponent of amharic4_BComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function amharic4_BRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'amharic4_B' ---
    // get current time
    t = amharic4_BClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *amharics4_2* updates
    if (t >= 0.0 && amharics4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      amharics4_2.tStart = t;  // (not accounting for frame time here)
      amharics4_2.frameNStart = frameN;  // exact frame index
      
      amharics4_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (amharics4_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      amharics4_2.setAutoDraw(false);
    }
    
    
    // *words4_2* updates
    if (t >= 0.0 && words4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      words4_2.tStart = t;  // (not accounting for frame time here)
      words4_2.frameNStart = frameN;  // exact frame index
      
      words4_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (words4_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      words4_2.setAutoDraw(false);
    }
    
    
    // *debugging_press_enter_to_skip_14* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_14.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_14.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_14.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_14.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_14.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debugging_press_enter_to_skip_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debugging_press_enter_to_skip_14.status = PsychoJS.Status.FINISHED;
        }
      
    if (debugging_press_enter_to_skip_14.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_14.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_14_allKeys = _debugging_press_enter_to_skip_14_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_14_allKeys.length > 0) {
        debugging_press_enter_to_skip_14.keys = _debugging_press_enter_to_skip_14_allKeys[_debugging_press_enter_to_skip_14_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_14.rt = _debugging_press_enter_to_skip_14_allKeys[_debugging_press_enter_to_skip_14_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_14.duration = _debugging_press_enter_to_skip_14_allKeys[_debugging_press_enter_to_skip_14_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of amharic4_BComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function amharic4_BRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'amharic4_B' ---
    for (const thisComponent of amharic4_BComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('amharic4_B.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_14.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_14.keys', debugging_press_enter_to_skip_14.keys);
    if (typeof debugging_press_enter_to_skip_14.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_14.rt', debugging_press_enter_to_skip_14.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_14.duration', debugging_press_enter_to_skip_14.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_14.stop();
    if (amharic4_BMaxDurationReached) {
        amharic4_BClock.add(amharic4_BMaxDuration);
    } else {
        amharic4_BClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function test4_NEWRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'test4_NEW' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    test4_NEWClock.reset();
    routineTimer.reset();
    test4_NEWMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codeSymbol_8
    /* Syntax Error: Fix Python code */
    textAmharic_8.setText(amharic4);
    textOptionA_8.setText(lottery_list4[0]);
    textOptionB_8.setText(lottery_list4[1]);
    textOptionC_8.setText(lottery_list4[2]);
    textOptionD_8.setText(lottery_list4[3]);
    textDiamond_7.setText(f'''     {lottery_list4[0]}
       {lottery_list4[1]}   {lottery_list4[2]}
         {lottery_list4[3]}''');
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    debugging_press_enter_to_skip_22.keys = undefined;
    debugging_press_enter_to_skip_22.rt = undefined;
    _debugging_press_enter_to_skip_22_allKeys = [];
    psychoJS.experiment.addData('test4_NEW.started', globalClock.getTime());
    test4_NEWMaxDuration = null
    // keep track of which components have finished
    test4_NEWComponents = [];
    test4_NEWComponents.push(textAmharic_8);
    test4_NEWComponents.push(textOptionA_8);
    test4_NEWComponents.push(textOptionB_8);
    test4_NEWComponents.push(textOptionC_8);
    test4_NEWComponents.push(textOptionD_8);
    test4_NEWComponents.push(textDiamond_7);
    test4_NEWComponents.push(key_resp_8);
    test4_NEWComponents.push(debugging_press_enter_to_skip_22);
    
    for (const thisComponent of test4_NEWComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function test4_NEWRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test4_NEW' ---
    // get current time
    t = test4_NEWClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textAmharic_8* updates
    if (t >= 0.0 && textAmharic_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textAmharic_8.tStart = t;  // (not accounting for frame time here)
      textAmharic_8.frameNStart = frameN;  // exact frame index
      
      textAmharic_8.setAutoDraw(true);
    }
    
    
    // *textOptionA_8* updates
    if (t >= 0.5 && textOptionA_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionA_8.tStart = t;  // (not accounting for frame time here)
      textOptionA_8.frameNStart = frameN;  // exact frame index
      
      textOptionA_8.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionA_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionA_8.setAutoDraw(false);
    }
    
    
    // *textOptionB_8* updates
    if (t >= 1.5 && textOptionB_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionB_8.tStart = t;  // (not accounting for frame time here)
      textOptionB_8.frameNStart = frameN;  // exact frame index
      
      textOptionB_8.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionB_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionB_8.setAutoDraw(false);
    }
    
    
    // *textOptionC_8* updates
    if (t >= 2.5 && textOptionC_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionC_8.tStart = t;  // (not accounting for frame time here)
      textOptionC_8.frameNStart = frameN;  // exact frame index
      
      textOptionC_8.setAutoDraw(true);
    }
    
    frameRemains = 2.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionC_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionC_8.setAutoDraw(false);
    }
    
    
    // *textOptionD_8* updates
    if (t >= 3.5 && textOptionD_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textOptionD_8.tStart = t;  // (not accounting for frame time here)
      textOptionD_8.frameNStart = frameN;  // exact frame index
      
      textOptionD_8.setAutoDraw(true);
    }
    
    frameRemains = 3.5 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textOptionD_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textOptionD_8.setAutoDraw(false);
    }
    
    
    // *textDiamond_7* updates
    if (t >= 4.5 && textDiamond_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textDiamond_7.tStart = t;  // (not accounting for frame time here)
      textDiamond_7.frameNStart = frameN;  // exact frame index
      
      textDiamond_7.setAutoDraw(true);
    }
    
    
    // *key_resp_8* updates
    if (t >= 4.5 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }
    
    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['right', 'up', 'left', 'down', 'space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        key_resp_8.duration = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_8.keys == correctAns4) {
            key_resp_8.corr = 1;
        } else {
            key_resp_8.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *debugging_press_enter_to_skip_22* updates
    if (t >= 0.0 && debugging_press_enter_to_skip_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debugging_press_enter_to_skip_22.tStart = t;  // (not accounting for frame time here)
      debugging_press_enter_to_skip_22.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_22.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_22.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { debugging_press_enter_to_skip_22.clearEvents(); });
    }
    
    if (debugging_press_enter_to_skip_22.status === PsychoJS.Status.STARTED) {
      let theseKeys = debugging_press_enter_to_skip_22.getKeys({keyList: ['return'], waitRelease: false});
      _debugging_press_enter_to_skip_22_allKeys = _debugging_press_enter_to_skip_22_allKeys.concat(theseKeys);
      if (_debugging_press_enter_to_skip_22_allKeys.length > 0) {
        debugging_press_enter_to_skip_22.keys = _debugging_press_enter_to_skip_22_allKeys[_debugging_press_enter_to_skip_22_allKeys.length - 1].name;  // just the last key pressed
        debugging_press_enter_to_skip_22.rt = _debugging_press_enter_to_skip_22_allKeys[_debugging_press_enter_to_skip_22_allKeys.length - 1].rt;
        debugging_press_enter_to_skip_22.duration = _debugging_press_enter_to_skip_22_allKeys[_debugging_press_enter_to_skip_22_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of test4_NEWComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function test4_NEWRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test4_NEW' ---
    for (const thisComponent of test4_NEWComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('test4_NEW.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_8.keys === undefined) {
      if (['None','none',undefined].includes(correctAns4)) {
         key_resp_8.corr = 1;  // correct non-response
      } else {
         key_resp_8.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_8.corr, level);
    }
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    psychoJS.experiment.addData('key_resp_8.corr', key_resp_8.corr);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        psychoJS.experiment.addData('key_resp_8.duration', key_resp_8.duration);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(debugging_press_enter_to_skip_22.corr, level);
    }
    psychoJS.experiment.addData('debugging_press_enter_to_skip_22.keys', debugging_press_enter_to_skip_22.keys);
    if (typeof debugging_press_enter_to_skip_22.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('debugging_press_enter_to_skip_22.rt', debugging_press_enter_to_skip_22.rt);
        psychoJS.experiment.addData('debugging_press_enter_to_skip_22.duration', debugging_press_enter_to_skip_22.duration);
        routineTimer.reset();
        }
    
    debugging_press_enter_to_skip_22.stop();
    // the Routine "test4_NEW" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function checkForCorr_4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'checkForCorr_4' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    checkForCorr_4Clock.reset();
    routineTimer.reset();
    checkForCorr_4MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_5
    if ((key_resp_8.corr === 1)) {
        checkmark_reps = 1;
        xmark_reps = 0;
    }
    if ((key_resp_8.corr === 0)) {
        checkmark_reps = 0;
        xmark_reps = 1;
    }
    
    psychoJS.experiment.addData('checkForCorr_4.started', globalClock.getTime());
    checkForCorr_4MaxDuration = null
    // keep track of which components have finished
    checkForCorr_4Components = [];
    
    for (const thisComponent of checkForCorr_4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function checkForCorr_4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'checkForCorr_4' ---
    // get current time
    t = checkForCorr_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of checkForCorr_4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function checkForCorr_4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'checkForCorr_4' ---
    for (const thisComponent of checkForCorr_4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('checkForCorr_4.stopped', globalClock.getTime());
    // the Routine "checkForCorr_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function WelcomeSlideRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'WelcomeSlide' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    WelcomeSlideClock.reset();
    routineTimer.reset();
    WelcomeSlideMaxDurationReached = false;
    // update component parameters for each repeat
    goNext.keys = undefined;
    goNext.rt = undefined;
    _goNext_allKeys = [];
    psychoJS.experiment.addData('WelcomeSlide.started', globalClock.getTime());
    WelcomeSlideMaxDuration = null
    // keep track of which components have finished
    WelcomeSlideComponents = [];
    WelcomeSlideComponents.push(Welcome);
    WelcomeSlideComponents.push(goNext);
    
    for (const thisComponent of WelcomeSlideComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function WelcomeSlideRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'WelcomeSlide' ---
    // get current time
    t = WelcomeSlideClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Welcome* updates
    if (t >= 0.0 && Welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Welcome.tStart = t;  // (not accounting for frame time here)
      Welcome.frameNStart = frameN;  // exact frame index
      
      Welcome.setAutoDraw(true);
    }
    
    
    // *goNext* updates
    if (t >= 0.0 && goNext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      goNext.tStart = t;  // (not accounting for frame time here)
      goNext.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { goNext.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { goNext.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { goNext.clearEvents(); });
    }
    
    if (goNext.status === PsychoJS.Status.STARTED) {
      let theseKeys = goNext.getKeys({keyList: ['return'], waitRelease: false});
      _goNext_allKeys = _goNext_allKeys.concat(theseKeys);
      if (_goNext_allKeys.length > 0) {
        goNext.keys = _goNext_allKeys[_goNext_allKeys.length - 1].name;  // just the last key pressed
        goNext.rt = _goNext_allKeys[_goNext_allKeys.length - 1].rt;
        goNext.duration = _goNext_allKeys[_goNext_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WelcomeSlideComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function WelcomeSlideRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'WelcomeSlide' ---
    for (const thisComponent of WelcomeSlideComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('WelcomeSlide.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(goNext.corr, level);
    }
    psychoJS.experiment.addData('goNext.keys', goNext.keys);
    if (typeof goNext.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('goNext.rt', goNext.rt);
        psychoJS.experiment.addData('goNext.duration', goNext.duration);
        routineTimer.reset();
        }
    
    goNext.stop();
    // the Routine "WelcomeSlide" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    InstructionsClock.reset();
    routineTimer.reset();
    InstructionsMaxDurationReached = false;
    // update component parameters for each repeat
    goNext1.keys = undefined;
    goNext1.rt = undefined;
    _goNext1_allKeys = [];
    psychoJS.experiment.addData('Instructions.started', globalClock.getTime());
    InstructionsMaxDuration = null
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(instructions_text);
    InstructionsComponents.push(goNext1);
    
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instructions' ---
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_text* updates
    if (t >= 0.0 && instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_text.tStart = t;  // (not accounting for frame time here)
      instructions_text.frameNStart = frameN;  // exact frame index
      
      instructions_text.setAutoDraw(true);
    }
    
    
    // *goNext1* updates
    if (t >= 0.0 && goNext1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      goNext1.tStart = t;  // (not accounting for frame time here)
      goNext1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { goNext1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { goNext1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { goNext1.clearEvents(); });
    }
    
    if (goNext1.status === PsychoJS.Status.STARTED) {
      let theseKeys = goNext1.getKeys({keyList: ['return'], waitRelease: false});
      _goNext1_allKeys = _goNext1_allKeys.concat(theseKeys);
      if (_goNext1_allKeys.length > 0) {
        goNext1.keys = _goNext1_allKeys[_goNext1_allKeys.length - 1].name;  // just the last key pressed
        goNext1.rt = _goNext1_allKeys[_goNext1_allKeys.length - 1].rt;
        goNext1.duration = _goNext1_allKeys[_goNext1_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instructions' ---
    for (const thisComponent of InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(goNext1.corr, level);
    }
    psychoJS.experiment.addData('goNext1.keys', goNext1.keys);
    if (typeof goNext1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('goNext1.rt', goNext1.rt);
        psychoJS.experiment.addData('goNext1.duration', goNext1.duration);
        routineTimer.reset();
        }
    
    goNext1.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function TestQuestionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TestQuestion' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    TestQuestionClock.reset();
    routineTimer.reset();
    TestQuestionMaxDurationReached = false;
    // update component parameters for each repeat
    answer_box.setText('');
    answer_box.refresh();
    answer_box.setPlaceholder('');
    enter.keys = undefined;
    enter.rt = undefined;
    _enter_allKeys = [];
    // Run 'Begin Routine' code from RandomQuestion
    if ((curr_item < 24)) {
        curr_item += 1;
    }
    
    psychoJS.experiment.addData('TestQuestion.started', globalClock.getTime());
    TestQuestionMaxDuration = null
    // keep track of which components have finished
    TestQuestionComponents = [];
    TestQuestionComponents.push(answer_box);
    TestQuestionComponents.push(enter);
    TestQuestionComponents.push(symbol);
    
    for (const thisComponent of TestQuestionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function TestQuestionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TestQuestion' ---
    // get current time
    t = TestQuestionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *answer_box* updates
    if (t >= 0.0 && answer_box.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer_box.tStart = t;  // (not accounting for frame time here)
      answer_box.frameNStart = frameN;  // exact frame index
      
      answer_box.setAutoDraw(true);
    }
    
    
    // *enter* updates
    if (t >= 0.0 && enter.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enter.tStart = t;  // (not accounting for frame time here)
      enter.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enter.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enter.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enter.clearEvents(); });
    }
    
    if (enter.status === PsychoJS.Status.STARTED) {
      let theseKeys = enter.getKeys({keyList: ['return'], waitRelease: false});
      _enter_allKeys = _enter_allKeys.concat(theseKeys);
      if (_enter_allKeys.length > 0) {
        enter.keys = _enter_allKeys[_enter_allKeys.length - 1].name;  // just the last key pressed
        enter.rt = _enter_allKeys[_enter_allKeys.length - 1].rt;
        enter.duration = _enter_allKeys[_enter_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    if (symbol.status === PsychoJS.Status.STARTED){ // only update if being drawn
      symbol.setText(test_questions[curr_item][0], false);
    }
    
    // *symbol* updates
    if (t >= 0.0 && symbol.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      symbol.tStart = t;  // (not accounting for frame time here)
      symbol.frameNStart = frameN;  // exact frame index
      
      symbol.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of TestQuestionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function TestQuestionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TestQuestion' ---
    for (const thisComponent of TestQuestionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('TestQuestion.stopped', globalClock.getTime());
    psychoJS.experiment.addData('answer_box.text',answer_box.text)
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(enter.corr, level);
    }
    psychoJS.experiment.addData('enter.keys', enter.keys);
    if (typeof enter.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enter.rt', enter.rt);
        psychoJS.experiment.addData('enter.duration', enter.duration);
        routineTimer.reset();
        }
    
    enter.stop();
    // the Routine "TestQuestion" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function EvaluateRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Evaluate' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    EvaluateClock.reset();
    routineTimer.reset();
    EvaluateMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from CorrectAnswers
    if ((answer_box.text.strip().toUpperCase() === test_questions[curr_item][1].toUpperCase())) {
        correct += 1;
        console.log(("Debugging: This is correct\n Correct = " + correct.toString()));
    }
    
    psychoJS.experiment.addData('Evaluate.started', globalClock.getTime());
    EvaluateMaxDuration = null
    // keep track of which components have finished
    EvaluateComponents = [];
    
    for (const thisComponent of EvaluateComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function EvaluateRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Evaluate' ---
    // get current time
    t = EvaluateClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EvaluateComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function EvaluateRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Evaluate' ---
    for (const thisComponent of EvaluateComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Evaluate.stopped', globalClock.getTime());
    // the Routine "Evaluate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function ThankYouRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ThankYou' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ThankYouClock.reset();
    routineTimer.reset();
    ThankYouMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from Debug
    thankyoumessage = (("Thank you for participating, You got " + correct.toString()) + " out of 24 correct");
    
    psychoJS.experiment.addData('ThankYou.started', globalClock.getTime());
    ThankYouMaxDuration = null
    // keep track of which components have finished
    ThankYouComponents = [];
    
    for (const thisComponent of ThankYouComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function ThankYouRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ThankYou' ---
    // get current time
    t = ThankYouClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ThankYouComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function ThankYouRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ThankYou' ---
    for (const thisComponent of ThankYouComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ThankYou.stopped', globalClock.getTime());
    // the Routine "ThankYou" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
