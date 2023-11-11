
distance = [ 5, 10, 15, 20,25, 30,35, 40, 50, 60, 70, 80, 90];

key_rate_dist = [0.10927659948504431,0.06319907549128939,0.03815888108446125, 0.02323232049223578,0.013939469052777403,0.00803054604586892,0.00424595484578702,0.001831543731746585, -0.0006073892817226034, -0.0014084576616961789,  -0.0015081860706546435,-0.0013342522167625326,-0.0010810541423993004];

v_drift = [ 0.05,0.1,0.15,0.2,0.3,0.4];

key_rate_drift = [0.05332908328699895,-0.00239768109301014, -0.02323232049223578, -0.025246803842804033, -0.06543188529078703,-0.10059328402311385
];

figure

plot( distance,key_rate_dist, 'r-*');
title( 'Key Rate vs Distance');
xlabel ( ' Distance in Kms ' );
ylabel ('Secret Key Rate');

figure
semilogy( distance, key_rate_dist, 'r-*');
title ( ' KeyRate vs Distance ');
xlabel('Distance in Kms');
ylabel('Secret Key Rate');

figure
plot( v_drift,key_rate_drift , 'b-*');
title( 'Key Rate for Different V-Drift Values');
xlabel ( ' V Drift');
ylabel ('Secret Key Rate ');

figure

semilogy( v_drift,key_rate_drift , 'b-*');




