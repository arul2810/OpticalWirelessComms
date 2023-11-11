

OutputPort1 = InputPort1;

record_signal = InputPort1.Sampled.Signal;

writematrix(record_signal,'tabledata.txt');

OutputPort1 = InputPort1;