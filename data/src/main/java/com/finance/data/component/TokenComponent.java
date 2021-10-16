package com.finance.data.component;

import com.finance.data.exception.TokenException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Component
public class TokenComponent implements HandlerInterceptor {

    private final Logger logger = LoggerFactory.getLogger(this.getClass().getSimpleName());
    private final static String apiToken = "Pvk4coiwHqt3ZqQ8SfJD!";

    public boolean matches(String token) {
        return this.apiToken.equals(token);
    }

    public boolean matchesInHeader(HttpServletRequest httpServletRequest) {
        String token = httpServletRequest.getHeader("api_token");
        if (token == null || token.isBlank()) return false;
        return this.matches(token);
    }

    @Override
    public boolean preHandle(HttpServletRequest httpServletRequest, HttpServletResponse httpServletResponse, Object handler) {
        if (this.matchesInHeader(httpServletRequest)) return true;
        else {
            throw new TokenException("token is invalid");
        }
    }
}
