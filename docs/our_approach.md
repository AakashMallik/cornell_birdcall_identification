# phase 1

#### pre-processing
- [x] Resampling data (32KHz) and save it as **wav** files
- [ ] Create stratified k-folds out of it
- [ ] Prepare a caching mechanism that does not regenerate spectrogram if there is no change in underlying audio (no audio transformation)
- [x] Use an effective length of 5 sec, by padding or by clipping the recording ⭐️

#### Model