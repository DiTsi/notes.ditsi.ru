# minio

### History

```bash
 9996  mcli config host add localhost:9000
10004  mcli mb myminio/test
10011  mcli config host add test http://localhost:9000 5Ktuc7FN004oLBa zECxfTZ0uCk00cw2V2tXNKHnR
10014  mcli admin info
10017  mcli config host list
10020  mcli config host list
10032  mcli ls test/
10033  mcli ls test
10034  mcli ls local
10035  mcli ls myminio
10037  mcli admin ohost list
10038  mcli admin host list
10039  mcli config host list
10040  mcli ls myminio
10041  mcli ls test
10047  mcli admin policy add myminio getonly getonly.json 
10049  mcli admin policy add myminio getonly getonly.json 
10051  mcli config host add myminio http://172.18.100.188:9000 minio minio123
10054  mcli admin user add myminio 
10058  mcli mb myminio/test
10066  mcli mb myminio/test
10093  mcli config host add localhost:9000
10095  mcli config host add myminio http://172.18.100.188:9000 minio minio123
10098  mcli admin user add myminio 
10102  mcli mb myminio/test
10110  mcli mb myminio/test
10120  mcli ls test/
10121  mcli ls test
10122  mcli ls local
10123  mcli ls myminio
10125  mcli admin ohost list
10126  mcli admin host list
10127  mcli config host list
10128  mcli ls myminio
10129  mcli ls test
10135  mcli admin policy add myminio getonly getonly.json 
10137  mcli admin policy add myminio getonly getonly.json 
10139  mcli config host add myminio http://172.18.100.188:9000 minio minio123
10142  mcli admin user add myminio 
10146  mcli mb myminio/test
10154  mcli mb myminio/test
10158  mcli admin policy set myminio getonly user=newuser
10159  mcli config host list
10162  mcli admin user list 
10163  mcli admin user list myminio
10165  mcli admin policy list myminio
10166  mcli admin policy info
10167  mcli admin policy info myminio
10168  mcli admin policy info getonly myminio
10169  mcli admin policy info readonly myminio
10170  mcli admin policy info readonly
10171  mcli admin policy info myminio getonly 
10175  mcli cp 1.tt myminio/test
10176  mcli ls myminio/test
10177  mcli ls test/test
10182  mcli admin user list
10183  mcli admin user list myminio
10185  mcli admin policy set test all all.json 
10186  mcli admin user add myminio newuser test
10187  mcli admin user add myminio test ohng2piD
10188  mcli admin user add myminio test ohng2piD
10190  mcli admin policy set myminio all user=test
10192  mcli admin policy add myminio all all.json
10194  mcli admin policy add myminio all all.json
10196  mcli admin policy set myminio all user=test
10197  mcli ls test/test
10198  mcli admin user ligs
10199  mcli admin user list
10200  mcli admin user list test
10201  mcli admin user list myminio
10202  mcli config host list
10204  mcli config host add usertest http://localhost:9000 test ohng2piD
10205  mcli ls usertest
10206  mcli ls usertest/test
10207  mcli ls usertest
10211  mcli admin user list
10212  mcli admin user list muminio
10213  mcli admin user list myminio
10215  mcli ls testuser
10216  mcli ls testuser/test
10217  mcli ls test
10218  mcli ls 
10219  mcli config host list 
10220  mcli ls
10222  mcli ls myminio
10223  mcli ls myminio/test
10224  mcli ls test/test
10225  mcli ls usertest/test
10227  mcli admin policy set myminio all user=test
10228  mcli admin policy add myminio all all.json
10230  mcli admin policy remove myminio all
10231  mcli admin policy add myminio all all.json
10233  mcli admin policy add myminio all all.json
10234  mcli admin policy set myminio all user=test
10235  mcli ls usertest/test
10236  mcli ls usertest

```