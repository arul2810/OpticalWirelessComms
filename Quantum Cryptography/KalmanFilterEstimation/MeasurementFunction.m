function Signal_Kalman = MeasurementFunction(phase_state, state_noise)

	Signal_Freq = 500000000

	Signal_Kalman =  ( ( sin ( 2 * pi  * Signal_Freq * Opti_Time + phase_state ) ) /2 )+ 0.5 + state_noise ;
	
end