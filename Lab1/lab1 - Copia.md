```python
```python
import numpy as np,pandas as pd, matplotlib.pyplot as plt 

if __name__ == '__main__':
    x = pd.read_csv('parkinsons_updrs.data')

    x.test_time = x.test_time - x.test_time.min()
    x.test_time = x.test_time.round()
    
    
    
#here I am going to select the first 36 patients
    
    data_train = x[x.subject < 37]
    data_test = x[x.subject > 36]
    data_train = data_train.groupby(["subject","test_time"]).mean()
    data_test = data_test.groupby (["subject","test_time"]).mean()
    Npatients = x.loc[:,"subject"].max()

	```python
	
	PROVA

#normalizing data
    data_test_1 = pd.Series()
    data_test_1 = data_test.copy()
    data_test_norm = pd.Series()
    data_test_norm = data_test.copy()
    data_train_norm = pd.Series()
    data_train_norm = data_train.copy()
    for index in data_train.keys():
        mean_train = data_train[index].mean()
        mean_test = data_test[index].mean()
        data_train_norm[index] -= mean_train
        data_test_norm[index] -= mean_train
        data_test_1[index] -= mean_test
        variance_test = data_test[index].std()
        variance_train = data_train[index].std()
        data_test_1[index] = data_test_1[index] / variance_test
        data_test_norm[index] = data_test_norm[index]/variance_train
        data_train_norm[index] = data_train_norm[index]/variance_train
        
    #uncomment to check that the two vectors are zero mean and with variance = 1
    #print ('VARIANCE TRAIN',data_train.var())
    #print ('MEAN TRAIN',data_train.mean().round())
    #print('VARIANCE TEST',data_test_1.var())
    #print('MEAN TEST',data_test_1.mean().round())
    #print('DATA_TEST_NORM',data_test_norm)
    #print(data_test_norm)

    FO = 'Jitter(%)'
    y_train = data_train_norm[FO]
    X_train = data_train_norm.copy()
    del X_train[FO]
    y_test = data_test_norm[FO]
    X_test = data_test_norm.copy()
    del X_test[FO]
    
    #application on MSE on train
    w_hat = np.dot(X_train.transpose(),X_train)
    w_hat = np.linalg.pinv(w_hat)
    w_hat = np.dot(w_hat, X_train.transpose())
    w_hat = np.dot(w_hat,y_train)
        
    y_hat_train = np.dot(X_train,w_hat)
   
    error_mse_train = np.dot(y_train.transpose(),y_train)
    second_term = np.dot(y_train.transpose(),y_hat_train)
    error_mse_train = error_mse_train - second_term
    plt.figure(1)
    plt.plot(y_hat_train,'g--',y_train.as_matrix(),'r--')
    plt.title('Comparison y_hat_test and y_train')
    plt.figure(3)
    plt.hist(abs(y_train-y_hat_train),bins=50)
    plt.title('Histogram abs diff y_train and y_hat_train')
    plt.figure(5)
    plt.plot(w_hat)
    plt.title('w_hat_train')
    
    #application on MSE on test
    w_hat = np.dot(X_test.transpose(),X_test)
    w_hat = np.linalg.pinv(w_hat)
    w_hat = np.dot(w_hat, X_test.transpose())
    w_hat = np.dot(w_hat,y_test)
        
    y_hat_test = np.dot(X_test,w_hat)
       
    error_mse_test = np.dot(y_test.transpose(),y_hat_test)

    second_term = np.dot(y_test.transpose(),y_hat_test)
    error_mse_test = error_mse_test - second_term
    plt.figure(2)
    #♠plt.plot(y_hat_test,'g--',y_test.as_matrix(),'r--')
    plt.plot(y_hat_test,y_test.as_matrix())
    plt.title('Comparison y_hat_test and y_test')
    plt.figure(4)
    plt.hist(abs(y_test-y_hat_test),bins=50)
    plt.title('Histogram abs diff y_test and y_hat_test')
    plt.figure(6)
    plt.plot(w_hat)
    plt.title('w_hat_train')

    plt.show()

    #i take the w_hat estimated as frist assumption for the for iterative
    epsilon = 10e-6
    w_hat_next = np.random.randn(19,)
    gamma = 10e-8
    while np.linalg.norm(w_hat_next - w_hat) > epsilon:
        w_hat = w_hat_next
        delta_e = -2*np.dot(X_train.transpose(),y_train) + 2*np.dot(np.dot(X_train.transpose(),X_train),w_hat)
        #print ('d',delta_e)
        w_hat_next = w_hat - gamma*delta_e
        #print ('w',w_hat_next)
        
    
    #STEEPEST DESCENT
    w_hat = np.random.randn(19,)
```

```
  File "<ipython-input-1-bd22266dda1a>", line 1
    ```python
    ^
SyntaxError: invalid syntax
```

