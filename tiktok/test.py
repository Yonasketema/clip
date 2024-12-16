import subprocess

command = [
     'color=c=black:r=60:size=1080x1920:d=10[black];'
    '[0:v]format=pix_fmts=yuva420p,crop=w=2*floor(iw/2):h=2*floor(ih/2),'
    'zoompan=z=\'if(eq(on,1),1,zoom+0.000417)\':x=\'0\':y=\'ih-ih/zoom\':fps=60:d=60*4:s=1080x1920,'
    'crop=w=1080:h=1920:x=\'(iw-ow)/2\':y=\'(ih-oh)/2\',fade=t=in:st=0:d=1:alpha=0,fade=t=out:st=3:d=1:alpha=1,'
    'setpts=PTS-STARTPTS[v0];'
    '[1:v]format=pix_fmts=yuva420p,crop=w=2*floor(iw/2):h=2*floor(ih/2),'
    'pad=w=16200:h=10800:x=\'(ow-iw)/2\':y=\'(oh-ih)/2\',zoompan=z=\'if(eq(on,1),1,zoom+0.000417)\':x=\'0\':y=\'0\':fps=60:d=60*4:s=1080x1920,'
    'fade=t=in:st=0:d=1:alpha=1,fade=t=out:st=3:d=1:alpha=1,setpts=PTS-STARTPTS+1*3/TB[v1];'
    '[2:v]format=pix_fmts=yuva420p,crop=w=2*floor(iw/2):h=2*floor(ih/2),'
    'zoompan=z=\'if(eq(on,1),1,zoom+0.000417)\':x=\'0\':y=\'0\':fps=60:d=60*4:s=1350x1920,'
    'crop=w=1080:h=1920:x=\'(iw-ow)/2\':y=\'(ih-oh)/2\',fade=t=in:st=0:d=1:alpha=1,fade=t=out:st=3:d=1:alpha=0,'
    'setpts=PTS-STARTPTS+2*3/TB[v2];'
    '[black][v0]overlay[ov0];[ov0][v1]overlay[ov1];[ov1][v2]overlay=format=yuv420'
]


subprocess.run(command)