function  Working_MATLAB()

ukf = unscentedKalmanFilter(state_function,MeasurementFunction,0,'HasAdditiveMeasurementNoise',false);

state_noise = 0.2;

ukf.MeasurementNoise = state_noise;

phase_noise = 0.1;

ukf.ProcessNoise = phase_noise;

i = 0;

while i <= 8192

	phase_corrected( i ) = correct ( ukf ) ;

	predict ( ukf );
    
    i = i + 1;
	
end

nexttile

plot ( Opti_Time, phase_corrected)

title ( "Kalman Plot")

end