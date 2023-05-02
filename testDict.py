testDataDict = {
    'tBodyAcc-mean()-X': [],
    "tBodyAcc-mean()-Y": [], 
    "tBodyAcc-mean()-Z": [], 
    "tBodyAcc-std()-X": [], 
    "tBodyAcc-std()-Y": [], 
    "tBodyAcc-std()-Z": [], 
    "tBodyAcc-mad()-X": [], 
    "tBodyAcc-mad()-Y": [], 
    "tBodyAcc-mad()-Z": [], 
    "tBodyAcc-max()-X": [], 
    "tBodyAcc-max()-Y": [], 
    "tBodyAcc-max()-Z": [], 
    "tBodyAcc-min()-X": [], 
    "tBodyAcc-min()-Y": [], 
    "tBodyAcc-min()-Z": [], 
    "tBodyAcc-sma()": [], 
    "tBodyAcc-energy()-X": [], #?
    "tBodyAcc-energy()-Y": [], #?
    "tBodyAcc-energy()-Z": [], #?
    "tBodyAcc-iqr()-X": [], 
    "tBodyAcc-iqr()-Y": [], 
    "tBodyAcc-iqr()-Z": [], 
    "tBodyAcc-entropy()-X": [], 
    "tBodyAcc-entropy()-Y": [], 
    "tBodyAcc-entropy()-Z": [], 
    "tBodyAcc-arCoeff()-X,1": [], 
    "tBodyAcc-arCoeff()-X,2": [], 
    "tBodyAcc-arCoeff()-X,3": [], 
    "tBodyAcc-arCoeff()-X,4": [], 
    "tBodyAcc-arCoeff()-Y,1": [], 
    "tBodyAcc-arCoeff()-Y,2": [], 
    "tBodyAcc-arCoeff()-Y,3": [], 
    "tBodyAcc-arCoeff()-Y,4": [], 
    "tBodyAcc-arCoeff()-Z,1": [], 
    "tBodyAcc-arCoeff()-Z,2": [], 
    "tBodyAcc-arCoeff()-Z,3": [], 
    "tBodyAcc-arCoeff()-Z,4": [], 
    "tBodyAcc-correlation()-X,Y": [], 
    "tBodyAcc-correlation()-X,Z": [], 
    "tBodyAcc-correlation()-Y,Z": [], 
    "tGravityAcc-mean()-X": [], 
    "tGravityAcc-mean()-Y": [], 
    "tGravityAcc-mean()-Z": [], 
    "tGravityAcc-std()-X": [], 
    "tGravityAcc-std()-Y": [], 
    "tGravityAcc-std()-Z": [], 
    "tGravityAcc-mad()-X": [], 
    "tGravityAcc-mad()-Y": [], 
    "tGravityAcc-mad()-Z": [], 
    "tGravityAcc-max()-X": [], 
    "tGravityAcc-max()-Y": [], 
    "tGravityAcc-max()-Z": [], 
    "tGravityAcc-min()-X": [],
    'tGravityAcc-min()-Y': [],
    'tGravityAcc-min()-Z': [],
    'tGravityAcc-sma()': [],
    'tGravityAcc-energy()-X': [],
    'tGravityAcc-energy()-Y': [],
    'tGravityAcc-energy()-Z': [],
    'tGravityAcc-iqr()-X': [],
    'tGravityAcc-iqr()-Y': [],
    'tGravityAcc-iqr()-Z': [],
    'tGravityAcc-entropy()-X': [],
    'tGravityAcc-entropy()-Y': [],
    'tGravityAcc-entropy()-Z': [],
    'tGravityAcc-arCoeff()-X,1': [],
    'tGravityAcc-arCoeff()-X,2': [],
    'tGravityAcc-arCoeff()-X,3': [],
    'tGravityAcc-arCoeff()-X,4': [],
    'tGravityAcc-arCoeff()-Y,1': [],
    'tGravityAcc-arCoeff()-Y,2': [],
    'tGravityAcc-arCoeff()-Y,3': [],
    'tGravityAcc-arCoeff()-Y,4': [],
    'tGravityAcc-arCoeff()-Z,1': [],
    'tGravityAcc-arCoeff()-Z,2': [],
    'tGravityAcc-arCoeff()-Z,3': [],
    'tGravityAcc-arCoeff()-Z,4': [],
    'tGravityAcc-correlation()-X,Y': [],
    'tGravityAcc-correlation()-X,Z': [],
    'tGravityAcc-correlation()-Y,Z': [],
    'tBodyAccJerk-mean()-X': [],
    'tBodyAccJerk-mean()-Y': [],
    'tBodyAccJerk-mean()-Z': [],
    'tBodyAccJerk-std()-X': [],
    'tBodyAccJerk-std()-Y': [],
    'tBodyAccJerk-std()-Z': [],
    'tBodyAccJerk-mad()-X': [],
    'tBodyAccJerk-mad()-Y': [],
    'tBodyAccJerk-mad()-Z': [],
    'tBodyAccJerk-max()-X': [],
    'tBodyAccJerk-max()-Y': [],
    'tBodyAccJerk-max()-Z': [],
    'tBodyAccJerk-min()-X': [],
    'tBodyAccJerk-min()-Y': [],
    'tBodyAccJerk-min()-Z': [],
    'tBodyAccJerk-sma()': [],
    'tBodyAccJerk-energy()-X': [],
    'tBodyAccJerk-energy()-Y': [],
    'tBodyAccJerk-energy()-Z': [],
    'tBodyAccJerk-iqr()-X': [],
    'tBodyAccJerk-iqr()-Y': [],
    'tBodyAccJerk-iqr()-Z': [],
    'tBodyAccJerk-entropy()-X': [],
    'tBodyAccJerk-entropy()-Y': [],
    'tBodyAccJerk-entropy()-Z': [],
    'tBodyAccJerk-arCoeff()-X,1': [],
    'tBodyAccJerk-arCoeff()-X,2': [],
    'tBodyAccJerk-arCoeff()-X,3': [],
    'tBodyAccJerk-arCoeff()-X,4': [],
    'tBodyAccJerk-arCoeff()-Y,1': [],
    'tBodyAccJerk-arCoeff()-Y,2': [],
    'tBodyAccJerk-arCoeff()-Y,3': [],
    'tBodyAccJerk-arCoeff()-Y,4': [],
    'tBodyAccJerk-arCoeff()-Z,1': [],
    'tBodyAccJerk-arCoeff()-Z,2': [],
    'tBodyAccJerk-arCoeff()-Z,3': [],
    'tBodyAccJerk-arCoeff()-Z,4': [],
    'tBodyAccJerk-correlation()-X,Y': [],
    'tBodyAccJerk-correlation()-X,Z': [],
    'tBodyAccJerk-correlation()-Y,Z': [],
    'tBodyAccMag-mean()': [],
    'tBodyAccMag-std()': [],
    'tBodyAccMag-mad()': [],
    'tBodyAccMag-max()': [],
    'tBodyAccMag-min()': [],
    'tBodyAccMag-sma()': [],
    'tBodyAccMag-energy()': [],
    'tBodyAccMag-iqr()': [],
    'tBodyAccMag-entropy()': [],
    'tBodyAccMag-arCoeff()1': [],
    'tBodyAccMag-arCoeff()2': [],
    'tBodyAccMag-arCoeff()3': [],
    'tBodyAccMag-arCoeff()4': [],
    'tGravityAccMag-mean()': [],
    'tGravityAccMag-std()': [],
    'tGravityAccMag-mad()': [],
    'tGravityAccMag-max()': [],
    'tGravityAccMag-min()': [],
    'tGravityAccMag-sma()': [],
    'tGravityAccMag-energy()': [],
    'tGravityAccMag-iqr()': [],
    'tGravityAccMag-entropy()': [],
    'tGravityAccMag-arCoeff()1': [],
    'tGravityAccMag-arCoeff()2': [],
    'tGravityAccMag-arCoeff()3': [],
    'tGravityAccMag-arCoeff()4': [],
    'tBodyAccJerkMag-mean()': [],
    'tBodyAccJerkMag-std()': [],
    'tBodyAccJerkMag-mad()': [],
    'tBodyAccJerkMag-max()': [],
    'tBodyAccJerkMag-min()': [],
    'tBodyAccJerkMag-sma()': [],
    'tBodyAccJerkMag-energy()': [],
    'tBodyAccJerkMag-iqr()': [],
    'tBodyAccJerkMag-entropy()': [],
    'tBodyAccJerkMag-arCoeff()1': [],
    'tBodyAccJerkMag-arCoeff()2': [],
    'tBodyAccJerkMag-arCoeff()3': [],
    'tBodyAccJerkMag-arCoeff()4':[],
    'fBodyAcc-mean()-X':[], 
    'fBodyAcc-mean()-Y':[],
    'fBodyAcc-mean()-Z':[],
    'fBodyAcc-std()-X':[],
    'fBodyAcc-std()-Y':[],
    'fBodyAcc-std()-Z':[],
    'fBodyAcc-mad()-X':[], 
    'fBodyAcc-mad()-Y':[], 
    'fBodyAcc-mad()-Z':[],
    'fBodyAcc-max()-X':[], 
    'fBodyAcc-max()-Y':[], 
    'fBodyAcc-max()-Z':[],
    'fBodyAcc-min()-X':[],
    'fBodyAcc-min()-Y':[], 
    'fBodyAcc-min()-Z':[],
    'fBodyAcc-sma()':[], 
    'fBodyAcc-energy()-X':[], 
    'fBodyAcc-energy()-Y':[],
    'fBodyAcc-energy()-Z':[], 
    'fBodyAcc-iqr()-X':[], 
    'fBodyAcc-iqr()-Y':[],
    'fBodyAcc-iqr()-Z':[], 
    'fBodyAcc-entropy()-X':[], 
    'fBodyAcc-entropy()-Y':[],
    'fBodyAcc-entropy()-Z':[], 
    'fBodyAcc-maxInds-X':[], 
    'fBodyAcc-maxInds-Y':[],
    'fBodyAcc-maxInds-Z':[], 
    'fBodyAcc-meanFreq()-X':[], 
    'fBodyAcc-meanFreq()-Y':[],
    'fBodyAcc-meanFreq()-Z':[], 
    'fBodyAcc-skewness()-X':[], 
    'fBodyAcc-kurtosis()-X':[],
    'fBodyAcc-skewness()-Y':[], 
    'fBodyAcc-kurtosis()-Y':[], 
    'fBodyAcc-skewness()-Z':[],
    'fBodyAcc-kurtosis()-Z':[], 
    'fBodyAcc-bandsEnergy()-1,8':[], 
    'fBodyAcc-bandsEnergy()-9,16':[],
    'fBodyAcc-bandsEnergy()-17,24':[], 
    'fBodyAcc-bandsEnergy()-25,32':[], 
    'fBodyAcc-bandsEnergy()-33,40':[],
    'fBodyAcc-bandsEnergy()-41,48':[], 
    'fBodyAcc-bandsEnergy()-49,56':[], 
    'fBodyAcc-bandsEnergy()-57,64':[],
    'fBodyAcc-bandsEnergy()-1,16':[], 
    'fBodyAcc-bandsEnergy()-17,32':[], 
    'fBodyAcc-bandsEnergy()-33,48':[],
    'fBodyAcc-bandsEnergy()-49,64':[], 
    'fBodyAcc-bandsEnergy()-1,24':[], 
    'fBodyAcc-bandsEnergy()-25,48':[],
    'fBodyAcc-bandsEnergy()-1,8':[], 
    'fBodyAcc-bandsEnergy()-9,16':[], 
    'fBodyAcc-bandsEnergy()-17,24':[],
    'fBodyAcc-bandsEnergy()-25,32':[], 
    'fBodyAcc-bandsEnergy()-33,40':[], 
    'fBodyAcc-bandsEnergy()-41,48':[],
    'fBodyAcc-bandsEnergy()-49,56':[], 
    'fBodyAcc-bandsEnergy()-57,64':[], 
    'fBodyAcc-bandsEnergy()-1,16':[],
    'fBodyAcc-bandsEnergy()-17,32':[], 
    'fBodyAcc-bandsEnergy()-33,48':[], 
    'fBodyAcc-bandsEnergy()-49,64':[],
    'fBodyAcc-bandsEnergy()-1,24':[], 
    'fBodyAcc-bandsEnergy()-25,48':[], 
    'fBodyAccJerk-mean()-X':[],
    'fBodyAccJerk-mean()-Y':[],
    'fBodyAccJerk-mean()-Z':[],
    'fBodyAccJerk-std()-X':[],
    'fBodyAccJerk-std()-Y':[],
    'fBodyAccJerk-std()-Z':[],
    'fBodyAccJerk-mad()-X':[],
    'fBodyAccJerk-mad()-Y':[],
    'fBodyAccJerk-mad()-Z':[],
    'fBodyAccJerk-max()-X':[],
    'fBodyAccJerk-max()-Y':[],
    'fBodyAccJerk-max()-Z':[],
    'fBodyAccJerk-min()-X':[],
    'fBodyAccJerk-min()-Y':[],
    'fBodyAccJerk-min()-Z':[],
    'fBodyAccJerk-sma()':[],
    'fBodyAccJerk-energy()-X':[],
    'fBodyAccJerk-energy()-Y':[],
    'fBodyAccJerk-energy()-Z':[],
    'fBodyAccJerk-iqr()-X':[],
    'fBodyAccJerk-iqr()-Y':[],
    'fBodyAccJerk-iqr()-Z':[],
    'fBodyAccJerk-entropy()-X':[],
    'fBodyAccJerk-entropy()-Y':[],
    'fBodyAccJerk-entropy()-Z':[],
    'fBodyAccJerk-maxInds-X':[],
    'fBodyAccJerk-maxInds-Y':[],
    'fBodyAccJerk-maxInds-Z':[],
    'fBodyAccJerk-meanFreq()-X':[],
    'fBodyAccJerk-meanFreq()-Y':[],
    'fBodyAccJerk-meanFreq()-Z':[],
    'fBodyAccJerk-skewness()-X':[],
    'fBodyAccJerk-kurtosis()-X':[],
    'fBodyAccJerk-skewness()-Y':[],
    'fBodyAccJerk-kurtosis()-Y':[],
    'fBodyAccJerk-skewness()-Z':[],
    'fBodyAccJerk-kurtosis()-Z':[],
    'fBodyAccJerk-bandsEnergy()-1,8':[],
    'fBodyAccJerk-bandsEnergy()-9,16':[],
    'fBodyAccJerk-bandsEnergy()-17,24':[],
    'fBodyAccJerk-bandsEnergy()-25,32':[],
    'fBodyAccJerk-bandsEnergy()-33,40':[],
    'fBodyAccJerk-bandsEnergy()-41,48':[],
    'fBodyAccJerk-bandsEnergy()-49,56':[],
    'fBodyAccJerk-bandsEnergy()-57,64':[],
    'fBodyAccJerk-bandsEnergy()-1,16':[],
    'fBodyAccJerk-bandsEnergy()-17,32':[],
    'fBodyAccJerk-bandsEnergy()-33,48':[],
    'fBodyAccJerk-bandsEnergy()-49,64':[],
    'fBodyAccJerk-bandsEnergy()-1,24':[],
    'fBodyAccJerk-bandsEnergy()-25,48':[],
    'fBodyAccJerk-bandsEnergy()-1,8':[],
    'fBodyAccJerk-bandsEnergy()-9,16':[],
    'fBodyAccJerk-bandsEnergy()-17,24':[],
    'fBodyAccJerk-bandsEnergy()-25,32':[],
    'fBodyAccJerk-bandsEnergy()-33,40':[],
    'fBodyAccJerk-bandsEnergy()-41,48':[],
    'fBodyAccJerk-bandsEnergy()-49,56':[],
    'fBodyAccJerk-bandsEnergy()-57,64':[],
    'fBodyAccJerk-bandsEnergy()-1,16':[],
    'fBodyAccJerk-bandsEnergy()-17,32':[],
    'fBodyAccJerk-bandsEnergy()-33,48':[],
    'fBodyAccJerk-bandsEnergy()-49,64':[],
    'fBodyAccJerk-bandsEnergy()-1,24':[],
    'fBodyAccJerk-bandsEnergy()-25,48':[],
    'fBodyAccJerk-bandsEnergy()-1,8':[],
    'fBodyAccJerk-bandsEnergy()-9,16':[],
    'fBodyAccJerk-bandsEnergy()-17,24':[],
    'fBodyAccJerk-bandsEnergy()-25,32':[],
    'fBodyAccJerk-bandsEnergy()-33,40':[],
    'fBodyAccJerk-bandsEnergy()-41,48':[],
    'fBodyAccJerk-bandsEnergy()-49,56':[],
    'fBodyAccJerk-bandsEnergy()-57,64':[],
    'fBodyAccJerk-bandsEnergy()-1,16':[],
    'fBodyAccJerk-bandsEnergy()-17,32':[],
    'fBodyAccJerk-bandsEnergy()-33,48':[],
    'fBodyAccJerk-bandsEnergy()-49,64':[],
    'fBodyAccJerk-bandsEnergy()-1,24':[],
    'fBodyAccJerk-bandsEnergy()-25,48':[],
    'fBodyAccMag-mean()':[],
    'fBodyAccMag-std()':[],
    'fBodyAccMag-mad()':[],
    'fBodyAccMag-max()':[],
    'fBodyAccMag-min()':[],
    'fBodyAccMag-sma()':[],
    'fBodyAccMag-energy()':[],
    'fBodyAccMag-iqr()':[],
    'fBodyAccMag-entropy()':[],
    'fBodyAccMag-maxInds':[],
    'fBodyAccMag-meanFreq()':[],
    'fBodyAccMag-skewness()':[],
    'fBodyAccMag-kurtosis()':[],
    'fBodyBodyAccJerkMag-mean()':[],
    'fBodyBodyAccJerkMag-std()':[],
    'fBodyBodyAccJerkMag-mad()':[],
    'fBodyBodyAccJerkMag-max()':[],
    'fBodyBodyAccJerkMag-min()':[],
    'fBodyBodyAccJerkMag-sma()':[],
    'fBodyBodyAccJerkMag-energy()':[],
    'fBodyBodyAccJerkMag-iqr()':[],
    'fBodyBodyAccJerkMag-entropy()':[],
    'fBodyBodyAccJerkMag-maxInds':[],
    'fBodyBodyAccJerkMag-meanFreq()':[],
    'fBodyBodyAccJerkMag-skewness()':[],
    'fBodyBodyAccJerkMag-kurtosis()':[],
    'angle(tBodyAccMean,gravity)':[],
    'angle(tBodyAccJerkMean,gravityMean)':[],
    'angle(X,gravityMean)':[],
    'angle(Y,gravityMean)':[],
    'angle(Z,gravityMean)':[]


}


# 266 fBodyAcc-mean()-X
# 267 fBodyAcc-mean()-Y
# 268 fBodyAcc-mean()-Z
# 269 fBodyAcc-std()-X
# 270 fBodyAcc-std()-Y
# 271 fBodyAcc-std()-Z
# 272 fBodyAcc-mad()-X
# 273 fBodyAcc-mad()-Y
# 274 fBodyAcc-mad()-Z
# 275 fBodyAcc-max()-X
# 276 fBodyAcc-max()-Y
# 277 fBodyAcc-max()-Z
# 278 fBodyAcc-min()-X
# 279 fBodyAcc-min()-Y
# 280 fBodyAcc-min()-Z
# 281 fBodyAcc-sma()
# 282 fBodyAcc-energy()-X
# 283 fBodyAcc-energy()-Y
# 284 fBodyAcc-energy()-Z
# 285 fBodyAcc-iqr()-X
# 286 fBodyAcc-iqr()-Y
# 287 fBodyAcc-iqr()-Z
# 288 fBodyAcc-entropy()-X
# 289 fBodyAcc-entropy()-Y
# 290 fBodyAcc-entropy()-Z
# 291 fBodyAcc-maxInds-X
# 292 fBodyAcc-maxInds-Y
# 293 fBodyAcc-maxInds-Z
# 294 fBodyAcc-meanFreq()-X
# 295 fBodyAcc-meanFreq()-Y
# 296 fBodyAcc-meanFreq()-Z
# 297 fBodyAcc-skewness()-X
# 298 fBodyAcc-kurtosis()-X
# 299 fBodyAcc-skewness()-Y
# 300 fBodyAcc-kurtosis()-Y
# 301 fBodyAcc-skewness()-Z
# 302 fBodyAcc-kurtosis()-Z
# 303 fBodyAcc-bandsEnergy()-1,8
# 304 fBodyAcc-bandsEnergy()-9,16
# 305 fBodyAcc-bandsEnergy()-17,24
# 306 fBodyAcc-bandsEnergy()-25,32
# 307 fBodyAcc-bandsEnergy()-33,40
# 308 fBodyAcc-bandsEnergy()-41,48
# 309 fBodyAcc-bandsEnergy()-49,56
# 310 fBodyAcc-bandsEnergy()-57,64
# 311 fBodyAcc-bandsEnergy()-1,16
# 312 fBodyAcc-bandsEnergy()-17,32
# 313 fBodyAcc-bandsEnergy()-33,48
# 314 fBodyAcc-bandsEnergy()-49,64
# 315 fBodyAcc-bandsEnergy()-1,24
# 316 fBodyAcc-bandsEnergy()-25,48
# 317 fBodyAcc-bandsEnergy()-1,8
# 318 fBodyAcc-bandsEnergy()-9,16
# 319 fBodyAcc-bandsEnergy()-17,24
# 320 fBodyAcc-bandsEnergy()-25,32
# 321 fBodyAcc-bandsEnergy()-33,40
# 322 fBodyAcc-bandsEnergy()-41,48
# 323 fBodyAcc-bandsEnergy()-49,56
# 324 fBodyAcc-bandsEnergy()-57,64
# 325 fBodyAcc-bandsEnergy()-1,16
# 326 fBodyAcc-bandsEnergy()-17,32
# 327 fBodyAcc-bandsEnergy()-33,48
# 328 fBodyAcc-bandsEnergy()-49,64
# 329 fBodyAcc-bandsEnergy()-1,24
# 330 fBodyAcc-bandsEnergy()-25,48
# 331 fBodyAcc-bandsEnergy()-1,8
# 332 fBodyAcc-bandsEnergy()-9,16
# 333 fBodyAcc-bandsEnergy()-17,24
# 334 fBodyAcc-bandsEnergy()-25,32
# 335 fBodyAcc-bandsEnergy()-33,40
# 336 fBodyAcc-bandsEnergy()-41,48
# 337 fBodyAcc-bandsEnergy()-49,56
# 338 fBodyAcc-bandsEnergy()-57,64
# 339 fBodyAcc-bandsEnergy()-1,16
# 340 fBodyAcc-bandsEnergy()-17,32
# 341 fBodyAcc-bandsEnergy()-33,48
# 342 fBodyAcc-bandsEnergy()-49,64
# 343 fBodyAcc-bandsEnergy()-1,24
# 344 fBodyAcc-bandsEnergy()-25,48
# 345 fBodyAccJerk-mean()-X
# 346 fBodyAccJerk-mean()-Y
# 347 fBodyAccJerk-mean()-Z
# 348 fBodyAccJerk-std()-X
# 349 fBodyAccJerk-std()-Y
# 350 fBodyAccJerk-std()-Z
# 351 fBodyAccJerk-mad()-X
# 352 fBodyAccJerk-mad()-Y
# 353 fBodyAccJerk-mad()-Z
# 354 fBodyAccJerk-max()-X
# 355 fBodyAccJerk-max()-Y
# 356 fBodyAccJerk-max()-Z
# 357 fBodyAccJerk-min()-X
# 358 fBodyAccJerk-min()-Y
# 359 fBodyAccJerk-min()-Z
# 360 fBodyAccJerk-sma()
# 361 fBodyAccJerk-energy()-X
# 362 fBodyAccJerk-energy()-Y
# 363 fBodyAccJerk-energy()-Z
# 364 fBodyAccJerk-iqr()-X
# 365 fBodyAccJerk-iqr()-Y
# 366 fBodyAccJerk-iqr()-Z
# 367 fBodyAccJerk-entropy()-X
# 368 fBodyAccJerk-entropy()-Y
# 369 fBodyAccJerk-entropy()-Z
# 370 fBodyAccJerk-maxInds-X
# 371 fBodyAccJerk-maxInds-Y
# 372 fBodyAccJerk-maxInds-Z
# 373 fBodyAccJerk-meanFreq()-X
# 374 fBodyAccJerk-meanFreq()-Y
# 375 fBodyAccJerk-meanFreq()-Z
# 376 fBodyAccJerk-skewness()-X
# 377 fBodyAccJerk-kurtosis()-X
# 378 fBodyAccJerk-skewness()-Y
# 379 fBodyAccJerk-kurtosis()-Y
# 380 fBodyAccJerk-skewness()-Z
# 381 fBodyAccJerk-kurtosis()-Z
# 382 fBodyAccJerk-bandsEnergy()-1,8
# 383 fBodyAccJerk-bandsEnergy()-9,16
# 384 fBodyAccJerk-bandsEnergy()-17,24
# 385 fBodyAccJerk-bandsEnergy()-25,32
# 386 fBodyAccJerk-bandsEnergy()-33,40
# 387 fBodyAccJerk-bandsEnergy()-41,48
# 388 fBodyAccJerk-bandsEnergy()-49,56
# 389 fBodyAccJerk-bandsEnergy()-57,64
# 390 fBodyAccJerk-bandsEnergy()-1,16
# 391 fBodyAccJerk-bandsEnergy()-17,32
# 392 fBodyAccJerk-bandsEnergy()-33,48
# 393 fBodyAccJerk-bandsEnergy()-49,64
# 394 fBodyAccJerk-bandsEnergy()-1,24
# 395 fBodyAccJerk-bandsEnergy()-25,48
# 396 fBodyAccJerk-bandsEnergy()-1,8
# 397 fBodyAccJerk-bandsEnergy()-9,16
# 398 fBodyAccJerk-bandsEnergy()-17,24
# 399 fBodyAccJerk-bandsEnergy()-25,32
# 400 fBodyAccJerk-bandsEnergy()-33,40
# 401 fBodyAccJerk-bandsEnergy()-41,48
# 402 fBodyAccJerk-bandsEnergy()-49,56
# 403 fBodyAccJerk-bandsEnergy()-57,64
# 404 fBodyAccJerk-bandsEnergy()-1,16
# 405 fBodyAccJerk-bandsEnergy()-17,32
# 406 fBodyAccJerk-bandsEnergy()-33,48
# 407 fBodyAccJerk-bandsEnergy()-49,64
# 408 fBodyAccJerk-bandsEnergy()-1,24
# 409 fBodyAccJerk-bandsEnergy()-25,48
# 410 fBodyAccJerk-bandsEnergy()-1,8
# 411 fBodyAccJerk-bandsEnergy()-9,16
# 412 fBodyAccJerk-bandsEnergy()-17,24
# 413 fBodyAccJerk-bandsEnergy()-25,32
# 414 fBodyAccJerk-bandsEnergy()-33,40
# 415 fBodyAccJerk-bandsEnergy()-41,48
# 416 fBodyAccJerk-bandsEnergy()-49,56
# 417 fBodyAccJerk-bandsEnergy()-57,64
# 418 fBodyAccJerk-bandsEnergy()-1,16
# 419 fBodyAccJerk-bandsEnergy()-17,32
# 420 fBodyAccJerk-bandsEnergy()-33,48
# 421 fBodyAccJerk-bandsEnergy()-49,64
# 422 fBodyAccJerk-bandsEnergy()-1,24
# 423 fBodyAccJerk-bandsEnergy()-25,48
# 503 fBodyAccMag-mean()
# 504 fBodyAccMag-std()
# 505 fBodyAccMag-mad()
# 506 fBodyAccMag-max()
# 507 fBodyAccMag-min()
# 508 fBodyAccMag-sma()
# 509 fBodyAccMag-energy()
# 510 fBodyAccMag-iqr()
# 511 fBodyAccMag-entropy()
# 512 fBodyAccMag-maxInds
# 513 fBodyAccMag-meanFreq()
# 514 fBodyAccMag-skewness()
# 515 fBodyAccMag-kurtosis()
# 516 fBodyBodyAccJerkMag-mean()
# 517 fBodyBodyAccJerkMag-std()
# 518 fBodyBodyAccJerkMag-mad()
# 519 fBodyBodyAccJerkMag-max()
# 520 fBodyBodyAccJerkMag-min()
# 521 fBodyBodyAccJerkMag-sma()
# 522 fBodyBodyAccJerkMag-energy()
# 523 fBodyBodyAccJerkMag-iqr()
# 524 fBodyBodyAccJerkMag-entropy()
# 525 fBodyBodyAccJerkMag-maxInds
# 526 fBodyBodyAccJerkMag-meanFreq()
# 527 fBodyBodyAccJerkMag-skewness()
# 528 fBodyBodyAccJerkMag-kurtosis()
# 555 angle(tBodyAccMean,gravity)
# 556 angle(tBodyAccJerkMean,gravityMean)
# 559 angle(X,gravityMean)
# 560 angle(Y,gravityMean)
# 561 angle(Z,gravityMean)


with open("/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/featuresAcc.txt", "r") as f:
    lines = f.readlines()
with open("/mnt/c/Users/sltnm/Desktop/FACULTATE/LICENTA/uci_har_dataset/features1.txt", "w") as f:
    for line in lines:
        element = line[3:]
        print(element)
        f.write("'{0}'".format(element))