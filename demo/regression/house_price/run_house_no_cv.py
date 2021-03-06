# Copyright (c) 2018 by contributors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import xlearn as xl

# Training task
fm_model = xl.create_fm() # Use factorization machine
fm_model.setTrain("./house_price_train.txt")    # Training data
fm_model.setValidate("./house_price_test.txt")  # Validation data

# param:
#  0. regression task
#  1. learning rate: 0.2
#  2. regular lambda: 0.002
#  3. evaluation metric: accuracy
param = {'task':'reg', 'lr':0.2, 
         'lambda':0.002, 'metric':'mae'}

# Start to train
# The trained model will be stored in model.out
fm_model.fit(param, './model.out')

# Prediction task
fm_model.setTest("./house_price_test.txt")  # Test data
fm_model.setSigmoid()  # Convert output to 0-1

# Start to predict
# The output result will be stored in output.txt
fm_model.predict("./model.out", "./output.txt")