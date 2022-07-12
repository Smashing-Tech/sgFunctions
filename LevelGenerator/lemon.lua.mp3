-- This file was automatically generated. Do not edit it manually.

function init()
	pStart = mgGetBool("start", true)
	pEnd = mgGetBool("end", true)
	
	mgMusic("28")
	mgFogColor(0.8, 0.76, 0.23, 0.92, 0.85, 0.4)
	
	confSegment("citrus/lemon/16_0", 1)
	confSegment("citrus/lemon/16_1", 1)
	confSegment("citrus/lemon/16_2", 1)
	confSegment("citrus/lemon/16_3", 1)
	confSegment("citrus/lemon/16_4_scoretop", 1)
	confSegment("citrus/lemon/8_0", 1)
	
	local accum_length = 0
	local room_length = 200
	
	if pStart then
		mgSegment("citrus/lemon/start", -accum_length)
	end
	
	while accum_length < room_length do
		accum_length = accum_length + mgSegment(nextSegment(), -accum_length)
	end
	
	if pEnd then
		mgSegment("citrus/lemon/end", -accum_length)
	end
	
	mgLength(accum_length)
end

function tick()
end
