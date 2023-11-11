ukf = unscentedKalmanFilter(state_function,MeasurementFunction,0,'HasAdditiveMeasurementNoise',false);

state_noise = 0.2;

ukf.MeasurementNoise = state_noise;

phase_noise = 0.1;

ukf.ProcessNoise = phase_noise;

size_time = size ( Opti_Time );

end

for k = 1:size_time

	phase_corrected( k ) = correct ( ukf ) ;

	predict ( ukf );
	
end

nexttile

plot ( Opti_Time, phase_corrected)

title ( "Kalman Plot")
